def collatz(number):
    if (number % 2) == 0:
        dividedEven = number//2
        print(dividedEven)
        return dividedEven
    else:
        oddNum = 3 * number + 1
        print(oddNum)
        return oddNum

userInp = int(input('Type in a number: '))

while userInp != 1:
    userInp = collatz(userInp)

