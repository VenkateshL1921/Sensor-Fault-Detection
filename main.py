from Sensor.configuration.mongo_db_connection import MongoDBClient
from Sensor.exception import SensorException
from Sensor.logger import logging
from Sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from Sensor.pipeline.training_pipeline import TrainPipeline
import os
import sys


# def test_exception():
#    try:
#        logging.info('We are dividing by zero')
#       div = 1/0
#    except Exception as e:
#        raise SensorException(e, sys)


# if __name__ == '__main__':
#    try:
#        test_exception()
#    except Exception as e:
#        print(e)

#mongo_client = MongoDBClient()
#print("collection name: ", mongo_client.database.list_collection_names())

if __name__ == '__main__':
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        logging.info(e)
