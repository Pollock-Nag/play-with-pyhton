"""
# Palindromic Triangle

rows = 6                        #Pattern(1,121,12321,1234321,123454321)
for i in range(1, rows + 1):
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
"""


# Palindromic Pyramid

# Reading number of rows
row = int(input('Enter how many lines? '))-1

# Generating pattern
for i in range(1, row + 1):

    # for space
    for j in range(1, row + 1 - i):
        print(' ', end='')

    # for increasing pattern
    for j in range(1, i + 1):
        print(j, end='')

    # for decreasing pattern
    for j in range(i - 1, 0, -1):
        print(j, end='')

    # Moving to next line
    print()