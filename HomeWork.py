def is_palidrome(stroke):
    return stroke == stroke[::-1]

print(is_palidrome('Шалаш'.lower()))
print(is_palidrome('Печенье'.lower()))
