def basic_compress(text):
    words = text.split()
    seen = set()
    compressed = []
    for word in words:
        if word.lower() not in seen:
            compressed.append(word)
    seen.add(word.lower())
    return ' '.join(compressed)
