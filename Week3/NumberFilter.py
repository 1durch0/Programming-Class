MyNumbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


def oddNumbersCount(array):
    oddNumbers = []
    for number in array:
        if number % 2 == 0:
            continue
        oddNumbers.append(number)
    return print(oddNumbers)

def evenNumbersCount(array):
    evenNumbers = []
    for number in array:
        if number % 2 != 0:
            continue
        evenNumbers.append(number)
    return print(evenNumbers)

oddNumbersCount(MyNumbers)
evenNumbersCount(MyNumbers)