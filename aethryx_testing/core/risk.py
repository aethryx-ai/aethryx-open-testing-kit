def classify_risk(level):
    levels = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    if level not in levels:
        return "UNKNOWN"
    return level


def from_vulnerability(vulnerable):
    return "HIGH" if vulnerable else "LOW"


def from_status(status):
    if status == "FAIL":
        return "CRITICAL"
    if status == "UNKNOWN":
        return "MEDIUM"
    return "LOW"
