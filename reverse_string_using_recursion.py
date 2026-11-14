def reverse(s,index):
    if index < 0:
        return ""
    return s[index] + reverse(s, index-1)
s= input("Enter the string:- ")
print(s)
result = reverse(s, len(s)-1)
print(result)