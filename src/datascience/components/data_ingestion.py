import os
import shutil
import urllib.request as request
from src.datascience.utils import logger 
from src.datascience.entity.config_entity import (DataIngestionconfig)

class Dataingestion:
    def __init__(self , config:DataIngestionconfig):
        self.config = config
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file)
            logger.info(f"file downloaded successfully and saved at: {filename}")
        else:
            logger.info(f"file already exists at: {self.config.local_data_file}")
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path , exist_ok=True)
        logger.info(f"data file already at: {self.config.local_data_file}, no extraction needed")