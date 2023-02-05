def checkio(num: int) -> str:
    """ return Fizz if the number is divisible by 3. if not, return the input as string"""
    if num%3 == 0:
        return 'Fizz'
    else:
        return str(num)
