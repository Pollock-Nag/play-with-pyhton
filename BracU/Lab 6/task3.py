def foo_moo(num):
    if(num%2==0 and num%3==0):
        return "FooMoo"
    elif(num%2==0):
        return "Foo"
    elif(num%3==0):
        return "Moo"
    else:
        return "Boo"

print(foo_moo(6))