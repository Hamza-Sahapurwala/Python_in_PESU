
# ! Lists

l = [5,2,4,1,3]

l.sort() # * sort(reverse=True) for descending order

l.append(6)

l.append([7,8])

l.insert(3, 10) # * position, value to be appended

print(l)

def e():

    l.append(3)

print(e())

print(l)

for i in l[::-1]:
    
    print(i,end='')
