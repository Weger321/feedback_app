import os
import time
from datetime import datetime
from pathlib import Path
import fnmatch

class FileManagerApp:
    def __init__(self):
        self.current_directory = '.'
        self.show_hidden = False
        self.max_depth = 3
    
    def list_files(self):
        """Перечисляет файлы и папки в текущей директории."""
        items = os.listdir(self.current_directory)
        print(f"\nТекущая директория: {self.current_directory}\n")
        for item in items:
            path = os.path.join(self.current_directory, item)
            if os.path.isfile(path):
                print(f"F | {item}")
            elif os.path.isdir(path):
                print(f"D | {item}")
    
    def change_directory(self, new_dir):
        """Меняет рабочую директорию."""
        global current_directory
        try:
            os.chdir(new_dir)
            self.current_directory = os.getcwd()
            print(f"Текущая директория изменена на: {new_dir}")
        except OSError as err:
            print(err)
    
    def search_files(self, pattern, recursive=True):
        """Производит поиск файлов по маске в указанной директории."""
        start_time = time.time()
        matching_files = []
        
        for root, dirs, files in os.walk(self.current_directory):
            for file in files:
                if fnmatch.fnmatch(file, pattern):
                    matching_files.append(os.path.join(root, file))
        
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 2)
        
        print(f"\nНайдено файлов: {len(matching_files)}")
        print(f"Время поиска: {elapsed_time} секунд\n")
        
        for idx, file in enumerate(matching_files):
            size = os.path.getsize(file)
            modified_date = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M:%S')
            print(f"{idx+1}. {file}, Размер: {size / 1024:.2f} KB, Изменён: {modified_date}")
    
    def main_menu(self):
        """Основной экран интерфейса приложения."""
        while True:
            print("\n===== Файл Менеджер =====\n")
            print("1. Просмотреть файлы и папки")
            print("2. Перейти в директорию")
            print("3. Найти файлы")
            print("4. Настройки поиска")
            print("5. Выход")
            
            choice = input("\nВыберите пункт меню: ")
            
            if choice == '1':
                self.list_files()
            elif choice == '2':
                new_dir = input("Введите новую директорию: ")
                self.change_directory(new_dir)
            elif choice == '3':
                pattern = input("Введите маску поиска (например, '*.txt'): ")
                self.search_files(pattern)
            elif choice == '4':
                self.config_settings()
            elif choice == '5':
                print("Завершение работы...")
                break
            else:
                print("Некорректный выбор!")
    
    def config_settings(self):
        """Настройка параметров поиска."""
        print("\n== Настройки поиска ==")
        print("1. Показывать скрытые файлы")
        print("2. Установить максимальную глубину поиска")
        print("3. Назад")
        
        setting_choice = input("\nВыберите настройку: ")
        
        if setting_choice == '1':
            show_hide = input("Показывать скрытые файлы? (y/n): ")
            self.show_hidden = (show_hide.lower() == 'y')
        elif setting_choice == '2':
            depth = int(input("Максимальная глубина поиска (рекомендуемый максимум ~5): "))
            self.max_depth = depth
        elif setting_choice != '3':
            print("Некорректный выбор!")

if __name__ == '__main__':
    app = FileManagerApp()
    app.main_menu()1