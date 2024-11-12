import tkinter as tk
from tkinter import filedialog
import re

# Функція для видалення слів з знаками пунктуації, крім тире і апострофа
def clean_words(text):
    # Розділяємо текст на слова
    words = text.split()
    # Видаляємо слова, що містять знаки пунктуації окрім тире та апострофа
    cleaned_words = [word for word in words if re.match(r"^[\w'-]+$", word)]
    # Видаляємо повторювані слова
    unique_words = list(set(cleaned_words))
    return unique_words

# Функція для відкриття текстового файлу
def open_file():
    root = tk.Tk()
    root.withdraw()  # Ховаємо основне вікно
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text, file_path

# Функція для вибору папки для збереження результату
def save_file(words, input_file_path):
    root = tk.Tk()
    root.withdraw()  # Ховаємо основне вікно
    folder_path = filedialog.askdirectory()
    
    # Витягаємо ім'я вхідного файлу та створюємо нове ім'я для вихідного файлу
    input_file_name = input_file_path.split("/")[-1]
    output_file_path = f"{folder_path}/cleaned_{input_file_name}"
    
    # Записуємо слова у вихідний файл
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(words))
    print(f"Файл збережено за адресою: {output_file_path}")

# Основна функція програми
def main():
    # Крок 1: Відкрити файл і прочитати текст
    text, input_file_path = open_file()
    
    # Крок 2: Видалити непотрібні слова та отримати унікальні
    unique_words = clean_words(text)
    
    # Крок 3: Вибрати папку для збереження файлу
    save_file(unique_words, input_file_path)

# Виконуємо програму
if __name__ == "__main__":
    main()
