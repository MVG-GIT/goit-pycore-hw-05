import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Регулярний вираз шукає числа з обов’язковими пробілами з обох боків
    # \s+ - пробіли, (\d+\.\d+|\d+) - число з десятковою крапкою або ціле число
    pattern = r'(?<=\s)(\d+\.\d+|\d+)(?=\s)'

    for match in re.finditer(pattern, text):
        yield float(match.group(1))


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))


# Приклад використання:
text = ("Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")  # Очікувано: 1351.46
