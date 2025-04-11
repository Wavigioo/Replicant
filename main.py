from core.compressor import basic_compress
from core.log import log_compression
from core.analyze import analyze_compression
from core.reflect import analyze_log_history
from core.reflect import analyze_log_history, check_recent_efficiency
from core.strategies import choose_compression_method
import time

def run():
    print("[Replicant] Analyzing past performance...")
    history = analyze_log_history()

    if isinstance(history, dict):
        print(f"[Replicant] Past jobs: {history['total_runs']}")
        print(f"[Replicant] Avg Efficiency: {history['average_efficiency']}%")
        print(f"[Replicant] Best: {history['best_efficiency']}%, Worst: {history['worst_efficiency']}%")
        print(f"[Replicant] Most Used Method: {history['most_used_method']}")
    else:
        print(f"[Replicant] {history}")

    if check_recent_efficiency():
        print("[Replicant] Warning: Recent compression performance has been low.")
        print("[Replicant] Suggest evaluating alternate compression methods.")
        
    print("[Replicant] Reading input file...")
    with open("input/sample_data.txt", "r") as infile:
        raw_data = infile.read()

    print("[Replicant] Compressing data...")
    start_time = time.time()
    
    compressed_data, method_used = choose_compression_method(raw_data, strategy="smart")


    runtime_ms = round((time.time() - start_time) * 1000, 2)
    efficiency = analyze_compression(raw_data, compressed_data)
    log_compression(raw_data, compressed_data, method=method_used, efficiency=efficiency)

    if efficiency >= 25:
        log_compression(raw_data, compressed_data, efficiency=efficiency, runtime_ms=runtime_ms)
        print(f"[Replicant] Compression efficiency: {efficiency}%")
    else:
        print(f"[Replicant] Compression too low ({efficiency}%) — skipping log.")

    with open("output/compressed_output.txt", "w") as outfile:
        outfile.write(compressed_data)

    print("[Replicant] Compression complete. Output saved to output/compressed_output.txt.")

if __name__ == "__main__":
    run()
