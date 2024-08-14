import os

class Config:
    DATA_DIR = os.getenv("DATA_DIR", "data_pipeline/processed_data")
    MODEL_DIR = os.getenv("MODEL_DIR", "models/land_cover_model")
    LOG_DIR = os.getenv("LOG_DIR", "logs")

config = Config()
