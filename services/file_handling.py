import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    """
    Извлекает часть текста (страницу), ограниченную размером 
    и обрезанную по последнему знаку препинания.
    """

    end = min(start + page_size + 1, len(text))  # Индекс конца страницы (не включая его)
    page_text = text[start:end]  # Текст страницы

    punctuation_pattern = re.compile(r'[,.!;:?]+')  # Регулярное выражение для знаков препинания

    # Последнее подходящее совпадение с конца
    last_match = next((
        match for match in reversed(list(punctuation_pattern.finditer(page_text)))
        if match.end() <= page_size and  # Не выходит за границы
        (not re.search(r"\.{2,3}", page_text) or match.end() != re.search(r"\.{2,3}", page_text).start()) 
        # Не многоточие или не совпадает с началом
    ), None)

    page_text = page_text[:last_match.end()] if last_match else page_text # Обрезаем, если есть совпадение

    return page_text, len(page_text)  # Текст и длина   

# Функция, формирующая словарь книги
def prepare_book(path) -> None:
    """
    Читает текстовый файл книги, разбивает его на страницы заданного размера
    и сохраняет в словаре book.
    """
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read() # Читаем весь текст книги из файла

    page_num = 1    # Номер текущей страницы
    start = 0       # Индекс текущей страницы
    end = 0         # Индекс конца текущей страницы
    while start < len(text):
        # Получаем текст страницы и ее длину с помощью _get_part_text
        page_text, length = _get_part_text(text, start, PAGE_SIZE)
        end = end + length # Вычисляем конец текущей страницы
        # Добавляем текст страницы в словарь book
        book[page_num] = page_text.lstrip()
        start = end   # Перемещаем индекс к следующей странице
        page_num += 1 # Увеличиваем номер страницы





# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))



