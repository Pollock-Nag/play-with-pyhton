exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}

num = int (input())

new_dict={}

for i in exam_marks.items():
   if(i[1]>=num):
       new_dict[i[0]]=i[1]
print(new_dict)