def count_words(text):
    words = text.split()
    return len(words)

# Проверка
s = "Привет как дела"
print(count_words(s))
