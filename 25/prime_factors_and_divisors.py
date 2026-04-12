def prime_factors(number):
    """
    Разложение числа на простые множители
    """
    divs = []
    for _i in range(2, int(number ** 0.5) + 1):
        while number % _i == 0:
            divs.append(_i)
            number //= _i
    if number > 1:
        divs.append(number)
    return divs



def divisors(n):
    """
    Поиск всех делителей кроме единицы и самого себя
    """
    _divisors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            _divisors.append(i)
            _divisors.append(n // i)
    if int(n ** 0.5) ** 2 == n and n > 1:
        _divisors.pop()
    return _divisors
