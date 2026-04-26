# 🛡️ AI SOC Analyst

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Project-Active-success)

---

## 🔐 Overview

AI SOC Analyst is an intelligent cybersecurity monitoring system designed to simulate the workflow of a real Security Operations Center (SOC). It detects potential cyber threats using a combination of rule-based logic and machine learning, transforms raw log data into structured security incidents, and generates human-like analytical summaries to assist in rapid decision-making.

The system leverages behavioral analysis and anomaly detection techniques to identify attacks such as brute-force attempts, DDoS activity, and suspicious user behavior. Each detected threat is enriched with contextual explanations and actionable recommendations, making the output both technically insightful and easy to interpret.

With an interactive dashboard built using Streamlit and a secure FastAPI backend, the platform provides a complete end-to-end solution—from data ingestion and threat detection to visualization and reporting.

---

## 🚀 Features

- 🔍 **Threat Detection Engine**
  - Rule-based detection for brute-force, DDoS, and suspicious activity  
  - Behavioral analysis per IP  

- 🤖 **Machine Learning Anomaly Detection**
  - Isolation Forest for detecting unusual patterns  
  - Multi-feature analysis (request count, failed attempts, time-based behavior)  

- 📄 **Incident Generation**
  - Structured incident reports with severity and timestamps  
  - Attack classification and context  

- 🧠 **AI-Powered SOC Summary**
  - Human-like explanations of detected threats  
  - Insightful and readable analysis  

- 🛡️ **Actionable Recommendations**
  - Suggested mitigation steps for each attack  
  - Helps in quick decision-making  

- 📊 **Interactive Dashboard**
  - Built using Streamlit  
  - Expandable incident views  

- 🎛️ **Filters & Analytics**
  - Filter by severity and IP  
  - Visual charts for attack trends  

- 🔐 **Authentication System**
  - JWT-based login  
  - Protected API endpoints  

---

## 🛠️ Tech Stack

- **Backend:** FastAPI  
- **Frontend:** Streamlit  
- **Machine Learning:** Scikit-learn (Isolation Forest)  
- **Data Processing:** Pandas  
- **Authentication:** JWT (python-jose)  

---

## 📂 Project Structure
