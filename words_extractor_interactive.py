import os
import string
from tkinter import Tk, filedialog

def extract_unique_words(input_path, output_folder):
    try:
        # Отримуємо назву файлу без розширення
        input_filename = os.path.basename(input_path)
        file_name_without_ext = os.path.splitext(input_filename)[0]

        # Читаємо текст із файлу
        with open(input_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Видаляємо знаки пунктуації та приводимо до нижнього регістру
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = text.translate(translator).lower()

        # Розбиваємо текст на слова та створюємо список унікальних слів
        words = cleaned_text.split()
        unique_words = sorted(set(words))  # Сортуємо слова для зручності

        # Створюємо новий файл для запису результату
        output_filename = f"{file_name_without_ext}_extract.txt"
        output_path = os.path.join(output_folder, output_filename)
        
        # Записуємо унікальні слова у новий файл
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write("\n".join(unique_words))

        print(f"Унікальні слова збережено у файл: {output_path}")
    
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях та спробуйте ще раз.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def main():
    # Створюємо приховане головне вікно
    root = Tk()
    root.withdraw()  # Ховаємо основне вікно
    
    # Вибір файлу для аналізу
    print("Оберіть файл для аналізу")
    input_path = filedialog.askopenfilename(
        title="Оберіть текстовий файл",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    if not input_path:
        print("Файл не обрано. Програма завершена.")
        return

    # Вибір папки для збереження результату
    print("Оберіть папку для збереження результату")
    output_folder = filedialog.askdirectory(title="Оберіть папку для збереження")
    
    if not output_folder:
        print("Папку не обрано. Програма завершена.")
        return

    # Викликаємо функцію для аналізу
    extract_unique_words(input_path, output_folder)

if __name__ == "__main__":
    main()
