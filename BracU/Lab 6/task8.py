def show_palindrome(num):
    ans=""
    for i in range(1,num+1):
        ans+=str(i)
        ans+=" "
    for i in range(num-1,0,-1):
        ans+=str(i)
        ans+=" "
    return ans

def show_palindromic_triangle(num):
    for i in range(1,num+1):
        for j in range (1,num-i+1):
            print(" ",end=" ")
        print(show_palindrome(i))


show_palindromic_triangle(5)