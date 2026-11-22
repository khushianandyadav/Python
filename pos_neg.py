l = eval(input("Enter the list:- "))
c1 =0
c2 =0
for i in l:
    if i>= 0:
        c1+=1
    else:
        c2+=1
print("Count of positive numbers is", c1)
print("Count of negative numbers is", c2)