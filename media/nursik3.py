#1
print(max(15,6))

#2
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizz_buzz"

    if number%3 == 0:
        return "fizz"
    if number % 5 == 0:
        return "buzz"

print(fizz_buzz(60))

#3
def check(number):
    if number<70:
        print("ok")
    else:
        points = (number-70)//5
        if points>12:
            print("license suspended")
        else:
            print("points:",points)

check(135)

#4
def showNumbers(limit):
    for x in range(limit):
        l = "even"
        if x%2 != 0:
            l = "odd"
        if x % 2 == 0:
            l = "even"

        print(x,l)

showNumbers(4)

#6
#start
def show_stars(rows):
    for x in range(rows):
        for y in range(x):
            print('*',end='')
        print()

show_stars(10)
