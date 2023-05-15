def show_palindrome(num):
    ans=""
    for i in range(1,num+1):
        ans+=str(i)
    for i in range(num-1,0,-1):
        ans+=str(i)
    return ans
print(show_palindrome(3))