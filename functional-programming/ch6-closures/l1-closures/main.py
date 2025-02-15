def word_count_aggregator():
    count = 0
    def word_count(doc):
        words = doc.split()
        nonlocal count
        count += len(words)
        return count
    return word_count

