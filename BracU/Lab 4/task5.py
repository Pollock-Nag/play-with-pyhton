li=["hey","there","","what's","","up","","?"]

print("Original List:",li)
for i in li:
    if(i==""):
        li.remove(i)
print("Modified List:",li)