
#1
is_it_monday = False
if is_it_monday:
    print('it is monday')
else:
    print('it is not monday')


is_a_weekday = True
if is_a_weekday:
    print('it is a weekday')
else:
    print('it is not a weekday')


#c

number_of_hours = 20
hourly_rate = 10
if number_of_hours > 40:
    hourly_rate = hourly_rate + (hourly_rate * 0.5)
    print(number_of_hours * hourly_rate)
else:
    print(number_of_hours * hourly_rate)



#2

i = 5
while i <= 15:
    print(i)
    i += 1


i = 0
while i < 100:
    i += 2
    print(i)

i = 100
while i > -10:
    i -= 5
    print(i)

i = 2
while i < 1000000:
    print(i)
    i = (i*i)

i = 100
while i >= 5:
    print(i)
    i -= 5
  
   

#b
num = 7
for i in range(1,11):
    print(num, 'x', i, '=', num*i)

i = 1
for i in range(1,10):
    print(str(i) * i)



#3 


for fizzbuzz in range(101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

#4
num = int(input("enter number:"))
print(num)

print('number\tsquare\tcube')

for number in range(1, num):
    square = number * number
    cube = number * number * number
    # print the rows using f-strings
    print(f'{number}\t{square}\t{cube}')
    continue
_continue = str(input("do you want to continue? yes/no "))



#5

grade = int(input("enter grade:"))
print(grade)

if grade <= 100 and grade >= 88:
    print('A')
elif grade <= 87 and grade >= 80:
    print('B')
elif grade <= 79 and grade >= 67:
    print('C')
elif grade <= 66 and grade >= 60:
    print('D')
elif grade <= 59 and grade >= 0:
    print('F')

_continue = str(input("do you want to continue? yes/no "))





