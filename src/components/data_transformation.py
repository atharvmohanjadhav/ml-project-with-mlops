import os,sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path= os.path.join("artifacts","data_transformation","preprocessor.pkl")
    

class DataTransformation():
    def __init__(self):
        self.transformation_config = DataTransformationConfig()

    def data_transformer_obj(self):
        try:
            num_col = ["writing_score","reading_score"]
            cat_col = ["gender","race_ethnicity","parental_level_of_education","lunch","test_preparation_course"]

            num_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy='most_frequent')),
                    ("one hot encoder",OneHotEncoder()),
                    ("scaling",StandardScaler(with_mean=False))
                ]
            )
            logging.info("Indivaidual Preprocessing completed!")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,num_col),
                    ("cat_pipeline",cat_pipeline,cat_col)
                ]
            )
            logging.info("All preprocessing done!")
            return preprocessor
    
        except Exception as e:
            raise CustomException(e,sys)
    
    def intiiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("read train and test data transformation completed!")

            logging.info("preprocessig started!")
            preprocesssor_obj = self.data_transformer_obj()

            target_column = "math_score"
            num_col = ["writing_score","reading_score"]
            
            x_train = train_df.drop(columns=[target_column],axis=1)
            x_test = test_df.drop(columns=[target_column],axis=1)

            y_train = train_df[target_column]
            y_test = test_df[target_column]

            preprocessed_x_train = preprocesssor_obj.fit_transform(x_train)
            preprocessed_x_test = preprocesssor_obj.transform(x_test)

            train_arr = np.c_[
                preprocessed_x_train,np.array(y_train)
            ]
            test_arr = np.c_[
                preprocessed_x_test,np.array(y_test)
            ]
            logging.info("saved preprocessed array!")

            save_object(file_path=self.transformation_config.preprocessor_obj_file_path,obj=preprocesssor_obj)
            return (train_arr,test_arr,)

        except Exception as e:
            raise CustomException(e,sys)
       
        


