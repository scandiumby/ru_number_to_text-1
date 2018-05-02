## ru_number_to_text
Преобразует число в слова прописью и добавляет 
валюту(по умолчанию валюта рубли/копейки),
которую можно задать

## Как установить?

pip install number_to_string

## Пример использования:

    from number_to_string import get_string_by_number

    string = get_string_by_number(123)
    assert string == 'Сто двадцать три рубля 00 копеек'


