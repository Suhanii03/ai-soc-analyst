def generate_summary(incidents):
    if not incidents:
        return "No suspicious activity detected. System appears normal."

    attack_counts = {}
    high_severity = 0
    ips = set()

    for incident in incidents:
        attack = incident["attack_type"]
        severity = incident["severity"]
        ip = incident["ip"]

        ips.add(ip)
        attack_counts[attack] = attack_counts.get(attack, 0) + 1

        if severity in ["High", "Critical"]:
            high_severity += 1

    # Build human-like explanation
    summary = f"In the recent analysis, {len(incidents)} security incidents were detected across {len(ips)} unique IP addresses. "

    for attack, count in attack_counts.items():
        if attack == "Brute Force Attack":
            summary += f"There were {count} brute-force attempts indicating possible password guessing attacks. "
        elif attack == "DDoS Suspicion":
            summary += f"{count} instances suggest potential distributed denial-of-service activity due to high traffic volume. "
        elif attack == "Anomaly Detected":
            summary += f"{count} anomalies were identified using machine learning, indicating unusual behavior patterns. "
        elif attack == "Suspicious Activity":
            summary += f"{count} suspicious activities involving unknown users were observed. "

    summary += f"A total of {high_severity} incidents were marked as high or critical severity, requiring immediate attention."

    return summary