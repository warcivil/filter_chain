[WINDOWS] python main.py

[OS X / LINUX] python3 main.py

Формат фильтров. Стандартные фильтры располагаются в filters/filter.py, кастомные фильтры желательно располагать в той же директории(filter). Далее их нужно импортировать в configs/config.py и добавить в FILTER_SET. настройка порядка обхода там же

фильтры на вход должны принимать обьект типа dict и возвращать его же, то есть:

def <your_filter_name>(data:dict) -> dict:
  ...
