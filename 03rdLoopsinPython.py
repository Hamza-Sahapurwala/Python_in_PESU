
# ! While Loop:

i = 10

while i!=0:
    print('Hello')
    i-=1

i = 10

while i!=20:
    print(i)
    if i == 15:
        break
    i+=1
i = 10
while i!=20:
    if i == 15:
        i+=1
    print(i)
    i+=1

i = 10

while i < 21:
    if i>=15:
        i+=1
    print(i)
    i+=1

print(100//6)
print(100%6)

# ! For Loops

for i in range(6):
    print(i,end='')

print()

for i in 'python':
    print(i)

a = 1

for i in range(9):
    
    for j in range(1,4):
    
        print(a,'\t',j)

    a+=1
    
    if a == 4:
        
        break

for i in range(1,4):

    for j in range(1,4):

        print(i,'\t',j)

n = int(input())

while n!=0:
    d = n % 10
    print(d)
    n//=10

n = int(input())

r = 0

while n!=0:
    a=n%10
    r *= 10 + a
    n//=10

n = int(input('Enter a no. for checking if it is amstrong or not:'))

s = 0

while n!=0:
    s = s + ((n%10)**3)

for i in range(1,6):
    for j in range(i):
        print(i,end='')
    print()

