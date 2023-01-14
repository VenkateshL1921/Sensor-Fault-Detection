# Sensor-Fault-Detection

## Problem Statement
Given the sensor data air pressure system (APS), identifying the failure caused by components of APS.
This is a binary classification problem where positive class indicates that failure is caused by certain componeny of APS while negative class indicates that failure is caused by something else and not by APS.

## Solution Implemented

1. Collect the data from sensors using kafka producer and consumer and store this data in mongoDB.
2. Extract the data from mongo DB and store it in CSV file.
3. Development of the project (data ingestion, validation, transformation, training and evaluation).
4. XGBoost classifer gave the best performance with 99.6% accuracy and reduced the cost (False negative and False positive) most.
5. Store the artifact collected in step 3 in AWS S3 bucket.
6. Start an EC2 instance, use AWS ECR for using docker and pull the the dockerfile in EC2 instance.
7. Use the github action for CI/CD pipeline.

## Tech stack Used

1. Python
2. Mongo DB
3. Confluent kafka
4. Machine learning algorithm
5. Docker
6. FastAPI
7. AWS S3, AWS ECR, AWS EC2
8. Git Actions

## Data Pipeline

![Data_Pipeline](https://user-images.githubusercontent.com/108605062/212458362-648a4ec7-ea27-41ef-bbe9-640f3c1cf933.png)

## Model Pipeline

![model_pipeline](https://user-images.githubusercontent.com/108605062/212458377-f0f0a059-33b8-40d7-9cbf-67a351d330ac.png)



