from core.compressor import basic_compress
def run():
    print("[Replicant] Reading input file...")

  # Step 1: Open and read the input file
    with open("input/sample_date.txt", "r") as infile:
        raw_data = infile.read()

    print("[Replicant] Compressing data...")
    compressed_data = basic_compress(raw_data)

  # Step 2: Write the compressed result to a new output file
    with open("output/compressed_output.txt", "w") as outfile:
        outfile.write(compressed_data)

  print("[Replicant] Compression complete. Output saved to output/compressed_output.txt.")

if __name__ == "__main__":
    run()
