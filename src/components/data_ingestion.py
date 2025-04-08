import os,sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation,DataTransformationConfig
from src.components.model_trainer import ModelTrainer,ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join("artifacts","data_ingestion","train.csv")
    test_data_path:str=os.path.join("artifacts","data_ingestion","test.csv")
    raw_data_path:str=os.path.join("artifacts","data_ingestion","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Enterd the data ingestion method!")
        try:
            df = pd.read_csv(r"D:\MLOps Udemy Krish Naik\MLops Project\notebooks\data\student.csv")
            logging.info("Read data succesfully!")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("train test split intitaited!")

            train_df,test_df = train_test_split(df,test_size=0.2,random_state= 42)
            train_df.to_csv(self.ingestion_config.train_data_path,index = False,header = True)
            test_df.to_csv(self.ingestion_config.test_data_path,index = False,header = True)
            logging.info("Completed data ingestion!")

            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path,
                    self.ingestion_config.raw_data_path)
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    try:
        obj = DataIngestion()
        train_df,test_df,raw_df = obj.initiate_data_ingestion()

        data_trans_obj = DataTransformation()
        train_arr,test_arr = data_trans_obj.intiiate_data_transformation(train_df,test_df)

        model_trainer = ModelTrainer()
        model_trainer.initiate_model_trainer(train_arr=train_arr,test_arr=test_arr)


    except Exception as e:
        raise CustomException(e,sys)