from fastapi import APIRouter
from backend.services.detection_engine import detect_threats
from backend.services.incident_generator import generate_incident
from backend.services.summary_engine import generate_summary 
from backend.services.auth_service import authenticate_user, create_token, verify_token
from fastapi import Header, HTTPException
router = APIRouter()

@router.get("/status")
def status():
    return {"status": "SOC system active"}

@router.post("/analyze")
def analyze_logs(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Token missing")

    token = authorization.split(" ")[1]
    user = verify_token(token)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    alerts = detect_threats("backend/data/sample_logs.csv")
    incidents = [generate_incident(alert) for alert in alerts]
    summary = generate_summary(incidents)

    return {
        "total_alerts": len(alerts),
        "incidents": incidents,
        "summary": summary
    }
@router.post("/ask")
def ask_soc():
    return {
        "response": "Most critical threats are brute-force attacks from suspicious IPs. Immediate blocking and monitoring is recommended."
    } 
@router.post("/login")
def login(username: str, password: str):
    if not authenticate_user(username, password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(username)
    return {"access_token": token}