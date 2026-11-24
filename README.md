# tasks-to-excel

Скрипт извлекает задания по физике из Markdown-файла и собирает их в Excel-таблицу с колонками «Часть», «Номер», «Вопрос», «Рисунок».

## Возможности

- Разбор заданий с группировкой по частям (`part`, `number`, `question`, `pic`)
- Оформление: жирный шрифт и рамка заголовка, выравнивание данных

## Установка

```bash
python -m venv .venv
source venv/Scripts/activate
pip install -r requirements.txt

```

## Использование
```bash
python tasks_to_excel.py

```
### По умолчанию читает tasks_data.md и сохраняет results.xlsx