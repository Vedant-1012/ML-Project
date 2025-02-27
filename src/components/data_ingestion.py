# This file will have have code related to reading the data from dataset
import os
import sys #Importing this bcz we will be using our Custom Exception
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','data.csv')

# @dataclass: The @dataclass decorator automatically generates special methods for your class, 
# like __init__, __repr__, __eq__, etc. 
# os.path.join() to make the code OS-independent 


# This class will likely be responsible for loading the data, 
# performing any necessary preprocessing, 
# and saving the data in a suitable format for the next stages of the pipeline.
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            # os.path.dirname(self.ingestion_config.train_data_path): Extracts the directory from the file path. 
            # For "artifacts/train.csv", it returns "artifacts".
            # os.makedirs(): Creates directories recursively, including any missing intermediate directories.

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            # self.ingestion_config.raw_data_path: 
            # Specifies the file path where the CSV file will be saved (defined in your DataIngestionConfig).
            
            logging.info('Train_Test_Split initiated')
            train_set,test_set = train_test_split(df, test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of the data is completed')

            return (
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()
