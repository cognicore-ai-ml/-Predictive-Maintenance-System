# Industrial Predictive Maintenance Engine

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![ML-Engine](https://img.shields.io/badge/ML%20Engine-XGBoost-17a2b8.svg)](https://xgboost.readthedocs.io/)

An end-to-end Machine Learning solution designed to predict the **Remaining Useful Life (RUL)** of industrial equipment using time-series streaming sensor telemetry. This project moves from raw feature engineering to a deployable, high-performance inference API microservice.

---

## 📌 Project Architecture & Layout
The repository is structured following professional, scalable production software design practices:

```text
predictive-maintenance/
├── data/
│   ├── raw/                 # NASA CMAPSS original text files
│   └── processed/           # Transformed engineering matrices
├── models/                  # Serialized weights and artifacts (.pkl)
├── notebooks/               # Exploratory engineering analysis
│   └── 01_eda_and_baseline.ipynb
├── src/                     # Production grade code modules
│   ├── __init__.py
│   ├── preprocess.py        # Vectorization & cleaning steps
│   ├── train.py             # Training loop execution
│   └── app.py               # Operational microservice API (FastAPI)
├── requirements.txt         # Pinned virtual environment configurations
└── README.md                # Project landing portfolio gateway

## 🔌 API Verification & Documentation

Initialize the backend service application directly from your console terminal:

```bash
uvicorn src.app:app --reload --host 127.0.0.1 --port 8000
```

```json

{
  "sensor_readings": [518.67, 642.35, 1589.70, 1400.60, 14.62, 21.61, 554.36, 2388.06, 9044.07, 1.30, 47.47, 521.66, 2388.02, 8131.49, 8.41, 0.03, 392.00, 2388.00, 100.00, 39.06, 23.41]
}
  ```
 ```json
 {
    "predicted_remaining_cycles": 114.38
 }
 ```








