from Sensor.exception import SensorException
from Sensor.logger import logging
from Sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from Sensor.pipeline.training_pipeline import TrainPipeline
import os
import sys
from fastapi import FastAPI
from Sensor.constant.application import APP_HOST, APP_PORT
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from fastapi.responses import Response
from Sensor.ml.model.estimator import ModelResolver, TargetValueMapping
from Sensor.utils.main_utils import load_object
from Sensor.constant.training_pipeline import SAVED_MODEL_DIR
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from Sensor.constant.training_pipeline import TARGET_COLUMN
import pickle
from Sensor.utils.main_utils import read_yaml_file
from Sensor.constant.training_pipeline import SCHEMA_FILE_PATH

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainPipeline()
        if train_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")
        train_pipeline.run_pipeline()
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.get("/predict")
async def predict_route():
    try:
        schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        filename = "C:/Users/venkatesh lotlikar/Desktop/Portfololio Projects/Sensor-Fault-Detection/artifact/01_11_2023_10_46_41/data_transformation/transformed_object/preprocessing.pkl"
        transformer = pickle.load(open(filename, "rb"))
        df = pd.read_csv(
            "C:/Users/venkatesh lotlikar/Desktop/Portfololio Projects/Sensor-Fault-Detection/artifact/01_11_2023_10_46_41/data_ingestion/feature_store/sensor.csv")
        df = pd.DataFrame(df)
        df1 = df.head(1)
        df2 = df1.drop(schema_config["drop_columns"], axis=1)
        model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not model_resolver.is_model_exists():
            return Response("Model is not available")

        best_model_path = model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)
        df1_features = df2.drop(TARGET_COLUMN, axis=1, inplace=True)
        df_transformed = transformer.fit_transform(df1_features)
        y_pred = model.predict(df_transformed)
        df1_features['predicted_column'] = y_pred
        df1_features['predicted_column'].replace(
            TargetValueMapping().reverse_mapping(), inplace=True)

        return {"predicted": y_pred}
    except Exception as e:
        raise Response(f"Error Occured! {e}")


def main():
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)
