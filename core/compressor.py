def basic_compress(text):
    words = text.split()
    seen = set()
    compressed = []
    for word in words:
        normalized = word.lower().strip()
        if normalized not in seen:
            compressed.append(word)
            seen.add(normalized)
    return ' '.join(compressed)
