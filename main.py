import os
import time
from core.compressor import basic_compress
from core.log import log_compression, log_user_feedback
from core.analyze import analyze_compression
from core.reflect import (
    analyze_log_history,
    analyze_user_feedback,
    check_recent_efficiency,
    get_best_performing_method,
    suggest_method
)
from core.strategies import choose_compression_method

def ensure_directories():
    os.makedirs("logs", exist_ok=True)
    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)

def run():
    ensure_directories()

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
        print("[Replicant] Warning: Efficiency drop detected. 😕")

    print("[Replicant] Reading input file...")
    try:
        with open("input/sample_data.txt", "r") as infile:
            raw_data = infile.read()
    except FileNotFoundError:
        print("[Replicant] Error: input/sample_data.txt not found.")
        return

    print("[Replicant] Compressing data...")
    start_time = time.time()

    preferred_strategy = get_best_performing_method()
    override_strategy = "reverse" if check_recent_efficiency() else None

    print(f"[Replicant] Trending best method: {preferred_strategy}")
    suggestion = suggest_method()
    if suggestion:
        print(f"[Replicant] Suggestion: {suggestion}")

    compressed_data, method_used = choose_compression_method(
        raw_data,
        strategy=preferred_strategy,
        override=override_strategy
    )

    runtime_ms = round((time.time() - start_time) * 1000, 2)
    efficiency = analyze_compression(raw_data, compressed_data)

    if efficiency >= 25:
        log_compression(raw_data, compressed_data, method=method_used, efficiency=efficiency, runtime_ms=runtime_ms)
        print(f"[Replicant] Compression efficiency: {efficiency}%")
    else:
        print(f"[Replicant] Compression too low ({efficiency}%) — skipping log.")

    with open("output/compressed_output.txt", "w") as outfile:
        outfile.write(compressed_data)

    print("[Replicant] Compression complete. Output saved to output/compressed_output.txt.")

    feedback = input("[Replicant] How would you rate this compression? (good/bad/skip): ").strip().lower()

    if feedback in ["good", "bad"]:
        log_user_feedback(method_used, efficiency, feedback)
        print("[Replicant] Feedback received. Thank you. 🙂")
    else:
        print("[Replicant] Feedback skipped. 👍")

    feedback_data = analyze_user_feedback()
    if feedback_data:
        print("[Replicant] User Feedback Summary:")
        for sentiment, methods in feedback_data.items():
            top_method = max(methods, key=methods.get) if methods else "None"
            print(f" {sentiment.capitalize()}: Most common = {top_method}")

if __name__ == "__main__":
    run()
