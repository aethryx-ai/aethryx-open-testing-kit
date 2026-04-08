def send_to_aethryx(event):
    print("Sending event to Aethryx Control Plane:", event)

def log_decision_trace(input, output):
    send_to_aethryx({
        "type": "decision_trace",
        "input": input,
        "output": output
    })
