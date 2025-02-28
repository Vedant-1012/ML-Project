# utils.py file in a Python project used to organize utility functions that are reusable across multiple scripts or modules.
import os
import sys
import numpy as np
import pandas as pd
import dill

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        # # Creates directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
            # dill is similar to Python’s built-in pickle module but can serialize more complex objects.

    except Exception as e:
        raise CustomException(e,sys)