import re
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, Side

from constants import INITIAL_PART, HEADERS, PATTERN, TITLE


def tasks_to_excel(
    tasks_file: Path,
    output_file: Path,
    initial_part: int = INITIAL_PART
) -> Path:
    """Извлекает информацию из Markdown и сохраняет их в .xlsx."""
    wb = Workbook()
    ws = wb.active
    ws.title = TITLE
    ws.append(HEADERS)

    text = tasks_file.read_text(encoding="utf-8")

    current_part = initial_part
    for match in re.finditer(PATTERN, text):
        part, number, question, pic = match.group(
            'part', 'number', 'question', 'pic'
        )
        if part is not None:
            current_part = int(part)
        ws.append([current_part, number, question, pic])

    line = Side(style="thin", color="000000")
    border = Border(top=line, bottom=line, left=line, right=line)

    for cell in ws[1]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = border

    for (cell,) in ws.iter_rows(min_row=2, min_col=1, max_col=1):
        cell.alignment = Alignment(horizontal="left", vertical="center")

    wb.save(output_file)
    return output_file


if __name__ == "__main__":
    saved = tasks_to_excel(Path("tasks_data.md"), Path("results.xlsx"))
    print(f"Сохранено: {saved}")
