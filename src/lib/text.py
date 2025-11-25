import re
import unicodedata

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'е')
    
    text = ''.join(char if unicodedata.category(char)[0] != 'C' else ' ' for char in text)
    
    return ' '.join(text.split())

def tokenize(text: str) -> list[str]:
    return re.findall(r'[\w-]+', text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

if __name__ == "__main__":
    print("Testing normalize:")
    print(repr(normalize("Привет\nMup\t")))
    print(repr(normalize("Ежик, Ёлка")))
    print(repr(normalize("Hello\nNworld")))
    print(repr(normalize("двойные   пробелы")))
    
    print("\nTesting tokenize:")
    print(tokenize("привет мир"))
    print(tokenize("hello,world!!!"))
    print(tokenize("по-настоящему круто"))
    print(tokenize("2025 год"))
    print(tokenize("emoji 💬 не слово"))
    
    print("\nTesting count_freq + top_n:")
    tokens1 = ["a","b","a","c","b","a"]
    freq1 = count_freq(tokens1)
    print(freq1)
    print(top_n(freq1, 2))
    
    tokens2 = ["bb","aa","bb","aa","cc"]
    freq2 = count_freq(tokens2)
    print(freq2)
    print(top_n(freq2, 2))

def get_words(text):
    """Разбивает текст на слова (совместимость)"""
    normalized = normalize(text)
    return tokenize(normalized)

def count_words(words):
    """Подсчитывает количество слов (совместимость)"""
    return len(words)

def count_unique_words(words):
    """Подсчитывает количество уникальных слов (совместимость)"""
    return len(set(words))