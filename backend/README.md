# FastAPI Backend

The backend provides the REST API used by the SocialIQ AI Complaint Management System.

## Main Responsibilities

- Receive citizen complaint requests
- Store complaint information
- Execute the AI prediction pipeline
- Save prediction results
- Return prediction results to the Streamlit frontend

## API

The main prediction endpoint is:

`POST /predict`

The FastAPI backend communicates with the AI service modules and trained machine-learning models.
