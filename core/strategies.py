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
