import os,sys
import pickle

from src.logger import logging
from src.exception import CustomException

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


def save_object(obj, filepath):
    try:
        logging.info(f"Saving Object at {filepath}")
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path, exist_ok=True)
        with open(filepath, "wb") as f:
            pickle.dump(obj, f)

    except Exception as e:
        logging.error("Error in saving object")
        raise CustomException(e,sys.exc_info())
    
def evaluate_models(X_train,X_test,y_train,y_test,models,params):
    try:
        logging.info("Initiating Model Training")
        model_scores = {}
        for name,model in models.items():
            grid_search = GridSearchCV(model,params[name],cv=5,scoring='r2',n_jobs=-1)
            grid_search.fit(X_train,y_train)
            model.set_params(**grid_search.best_params_)
            model.fit(X_train,y_train)
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            model_scores[name] = {
                "train_score":r2_score(y_train,y_train_pred),
                "test_score":r2_score(y_test,y_test_pred)
            }
        logging.info("Model Training Completed")
        return model_scores
    except Exception as e:
        logging.error("Error in Model Training")
        raise CustomException(e,sys.exc_info())
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as f:
            obj = pickle.load(f)
        return obj
    except Exception as e:
        logging.error("Error in loading object")
        raise CustomException(e,sys.exc_info())

