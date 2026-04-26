def generate_explanation(alert):
    if alert["type"] == "Brute Force Attack":
        return f"IP {alert['ip']} is attempting multiple failed logins, indicating a possible brute-force attack."

    elif alert["type"] == "DDoS Suspicion":
        return f"IP {alert['ip']} is sending an unusually high number of requests, indicating potential DDoS activity."

    elif alert["type"] == "Suspicious Activity":
        return f"Unknown user activity detected from IP {alert['ip']} with abnormal request patterns."

    elif alert["type"] == "Anomaly Detected":
        return f"Machine learning model detected unusual behavior from IP {alert['ip']}."

    return "No explanation available"