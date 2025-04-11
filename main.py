from core.compressor import basic_compress
from core.log import log_compression
from core.analyze import analyze_compression
from core.reflect import analyze_log_history

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
    print("[Replicant] Reading input file...")

    with open("input/sample_data.txt", "r") as infile:
        raw_data = infile.read()

    print("[Replicant] Compressing data...")
    compressed_data = basic_compress(raw_data)

    efficiency = analyze_compression(raw_data, compressed_data)

    if efficiency >= 25:
        log_compression(raw_data, compressed_data, efficiency=efficiency)
        print(f"[Replicant] Compression efficiency: {efficiency}%")
    else:
        print(f"[Replicant] Compression too low ({efficiency}%) — skipping log.")

    with open("output/compressed_output.txt", "w") as outfile:
        outfile.write(compressed_data)

    print("[Replicant] Compression complete. Output saved to output/compressed_output.txt.")

if __name__ == "__main__":
    run()
