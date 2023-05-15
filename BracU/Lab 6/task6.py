def year_month_days(num):

    year=(num//365)
    month= (num%365)//30
    day= (num%365)%30

    print(year,"years,",month,"months and",day,"days")
num = int(input())
year_month_days(num)