# ASIDA v2.0 Backend
# Flask-based API for forecasting, smart data, synthetic scenarios,
# streaming analytics, digital twins, and autonomous AI decisions.

from flask import Flask, request, jsonify
import datetime
import random

app = Flask(__name__)

# -------------------------------
# 1. Smart Data Layer
# -------------------------------
def smart_data_filter(raw_signals):
    curated = [s for s in raw_signals if "critical" in s.lower()]
    return curated

# -------------------------------
# 2. Synthetic Data Sandbox
# -------------------------------
def synthetic_scenario(occupancy, demand_factor):
    # Simple simulation: adjust occupancy by demand factor
    simulated = occupancy * (1 + demand_factor)
    return round(simulated, 2)

# -------------------------------
# 3. Streaming Analytics
# -------------------------------
def streaming_alerts(feed_data):
    alerts = []
    for f in feed_data:
        if f.get("value", 0) > f.get("threshold", 1):
            alerts.append(f"ALERT: {f['name']} spike detected!")
    return alerts

# -------------------------------
# 4. Digital Twin Simulation
# -------------------------------
def digital_twin(hotel_data):
    # Virtual replica simulation
    rooms = hotel_data.get("rooms", 100)
    occupancy_rate = hotel_data.get("occupancy_rate", 0.5)
    avg_rate = hotel_data.get("avg_rate", 5000)  # in KShs
    revenue = rooms * occupancy_rate * avg_rate
    energy_use = rooms * 5  # simple proxy
    return {"simulated_revenue": revenue, "energy_use": energy_use}

# -------------------------------
# 5. Autonomous AI Decision Layer
# -------------------------------
def ai_pricing_decision(occupancy, demand):
    if occupancy < 0.4 and demand > 0.7:
        return {"action": "Discount", "confidence": 0.85}
    elif occupancy > 0.85:
        return {"action": "Increase Price", "confidence": 0.9}
    else:
        return {"action": "Hold Price", "confidence": 0.7}

# -------------------------------
# 6. Immutable Forecast Ledger (Blockchain-style)
# -------------------------------
forecast_ledger = []

def log_forecast(entry):
    timestamp = datetime.datetime.now().isoformat()
    block = {"timestamp": timestamp, "entry": entry}
    forecast_ledger.append(block)
    return block

# -------------------------------
# API Endpoints
# -------------------------------

@app.route("/forecast", methods=["POST"])
def forecast():
    data = request.json
    occupancy = data.get("occupancy", 0.5)
    demand = data.get("demand", 0.5)

    decision = ai_pricing_decision(occupancy, demand)
    scenario = synthetic_scenario(occupancy, demand)
    block = log_forecast({"occupancy": occupancy, "demand": demand, "decision": decision})

    return jsonify({
        "decision": decision,
        "synthetic_scenario": scenario,
        "ledger_entry": block,
        "timestamp": block["timestamp"]
    })

@app.route("/alerts", methods=["POST"])
def alerts():
    feed_data = request.json.get("feeds", [])
    return jsonify({"alerts": streaming_alerts(feed_data)})

@app.route("/digital_twin", methods=["POST"])
def twin():
    hotel_data = request.json
    return jsonify(digital_twin(hotel_data))

@app.route("/ledger", methods=["GET"])
def ledger():
    return jsonify({"forecast_ledger": forecast_ledger})

# -------------------------------
# Run Server
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)