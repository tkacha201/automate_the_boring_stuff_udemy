def div42by(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error you tried to devide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
