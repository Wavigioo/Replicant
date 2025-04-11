import time

def log_compression(input_text, output_text, method="basic_compress"):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (f"[{timestamp}] Method: {method} I " f"Input length: {len(input_text)} I Output length: {len(output_text)}\n")
    with open("logs/replicant.log", "a") as logfile: logfile.write(log_entry)
