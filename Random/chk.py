try:
    n1=int(input())
    n2=int(input())

    print(n1/n2)

except Exception:
    print('Some Exception',end='||')
except ValueError:
    print('enter integer',end='||')
except ZeroDivisionError:
    print('sec num can not be zero',end='||')
except TypeError:
    print('num was not provides',end='||')