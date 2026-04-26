from datetime import datetime
from backend.services.explanation_engine import generate_explanation

def generate_incident(alert):
    return {
        "timestamp": str(datetime.now()),
        "ip": alert["ip"],
        "attack_type": alert["type"],
        "severity": alert["severity"],
        "explanation": generate_explanation(alert),
        "recommended_action": get_recommendation(alert["type"])
    }

def get_recommendation(alert_type):
    if alert_type == "Brute Force Attack":
        return "Block IP and enable account lockout policies."

    elif alert_type == "DDoS Suspicion":
        return "Apply rate limiting and investigate traffic sources."

    elif alert_type == "Suspicious Activity":
        return "Monitor user activity and verify authentication."

    elif alert_type == "Anomaly Detected":
        return "Further investigate unusual behavior."

    return "No action defined"