import os
import string

def extract_unique_words(input_path, output_folder):
    try:
        input_filename = os.path.basename(input_path)
        file_name_without_ext = os.path.splitext(input_filename)[0]

        with open(input_path, 'r', encoding='utf-8') as file:
            text = file.read()

        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = text.translate(translator).lower()

        words = cleaned_text.split()
        unique_words = sorted(set(words))

        output_filename = f"{file_name_without_ext}_extract.txt"
        output_path = os.path.join(output_folder, output_filename)

        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write("\n".join(unique_words))

        print(f"Unique words is save in file: {output_path}")

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях та спробуйте ще раз.")

    except Exception as e:
        print(f"Сталася помилка: {e}")
        
input_path = input("Введіть шлях до файлу, який потрібно проаналізувати: ")
output_folder = input("Введіть шлях до папки, де зберегти новий файл: ")

extract_unique_words(input_path, output_folder)
        
