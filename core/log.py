import time

def log_compression(input_text, output_text, method="basic_compress", efficiency=None, runtime_ms=None):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    if runtime_ms is None:
        runtime_ms = "N/A"

    log_entry = (
        f"[{timestamp}] | Method: {method} | "
        f"Input length: {len(input_text)} | Output length: {len(output_text)} | "
        f"Efficiency: {efficiency}% | Runtime: {runtime_ms}ms\n"
    )

    with open("logs/replicant.log", "a") as logfile:
        logfile.write(log_entry)

def log_user_feedback(method, efficiency, feedback):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    feedback_entry = (
        f"[{timestamp}] | Method: {method} | "
        f"Efficiency: {efficiency}% | Feedback: {feedback}\n"
    )

    with open("logs/user_feedback.log", "a") as f:
        f.write(feedback_entry)
