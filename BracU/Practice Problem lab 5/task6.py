given_dict = { "Normal Skills":[10,15,20], "Ultimate Skill":50 }
sum=given_dict["Ultimate Skill"]
given_dict.pop("Ultimate Skill")
for i in given_dict.items():
    for j in i[1]:
        sum+=j


print("Additive Damage Score is",sum)
fisex_output="The agent's name is"
if(sum<= 70):
    print(fisex_output,"Rage")

elif(sum>70 and sum<=100):
    print(fisex_output,"Jett")
else:
    print(fisex_output,"Sage")

