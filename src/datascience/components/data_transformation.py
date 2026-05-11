import os
from src.datascience.utils import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.datascience.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path, header=None, names=["vendor","model","MYCT","MMIN","MMAX","CACH","CHMIN","CHMAX","PRP","ERP"])
        data = data.drop(columns=["vendor", "model", "ERP"])
        train , test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info(f"splitting is done and train and test files are saved in {self.config.root_dir}")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)