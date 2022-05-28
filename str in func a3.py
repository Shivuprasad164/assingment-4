import string


def reverse(str):
    string=" "
    for i in str:
        string = i+ string
    return string
str = input("enter the word:")
print("the original string is:",string)
print("the reverse string is:",reverse(str))   