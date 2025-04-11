import random
from .compressor import basic_compress


def reverse_compress(text):
    return ' '.join(reversed(text.split()))

def choose_compression_method(text, strategy="basic"):
    if strategy == "basic":
        return basic_compress(text), "basic"
    elif strategy == "reverse":
        return reverse_compress(text), "reverse"
    elif strategy == "smart":

        methods = [
            ("basic", basic_compress),
            ("reverse", reverse_compress)
        ]
        chosen_name, chosen_func = random.choice(methods)
        return chosen_func(text), chosen_name
    else:
        raise ValueError(f"Unknown compression strategy: {strategy}")
from .compressor import basic_compress


def reverse_compress(text):
    return ' '.join(reversed(text.split()))

def choose_compression_method(text, strategy="basic"):
    if strategy == "basic":
        return basic_compress(text), "basic"
    elif strategy == "reverse":
        return reverse_compress(text), "reverse"
    else:
        raise ValueError(f"Unknown compression strategy: {strategy}")
