from .compressor import basic_compress
from .reflect import analyze_log_history
import random

def reverse_compress(text):
    return ' '.join(reversed(text.split()))

available_methods = {
    "basic": basic_compress,
    "reverse": reverse_compress
}

def choose_compression_method(text, strategy="basic", override=None):
    # Forced override logic
    if override in available_methods:
        return available_methods[override](text), override

    # Smart strategy (learn from logs)
    if strategy == "smart":
        log_summary = analyze_log_history()

        if isinstance(log_summary, dict):
            best_method = log_summary.get("most_used_method", "basic")
            chosen_func = available_methods.get(best_method, basic_compress)
            return chosen_func(text), best_method
        else:
            # No history? Choose randomly
            chosen_name, chosen_func = random.choice(list(available_methods.items()))
            return chosen_func(text), chosen_name

    # Default strategy behavior
    if strategy in available_methods:
        return available_methods[strategy](text), strategy
    else:
        raise ValueError(f"Unknown compression strategy: basic")
