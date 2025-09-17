def count_words(text):
    words = text.split()
    
    return len(words)

def count_chars(text, ignore_case=True):
    chars = {}
    for i in range(0, len(text) - 1):
        c = text[i]
        if ignore_case:
            c = c.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_char_counts(char_counts):
    char_list = []
    for c in char_counts:
        char_list.append({
            "char": c,
            "num": char_counts[c]
        })
    def ordering(char_record):
        return char_record["num"]
    char_list.sort(reverse=True, key=ordering)
    return char_list