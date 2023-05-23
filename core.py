print('task 0')
def hello():
    return "Hello!"
print(hello())

print('task 1')
def add(param1, param2):
    return param1 + param2
result=add(7, 2)
print(result)

print('task2')
def fizz_buzz(number):
    if number % 3==0 and number % 5==0:
        return "FizzBuzz"
    elif number % 3==0:
        return "Fizz"
    elif number % 5==0:
        return "Buzz"
    else:
        return str(number)
print(fizz_buzz(3))

print('task3')
def tri_area(base, heigh):
    tri=(base * heigh)/2
    return tri
print(tri_area(1,8))

print('task4')
def calculate_fuel(distance):
    fuel_needed = distance * 10
    if fuel_needed<100:
        fuel_needed=100
    return fuel_needed
print(calculate_fuel(45))


print('task5')
def both(number1, number2):
    if (number1 < 0 and number2 < 0) or (number1 > 0 and number2 > 0) or (number1 == 0 and number2 == 0):
        return True
    else:
        return False
print(both(-1,0))

print('task6')
def int_within_bounds(number, lower_bound, upper_bound):
    if not isinstance(number, int):
        return False
    if lower_bound<= number < upper_bound:
        return True
    else:
        return False
print(int_within_bounds(0,0,0))

print('task7')
def make10(a,b):
    if a==10 and b==10 or a+b==10:
        return True
    else:
        return False
print(make10(10,5))

print('task8')
def squares_sum(n):
    sum_of_squares=0
    for num in range(1, n+1):
        sum_of_squares += num **2
    return sum_of_squares
print(squares_sum(2))


print('task9')
def sum_even_nums_in_range(start, stop):
    sum=0
    for num in range(start, stop+1):
        if num % 2==0:
            sum+=num
    return sum
print(sum_even_nums_in_range(1, 10))

print('task10')
def mean(number):
   digits = [int(digit) for digit in str(number)]
   digit_sum=sum(digits)
   digit_count=len(digits)
   return digit_sum//digit_count
print(mean(128))