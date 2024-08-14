
# Sustainable Infrastructure Development Project

## Overview
This project aims to use satellite imagery for sustainable infrastructure development and conservation. The system uses machine learning models to classify land cover and assess the suitability of different areas for infrastructure development.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run data ingestion: `python data_pipeline/data_ingestion.py`.
4. Run data preprocessing: `python data_pipeline/data_preprocessing.py`.
5. Train the model: `python models/land_cover_model.py`.
6. Build and deploy the Docker container: `docker-compose up --build`.

## Usage
Upload satellite images via the FastAPI REST API to get predictions on land cover classification and infrastructure suitability.

## Monitoring
Monitor the deployed model using Prometheus and Grafana dashboards.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
