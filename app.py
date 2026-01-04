import streamlit as st
import pandas as pd

st.set_page_config(page_title="Public Health AI Monitor")

st.title("AI-Assisted Public Health Data Quality & Risk Monitor")

# Sample dataset (simulating Snowflake table)
data = pd.DataFrame({
    "patient_id": ["P001","P002","P003","P004","P002","P005"],
    "age": [34,67,None,150,67,22],
    "district": ["District_A","District_A","District_B","District_B","District_A","District_C"],
    "symptom": ["fever","cough","breathing_issue","fever","cough","headache"]
})

st.subheader("Health Records")
st.dataframe(data)

# Data quality checks
data["age_issue"] = data["age"].isna() | (data["age"] < 0) | (data["age"] > 120)

quality = data.groupby("district").agg(
    total_records=("patient_id","count"),
    age_issues=("age_issue","sum"),
    duplicate_records=("patient_id", lambda x: x.duplicated().sum())
)

st.subheader("Data Quality Issues by District")
st.dataframe(quality)

# Risk signal
risk = data.groupby("district").agg(
    risk_cases=("symptom", lambda x: x.isin(
        ["fever","cough","breathing_issue"]
    ).sum())
)

st.subheader("Health Risk Signals")
st.dataframe(risk)

# AI-style summary
st.subheader("AI-Generated Summary")
st.success(
    "District_B shows high risk due to abnormal age values and frequent fever-related symptoms. "
    "District_A shows moderate risk due to duplicate patient records. "
    "District_C currently shows low risk."
)