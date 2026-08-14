# 🏛️ SocialIQ AI Complaint Management System

## Artificial Intelligence Powered Citizen Complaint Management Platform

SocialIQ AI Complaint Management System is an AI-powered citizen complaint management platform designed to automatically analyze, classify, prioritize, and process citizen complaints.

The system combines a **Streamlit frontend**, **FastAPI backend**, **machine-learning models**, and **PostgreSQL database** to provide an intelligent complaint-processing workflow.

A submitted complaint is processed through multiple AI modules and the results are displayed through an interactive dashboard.

---

# 🎯 Project Objective

The main objective of SocialIQ is to reduce the manual effort involved in handling citizen complaints.

The system automatically analyzes a complaint and provides:

- Complaint classification
- Department prediction
- Priority prediction
- Sentiment analysis
- Feedback category prediction
- Emergency detection
- Harmful-content detection
- Trend forecasting
- Anomaly detection
- Government action recommendation

This allows complaints to be analyzed quickly and helps identify urgent, abnormal, or potentially harmful complaints.

---

# 🤖 AI Modules

SocialIQ contains 10 major AI modules.

| No. | Module | Purpose |
|---|---|---|
| 1 | Complaint Reason Classification | Identifies the main reason/category of the complaint |
| 2 | Department Prediction | Predicts the government department responsible for the complaint |
| 3 | Sentiment Analysis | Determines the sentiment expressed in the complaint |
| 4 | Feedback Category Prediction | Classifies the type of citizen feedback |
| 5 | Priority Prediction | Determines the priority level of the complaint |
| 6 | Emergency Detection | Identifies emergency-related complaints |
| 7 | Harmful Content Detection | Detects potentially harmful content |
| 8 | Trend Forecasting | Identifies complaint trends |
| 9 | Anomaly Detection | Detects unusual or abnormal complaint patterns |
| 10 | Government Action Recommendation | Suggests an appropriate government action |

---

# 🏗️ System Architecture

The overall workflow of the system is:

```text
                    🏛️ SocialIQ AI
                           │
                           ▼
                  Streamlit Frontend
                           │
                           ▼
                    FastAPI Backend
                           │
                           ▼
                      predict_all()
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
     Department        Sentiment        Priority
     Prediction        Analysis         Prediction
          │                │                │
          ├────────────────┼────────────────┤
          │                │                │
          ▼                ▼                ▼
      Emergency        Feedback         Harmful
      Detection        Category         Content
          │                │                │
          └────────────────┼────────────────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
      Trend Forecasting          Anomaly Detection
             │                           │
             └─────────────┬─────────────┘
                           ▼
              Government Action
                 Recommendation
                           │
                           ▼
                    PostgreSQL
