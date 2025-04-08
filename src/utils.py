import pandas as pd
import numpy as np
import os,sys
from src.exception import CustomException
from src.logger import logging
import dill
from sklearn.metrics import r2_score

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok= True)
        with open(file_path,"wb") as file:
            dill.dump(obj,file)

    except Exception as e:
        raise CustomException(e,sys)

def eval_model(x_train,y_train,x_test,y_test,models):
    try:
        report ={}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            model.fit(x_train,y_train)

            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            train_score = r2_score(y_train,y_train_pred)
            test_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_score
        return report
        
    except Exception as e:
        raise CustomException(e,sys)