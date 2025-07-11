import sys
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        # Неправильний формат рядка, повертаємо пустий словник
        return {}
    date, time, level, message = parts
    return {
        'date': date,
        'time': time,
        'level': level.upper(),  # для уніфікації
        'message': message
    }

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, encoding='utf-8') as f:
            for line in f:
                log_entry = parse_log_line(line)
                if log_entry:
                    logs.append(log_entry)
    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не знайдено.")
        sys.exit(1)
    except IOError as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    # Використовуємо list comprehension (елемент функціонального програмування)
    return [log for log in logs if log.get('level') == level]

def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log.get('level', 'UNKNOWN')] += 1
    return dict(counts)

def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<17} | {'Кількість':<8}")
    print(f"{'-'*17}-|{'-'*9}")
    for level, count in sorted(counts.items()):
        print(f"{level:<17} | {count:<8}")

def main():
    # Перевірка аргументів командного рядка
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу> [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if filter_level:
        filtered_logs = filter_logs_by_level(logs, filter_level)
        print(f"\nДеталі логів для рівня '{filter_level.upper()}':")
        if filtered_logs:
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print("Записів цього рівня не знайдено.")

if __name__ == "__main__":
    main()
