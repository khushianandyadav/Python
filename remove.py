l = eval(input("Enter the list:- "))
num = int(input("Enter the number:- "))
print(l.count(num))
if l.count(num) > 1:
    l.remove(num)
    print(l)



