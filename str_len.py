'''var = list(map(lambda x: {x:len(x)}, ['Akash', 'Virat','Suresh','Adam']))
print(var)'''

l = ['Akash', 'Virat','Suresh','Adam']
var = set(map(lambda x:x.upper(),l))
print(var)