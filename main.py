from core.compressor import basic_compress
from core.log import log_compression
from core.analyze import analyze_compression

def run():
    print("[Replicant] Reading input file...")

    with open("input/sample_data.txt", "r") as infile: raw_data = infile.read()

    print("[Replicant] Compressing data...")
    compressed_data = basic_compress(raw_data)

    # Analyze and Log
    efficiency = analyze_compression(raw_data, compressed_data)
    log_compression(raw_data, compressed_data, efficiency=efficiency)

    print(f"[Replicant] Compression efficiency: {efficiency}%")


    with open("output/compressed_output.txt", "w") as outfile:
        outfile.write(compressed_data)

    print("[Replicant] compression complete. Output saved to output/compressed_output.txt.")

if __name__ == "__main__":
    run()
