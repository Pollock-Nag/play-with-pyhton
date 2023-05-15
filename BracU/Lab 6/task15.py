grocery_items={"Rice":105,"Potato":20,"Chicken":250,"Beef":510,"Oil":85}

def price_calculator(order_items,location="Dhanmondi"):
    total=0
    for i in order_items:
        total+=grocery_items[i]
    if(location=='Dhanmondi'):
        total+=30
    else:
        total+=70
    return total



items=input().strip('[]').replace('"',"").split(", ")

print(price_calculator(items))