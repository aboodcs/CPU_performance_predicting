import os
import sys
import yaml
import logging
from pathlib import Path
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from box.exceptions import BoxValueError
from src.datascience.utils import logger

# @ensure_annotations → ensures path_to_yaml is actually a Path object
# Input: path to YAML file
# Output: ConfigBox object
@ensure_annotations 
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the yaml file.

    Raises:
        ValueError: If the yaml file is empty.
        e: Any exception raised while reading the yaml file.      
    
    Returns:
        ConfigBox: ConfigBox object containing the yaml data.
    """

    try:
        with open(path_to_yaml)as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list , verbose=True):
    for path in path_to_directories:
        os.makedirs(path , exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
        

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data , f , indent=4)
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) ->ConfigBox:
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded from: {path}")
    return ConfigBox(content) 


@ensure_annotations
def save_bin(path: Path , data: Any):
    joblib.dump(value=data , filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(filename=path)
    logger.info(f"binary file loaded from: {path}")
    return data