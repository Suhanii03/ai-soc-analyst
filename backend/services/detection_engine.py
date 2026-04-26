# 📦 Imports
import pandas as pd
from sklearn.ensemble import IsolationForest


# 🧱 PART 1: Load logs
def load_logs(file_path):
    df = pd.read_csv(file_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df


# ⚡ PART 2: Severity calculation
def calculate_severity(total_requests, failed_attempts):
    if total_requests > 150 or failed_attempts > 20:
        return "Critical"
    elif total_requests > 80 or failed_attempts > 10:
        return "High"
    else:
        return "Medium"


# 📏 PART 3: Improved Rule-based detection (per IP behavior)
def rule_based_detection(df):
    alerts = []

    ip_groups = df.groupby('ip')

    for ip, group in ip_groups:
        total_requests = group['request_count'].sum()
        failed_attempts = group[group['status_code'] == 401]['request_count'].sum()

        severity = calculate_severity(total_requests, failed_attempts)

        # 🚨 Brute force detection
        if failed_attempts > 10:
            alerts.append({
                "type": "Brute Force Attack",
                "ip": ip,
                "severity": severity,
                "message": f"{failed_attempts} failed login attempts detected"
            })

        # 🚨 DDoS detection
        if total_requests > 100:
            alerts.append({
                "type": "DDoS Suspicion",
                "ip": ip,
                "severity": severity,
                "message": f"High traffic volume: {total_requests} requests"
            })

    return alerts


# 🤖 PART 4: Improved ML anomaly detection
def ml_anomaly_detection(df):
    # Feature engineering
    df['hour'] = df['timestamp'].dt.hour
    df['is_failed'] = df['status_code'].apply(lambda x: 1 if x == 401 else 0)

    features = df[['request_count', 'is_failed', 'hour']]

    # ML model
    model = IsolationForest(contamination=0.15, random_state=42)
    df['anomaly'] = model.fit_predict(features)

    anomalies = df[df['anomaly'] == -1]

    alerts = []
    for _, row in anomalies.iterrows():
        alerts.append({
            "type": "Anomaly Detected",
            "ip": row['ip'],
            "severity": "Medium",
            "message": f"Unusual pattern detected (requests: {row['request_count']})"
        })

    return alerts


# 🔗 PART 5: Combine everything
def detect_threats(file_path):
    df = load_logs(file_path)

    rule_alerts = rule_based_detection(df)
    ml_alerts = ml_anomaly_detection(df)

    return rule_alerts + ml_alerts