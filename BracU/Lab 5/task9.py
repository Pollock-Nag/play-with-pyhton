exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
dict_ans={}
n=int(input())
for i in exam_marks.items():
    if(i[1]>=n):
        key=i[0]
        val=i[1]
        dict_ans[key]=val
print(dict_ans)
