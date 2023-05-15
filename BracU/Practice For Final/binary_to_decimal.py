"""
def binaryToDecimal(n):
    return int(n,2)
"""

def binaryToDecimal(binary):
    decimal=0
    for digit in binary:
        print(int(digit))
        decimal = decimal * 2 + int(digit)
    return decimal

print(binaryToDecimal('10'))