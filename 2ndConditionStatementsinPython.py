
# ! If, Else % Elif statements

if 18 <= int(input('Enter age:\n')):
    print('Eligible for voting')

else:
    print('Can\'t vote')

a = 5
b = 10

if a > b:
    print('A is greater than B')

elif a == b:
    print('A is equal to B')

else:
    print('A is less than B')

name = input('Enter name:')

a = int(input('Enter Marks for subject 1:'))
b = int(input('Enter Marks for subject 2:'))
c = int(input('Enter Marks for subject 3:'))
d = int(input('Enter Marks for subject 4:'))
e = int(input('Enter Marks for subject 5:'))

if 90 <= ((a+b+c+d+e)/500)*100 <= 100:
    print('Grade S')

elif 80 <= ((a+b+c+d+e)/500)*100 < 90:
    print('Grade A')

elif 70 <= ((a+b+c+d+e)/500)*100 < 80:
    print('Grade B')
    
elif 60 <= ((a+b+c+d+e)/500)*100 < 70:
    print('Grade C')
    
elif 50 <= ((a+b+c+d+e)/500)*100 < 60:
    print('Grade D')
    
else:
    print('Grade F')

if True:
    print('Let\'s gooooooooooooo')

else:
    print('Its fine')

n = input('Enter a no.:')

if n==n[::-1]:

    print('Palindrome')

else:
    
    print('Not Palindrome')

# ! Ternerary operators

marks = 80

g = 'Good' if marks < 80 else 'b is min'