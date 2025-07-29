import argparse
import sys


def calc(a: float, operator: str, b: float) -> float:
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            raise ValueError("Деление на ноль!")
    else:
        raise ValueError(f"Неизвестный оператор: {operator}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Простой калькулятор. Принимает два числа и оператор, пример: 2 + 2")
    parser.add_argument('a', type=float, help="Первое число")
    parser.add_argument('operator', choices=['+', '-', '*', '/'], help="Оператор (+, -, *, /)")
    parser.add_argument('b', type=float, help="второе число")
    args = parser.parse_args()

    try:
        result = calc(args.a, args.operator, args.b)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(2)
    print(result)
