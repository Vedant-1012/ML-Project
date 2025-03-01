# Model training will happened here
import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import(AdaBoostRegressor,RandomForestRegressor,GradientBoostingRegressor)
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score
from xgboost import XGBRegressor
from catboost import CatBoostRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting training and test input data")
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1], # All the rows and all the columns except the last one
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                'Random Forest': RandomForestRegressor(),
                'Decision Tree': DecisionTreeRegressor(),
                'Linear Regression': LinearRegression(),
                'AdaBoostRegressor': AdaBoostRegressor(),
                'XGBoost Regressor' : XGBRegressor(),
                'GradientBoostingRegressor' : GradientBoostingRegressor(),
                'CatBoost Regressor' : CatBoostRegressor(verbose=False),
                'KNeighborsRegressor' : KNeighborsRegressor()
                
            }

            model_report:dict = evaluate_model(X_train, y_train,X_test,y_test,models)
            
            # To get the best model score from dict
            best_model_score = max(sorted(model_report.values()))

            # Get the best model name
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best Model found")
            
            logging.info("Best found Model on Training and Testing dataset")
            
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )

            predicted = best_model.predict(X_test)

            r2_square =r2_score(y_test,predicted)

            logging.info(f"Best model R2 score: {r2_square}")
             # Return the best model, score, and R2 score for further use
            return best_model, best_model_score, r2_square


            

        except Exception as e:
            raise CustomException(e,sys)
            


