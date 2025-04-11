def analyze_compression(input_text, output_text):
    input_len = len(input_text)
    output_len = len(output_text)

    if input_len == 0:
        return 0.0 # Avoid division by zero

    efficiency = (1 - (output_len / input_len)) * 100
    return round(efficiency, 2)
