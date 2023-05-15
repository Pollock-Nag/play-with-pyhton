def create_Empty_adjList(no_of_nodes):
    d={}
    for i in range(no_of_nodes):
        d[i]=[]
    return d

def insert_val_adjList(adj_list,x,y):
    adj_list[x].append(y)
    adj_list[y].append(x)


def print_adjList(adj_list):
    for k,v in adj_list.items():
        print(k,"=>",v)

#*********** MAIN **********#
n= 6
e = 8

#creating an empty adj_list
adj_list=create_Empty_adjList(n)

#inserting val into adj list
for i in range(e):
    li = input().split(" ")
    x, y = int(li[0]), int(li[1])
    insert_val_adjList(adj_list,x,y)

#parinting adj_list
print_adjList(adj_list)