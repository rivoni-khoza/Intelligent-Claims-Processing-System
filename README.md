# Intelligent-Claims-Processing-System

## Overview
This project automates and summarizes insurance claim documents using a Large Language Model (LLM) integrated with Azure services. It supports faster triaging, reduces manual effort, and improves fraud detection accuracy.

## Business Problem
Claims departments face inefficiencies due to manual processing, inconsistent classification, and delayed decision-making. This solution accelerates claim handling and provides real-time insights.
-  **LLMs for text summarization and classification**
-  **Azure services** for data processing and deployment
-  **Exploratory Data Analysis (EDA)** for insight generation
-  **Business Intelligence (BI)** for claims monitoring
-  **Data engineering and modeling** for structured data integration


## Tech Stack
- LLM: OpenAI  (via LangChain)
- Cloud: Azure Functions, Blob Storage, Data Factory
- Data Processing: PySpark on Azure Databricks
- Data Warehouse: Azure Synapse Analytics
- Visualization: Power BI
- Tools: VSCode, Git, PowerShell, SQL Server Management Studio

## Key Features
- Automated classification of claims via LLM
- Real-time summarization of claim narratives
- Fraud pattern scoring using keyword embeddings
- Power BI dashboard for executive monitoring

Data Source
New York State Workers’ Compensation Claims Dataset

**Dataset:** [Assembled Workers’ Compensation Claims: Beginning 2000](https://data.ny.gov/Government-Finance/Assembled-Workers-Compensation-Claims-Beginning-20/jshw-gkgu)

**Source:** [data.ny.gov](https://data.ny.gov)

Format: JSON (via API) 

Update Frequency: Quarterly

Coverage: 2006 – Present

Domain: Insurance claims from workers across various industries in New York State

Official, real-world, anonymized dataset
