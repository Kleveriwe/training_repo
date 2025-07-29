def calc(a  : int, operator: str, b:int)-> int:
    try:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError('на ноль делить нельзя')
            return a / b
        else:
            return f'Ошибка: неподдерживаемый оператор {operator}'

    except ValueError:
        return 'Ошибка: a и b должны быть числами.'

    except SyntaxError:
        print('Ошибка: оператор должен быть строкой (например, "+", "-")')

    except Exception as e: # этот отбор из gpt взял, но с ним лучше
        return f'Ошибка: {e}'

# ВОПРОС, ты в условии её не прописывал, но как мне кажется нужно перехватить еще ошибку, если оператор не str
# (БЕЗ КАВЫЧЕК)
# print(calc(5,/,8))
# но если я прописываю
# if not isinstance(operator, str):
#             return "Ошибка: оператор должен быть строкой (например, '+', '-')"
# или
# except SyntaxError:
#         print('Ошибка: оператор должен быть строкой (например, "+", "-")')
# она не уходит
# и вот эта gpt строчка (    except Exception as e:
#         return f'Ошибка: {e}')
#
#         как я понял вообще должна перехватывать все иные ошибки,
# но эта все равно вылетает в терминале
# её можно как-то нашаманить ?
# и нужно ли ахах?