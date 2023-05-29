import os,sys
from dataclasses import dataclass

from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier
)
from catboost import CatBoostClassifier
from xgboost import XGBRegressor

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import r2_score

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object,evaluate_models


@dataclass
class ModelTrainerConfig:
    trainer_model_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self) :
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split the data into train and test")
            X_train,y_train = train_array[:,:-1],train_array[:,-1]
            X_test,y_test = test_array[:,:-1],test_array[:,-1]

            logging.info("Initiating Model Training")
            models = {"Random Forest": RandomForestClassifier(),
                      "Gradient Boosting": GradientBoostingClassifier(),
                      "Ada Boost": AdaBoostClassifier(),
                      "Cat Boost": CatBoostClassifier(),
                      "XG Boost": XGBRegressor(),
                      "Linear Regression": LinearRegression()}
            params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    'splitter':['best','random'],
                },
                "Random Forest":{
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "CatBoosting Regressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    'n_estimators': [8,16,32,64,128,256]
                }
                
            }

            model_report = evaluate_models(X_train,X_test,y_train,y_test,models,params)
            best_model_score = max([model["test_score"] for model in model_report.values()])          
            best_model_name = [model_name for model_name,model in model_report.items() if model["test_score"]==best_model_score][0]

           
            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best Model is {best_model_name}")

            save_object(
                obj=models[best_model_name],
                filepath=self.model_trainer_config.trainer_model_path
            )

            predicted_values = models[best_model_name].predict(X_test)
            r2_score_ = r2_score(y_test,predicted_values)

            logging.info(f"R2 Score of the model is {r2_score_}")
            return r2_score_
        
        except Exception as e:
            logging.error("Error in Model Training")
            raise CustomException(e,sys.exc_info())

            