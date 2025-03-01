# utils.py file in a Python project used to organize utility functions that are reusable across multiple scripts or modules.
import os
import sys
import numpy as np
import pandas as pd
import dill

from sklearn.metrics import r2_score

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

def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        for i, (model_name, model) in enumerate(models.items()):
            print(f"Training model: {model_name}")  # Debugging log

            model.fit(X_train, y_train)  # Train the model

            y_train_pred = model.predict(X_train)  # Predictions on train data
            y_test_pred = model.predict(X_test)    # Predictions on test data

            train_model_score = r2_score(y_train, y_train_pred)  # Train R2 score
            test_model_score = r2_score(y_test, y_test_pred)      # Test R2 score

            # Add the model's test score to the report
            report[model_name] = test_model_score

            print(f"Model {model_name} - Test Score: {test_model_score}")  # Debugging log

        # Ensure the report is not empty
        if not report:
            raise CustomException("Model evaluation returned an empty report")

        return report

    except Exception as e:
        print(f"Error in evaluate_model: {e}")  # Log error message for debugging
        raise CustomException(f"Error in evaluate_model: {str(e)}", sys)


