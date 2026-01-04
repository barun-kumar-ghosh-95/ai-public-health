# AI-Assisted Public Health Data Quality & Risk Monitor

This project is an AI-for-Good prototype designed to help public health teams identify
data quality issues and early health risk signals from public health datasets.

The solution is designed to run entirely inside Snowflake using Snowflake SQL,
Snowflake Streamlit, and AI SQL. Due to Snowflake trial activation time, the prototype
is demonstrated locally using Streamlit with the same schema and logic.

## Problem
Public health datasets often contain missing values, duplicate records, and inconsistent
reporting, which hide early warning signs and delay intervention.

## Solution
The application automatically:
- Performs data-quality checks (missing, invalid, duplicate records)
- Aggregates district-level health risk signals
- Generates plain-language AI-style summaries for non-technical users

## Technology Stack
- Python
- Streamlit
- SQL

## Snowflake Tools Used
- Snowflake SQL Worksheets
- Snowflake Streamlit
- Snowflake AI SQL (Snowflake Intelligence)

## Deployment
In production, this application runs fully inside Snowflake using Snowflake tables,
SQL Worksheets, Snowflake Streamlit, and AI SQL without external infrastructure.

## Demo
The working prototype is demonstrated via a Streamlit application and screenshots
included in the prototype deck.
