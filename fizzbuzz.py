def fizzbuzz(n: int):
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(f'Введенное вами число {i} не кратно ни 3, ни 5')


fizzbuzz(27)
