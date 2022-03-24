import random

def isValidNumber(number):
    try:
        numberList = list(str(number))
        if len(set(numberList)) == 4:
            return True
        return False
    except:
        return False

def checkCowBull(number_guess, number_computer):
    i_cow, i_bull = [], []
    try:
        number_guess_list = list(str(number_guess))
        number_computer_list = list(str(number_computer))
        for index in range(len(number_guess_list)):
            if number_computer_list[index] == number_guess_list[index]:
                i_bull.append(index)
            elif number_guess_list[index] in number_computer_list:
                i_cow.append(index)
        return i_cow, i_bull
    except:
        return i_cow, i_bull

numberForGuess = 0
numberOfComputer = 0
countOfTry = 0
index_cow = []
index_bull = []

while not isValidNumber(numberOfComputer):
    numberOfComputer = random.randint(1000, 9999)

index_cow, index_bull = checkCowBull(numberForGuess, numberOfComputer)

print("Введите число:")
while len(index_bull) != 4:
    countOfTry += 1
    numberForGuess = int(input())
    number_guest_list = list(str(numberForGuess))
    if not isValidNumber(numberForGuess):
        print("Все цифры должны быть разными!")
    else:
        if numberForGuess == numberOfComputer:
            print(f"Попытка: {countOfTry}; Число: {numberForGuess}; Число, которое нужно отгадать: {numberOfComputer}")
        else:
            index_cow, index_bull = checkCowBull(numberForGuess, numberOfComputer)
            print(f"Попытка: {countOfTry}; Количество быков: {len(index_bull)}; коров: {len(index_cow)}")