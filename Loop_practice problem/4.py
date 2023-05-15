
start=int(input())
end=int(input())

for year in range(start,end+1):

    if(year%4==0 or year%400==0 and year!=100 ):
        print(year,end=" ")
    else:
        pass