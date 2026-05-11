import os
import pandas as pd
from src.datascience.entity.config_entity import DataValidationConfig
from src.datascience.utils import logger

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self):
        try:
            validate_status = None
            data = pd.read_csv(os.path.join(self.config.unzip_data_dir, "machine.data"), header=None, names=["vendor","model","MYCT","MMIN","MMAX","CACH","CHMIN","CHMAX","PRP","ERP"])
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            validate_status = True
            for col in all_schema:
                if col not in all_cols:
                    validate_status = False
                    break
            
            with open(self.config.STATUS_FILE, "w") as f:
                if validate_status:
                    f.write("Validation status: Passed")
                else:
                    f.write("Validation status: Failed")
            return validate_status
        except Exception as e:
            logger.exception(e)