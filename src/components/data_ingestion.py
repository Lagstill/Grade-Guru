import os,sys
import pandas as pd

from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass #no need init its a decorator when no functions
class DataIngestionConfig:
    train_data_path : str=os.path.join('artifacts',"train.csv")
    test_data_path : str=os.path.join('artifacts',"test.csv")
    raw_data_path : str= "data\Performance_data.csv"

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try: # can be a Mysql/mongdb client
            logging.info("Initiating Data Ingestion")
            df = pd.read_csv(self.ingestion_config.raw_data_path)
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            train,test = train_test_split(df,test_size=0.2,random_state=42)
            train.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Data Ingestion Completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.error("Data Ingestion Failed")
            raise CustomException(e,sys.exc_info())
        

if __name__ == "__main__":
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()