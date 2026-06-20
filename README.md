# End-to-End MLOps Customer Churn Intelligence Platform

An end-to-end machine learning application that predicts telecom customer churn and provides business-focused insights through an interactive dashboard.

## Live Demo

Dashboard:
https://end-to-end-mlops-customer-churn-platform-vzusimhxbgchrasmnkgud.streamlit.app/

API:
https://customer-churn-api-z5wl.onrender.com/

API Documentation:
https://customer-churn-api-z5wl.onrender.com/docs

---

## Overview

This project uses the IBM Telco Customer Churn dataset to predict whether a customer is likely to leave a telecom service provider.

The application combines:

* Machine Learning model training
* FastAPI model serving
* Streamlit dashboard
* Docker containerization
* Cloud deployment

Users can enter customer details and receive:

* Churn probability
* Customer risk assessment
* Revenue-at-risk estimation
* Business insights and retention recommendations

---

## Dataset

**IBM Telco Customer Churn Dataset**

Dataset Link:
https://www.ibm.com/communities/analytics/watson-analytics-blog/guide-to-sample-datasets/

Target Variable:

* Churn (Yes/No)

Features:

* Customer demographics
* Service subscriptions
* Contract details
* Billing information
* Customer tenure

---

## Model Performance

| Metric   | Score  |
| -------- | ------ |
| Accuracy | 78.56% |
| F1 Score | 64.55% |

Model Used:

* Random Forest Classifier

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* FastAPI
* Streamlit
* Plotly
* Docker
* Git & GitHub
* Render

---

## Project Structure

```text
end-to-end-mlops-customer-churn-platform/

├── app/
│   ├── main.py
│   └── schema.py
│
├── models/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   └── features.pkl
│
├── src/
│   └── train.py
│
├── dashboard.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Start Streamlit dashboard:

```bash
streamlit run dashboard.py
```

---

## Docker

Build image:

```bash
docker build -t customer-churn-api .
```

Run container:

```bash
docker run -p 8000:8000 customer-churn-api
```

---

## Deployment

* FastAPI API deployed on Render
* Streamlit Dashboard deployed on Streamlit Community Cloud

---

## Author

Aanand Mahawal

GitHub:
https://github.com/aanandmahawal
