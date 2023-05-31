import sys,os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e, sys.exc_info())
                
class CustomData:
    def __init__(self,
                gender: str,
                race_ethnicity: str,
                parental_level_of_education,
                lunch: str,
                test_preparation_course: str,
                reading_score: int,
                writing_score: int):

        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_dataframe(self):
        try:
            columns = ['gender', 'race/ethnicity', 'parental level of education', 'lunch','test preparation course', 'reading score', 'writing score']
            var = [self.gender,self.race_ethnicity,self.parental_level_of_education,self.lunch,self.test_preparation_course,self.reading_score,self.writing_score]
            data = {}
            for col in columns:
                data[col] =  [var[columns.index(col)]]
            return pd.DataFrame(data)
        
        except Exception as e:
            raise CustomException(e, sys.exc_info())
        
        
