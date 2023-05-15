def calculate_tax(age,salary,designation):
    tax=0
    if(age<18 or degisnation=="president" or salary<10000):
        tax=0
    elif(salary>=10000 and salary<=20000):
        tax=(salary*(5/100))
    elif(salary>20000):
        tax=(salary*(10/100))
    return tax



age = int(input("please enter age "))
salary =int(input("please enter salaty "))
degisnation=input("please enter designation ").lower()

print(calculate_tax(age,salary,degisnation))