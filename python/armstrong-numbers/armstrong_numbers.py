def is_armstrong_number(number):
    power = len(str(number))
    return number == sum((int(num) ** power for num in str(number)))
