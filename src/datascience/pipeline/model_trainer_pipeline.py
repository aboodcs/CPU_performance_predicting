from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_trainer import ModelTrainer
from src.datascience.utils import logger

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    def initiate_model_trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()