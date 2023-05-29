import os,sys
import pickle

from src.logger import logging
from src.exception import CustomException

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
