import os,sys
import pandas as pd
import numpy as np
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.utils import save_object

import warnings
warnings.filterwarnings('ignore')

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path : str=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        try:
            logging.info("Getting Data Transformer Object")
            numerical_columns = ['reading score','writing score',]
            categorical_columns = [
                'gender', 'race/ethnicity', 'parental level of education', 'lunch','test preparation course'
            ]

            numerical_transformer = Pipeline(
                steps = [("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
            )

            categorical_transformer = Pipeline(
                steps = [("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))]
            )

            logging.info(f"Categorical Columns: {categorical_columns}")
            logging.info(f"Numerical Columns: {numerical_columns}")

            preprocessor = ColumnTransformer(
                transformers = [
                    ("num", numerical_transformer, numerical_columns),
                    ("cat", categorical_transformer, categorical_columns),
                ]
            )

            logging.info("Data Transformer Object Created")
            return preprocessor
        except Exception as e:
            logging.error("Error in getting data transformer object")
            raise CustomException(e,sys.exc_info())
    
    def initiate_data_transformation(self,train_path,test_path):
        try:
            logging.info("Initiating Data Transformation")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Data Loaded Successfully")
            preprocessor = self.get_data_transformer_object()
            logging.info("Data Transformer Object Created")

            target_column_name = "math score"

            input_feature_train = train_df.drop(target_column_name, axis=1)
            target_feature_train = train_df[target_column_name]

            input_feature_test = test_df.drop(target_column_name, axis=1)
            target_feature_test = test_df[target_column_name]

            logging.info("Data Transformation Started")

            input_feature_train_arr = preprocessor.fit_transform(input_feature_train)
            input_feature_test_arr = preprocessor.transform(input_feature_test)
            train_arr = np.concatenate((input_feature_train_arr, target_feature_train.values.reshape(-1, 1)), axis=1)
            test_arr = np.concatenate((input_feature_test_arr, target_feature_test.values.reshape(-1, 1)), axis=1)

            save_object (filepath=self.transformation_config.preprocessor_obj_file_path, obj = preprocessor)
            logging.info("Data Transformation Completed")

            return(
                train_arr,
                test_arr,
                self.transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            logging.error("Error in initiating data transformation")
            raise CustomException(e,sys.exc_info())

            
