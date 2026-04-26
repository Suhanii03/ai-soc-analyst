import streamlit as st
import requests
import pandas as pd

# Config
st.set_page_config(page_title="AI SOC Analyst", layout="wide")

API_BASE = "http://127.0.0.1:8000"
ANALYZE_URL = f"{API_BASE}/analyze"
LOGIN_URL = f"{API_BASE}/login"

# Session state
if "token" not in st.session_state:
    st.session_state.token = None

# ---------------- LOGIN PAGE ----------------
if not st.session_state.token:
    st.title("🔐 AI SOC Analyst Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = requests.post(
            LOGIN_URL,
            params={"username": username, "password": password}
        )

        if response.status_code == 200:
            st.session_state.token = response.json()["access_token"]
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials")

    st.stop()

# ---------------- MAIN DASHBOARD ----------------

st.title("🛡️ AI SOC Analyst Dashboard")

# Logout button
if st.sidebar.button("Logout"):
    st.session_state.token = None
    st.rerun()

# Sidebar controls
st.sidebar.header("Controls")
run_analysis = st.sidebar.button("Run Threat Analysis")

# Filters
st.sidebar.subheader("Filters")
selected_severity = st.sidebar.multiselect(
    "Filter by Severity",
    ["Critical", "High", "Medium"]
)

selected_ip = st.sidebar.text_input("Filter by IP")

# Run analysis
if run_analysis:
    with st.spinner("Analyzing logs..."):
        headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

        response = requests.post(ANALYZE_URL, headers=headers)

        if response.status_code == 200:
            data = response.json()

            st.success("Analysis Complete")

            # Summary
            st.subheader("📊 SOC Summary")
            st.write(data["summary"])

            # Convert to DataFrame
            df = pd.DataFrame(data["incidents"])

            # Apply filters
            if selected_severity:
                df = df[df["severity"].isin(selected_severity)]

            if selected_ip:
                df = df[df["ip"].str.contains(selected_ip)]

            # Metrics
            col1, col2 = st.columns(2)
            col1.metric("Total Alerts", data["total_alerts"])
            col2.metric("Filtered Incidents", len(df))

            # 📊 Attack Type Chart
            st.subheader("📈 Attack Type Distribution")
            if not df.empty:
                st.bar_chart(df["attack_type"].value_counts())
            else:
                st.warning("No data for selected filters")

            # 📊 Severity Chart
            st.subheader("⚠️ Severity Distribution")
            if not df.empty:
                st.bar_chart(df["severity"].value_counts())

            # 🚨 Incident Details
            st.subheader("🚨 Detected Incidents")
            if not df.empty:
                for _, incident in df.iterrows():
                    with st.expander(f"{incident['attack_type']} - {incident['ip']}"):
                        st.write(f"**Severity:** {incident['severity']}")
                        st.write(f"**Explanation:** {incident['explanation']}")
                        st.write(f"**Recommended Action:** {incident['recommended_action']}")
                        st.write(f"**Timestamp:** {incident['timestamp']}")
            else:
                st.warning("No incidents match your filters")

        elif response.status_code == 401:
            st.error("Session expired. Please login again.")
            st.session_state.token = None
            st.rerun()
        else:
            st.error("Failed to connect to backend")

else:
    st.info("Click 'Run Threat Analysis' to start")