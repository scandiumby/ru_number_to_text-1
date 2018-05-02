## ru_number_to_text
Преобразует число в слова прописью и добавляет 
валюту, которую можно задать 
(по умолчанию валюта рубли/копейки)

## Как установить?

    pip install number_to_string

## Пример использования:

    from number_to_string import get_string_by_number

    string = get_string_by_number(123)
    assert string == 'Сто двадцать три рубля 00 копеек'

    currency_main = ('тенге', 'тенге', 'тенге')
    currency_additional = ('тиын', 'тиына', 'тиынов')
    string = get_string_by_number(
        325, 
        currency_main, 
        currency_additional,
    )
    assert string == 'Триста двадцать пять тенге 00 тиынов'
    
## Скоро:

Добавление английского языка