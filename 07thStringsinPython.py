
# ! Strings

s = 'p e s'

print(s.index('e')) # * Returns the index of the first occurence of given string in s (this will return 2) 

print(s.title()) # ! Uppercases all characters which are after space and first character

print(s.capitalize()) # ! Only first character is uppercased

s = ' p e s'

print(s.capitalize()) #  ! doesn't capitalize the first character if the the first character is not an alphabet

a = ' abc  xyz'

b = 'xyz'

print(a.join(b))

print(a.isalpha()) # * All characters should be alphabets to return True

t = 'Hello Sam!'

a = t.maketrans('S','p') # * This is replace function with extra steps

print(a)

print(t.translate(a)) # * This is the final step for replacing

print(b.partition('y'))

b = 'Hello My name'

print(b.partition('n')) # * This returns a tuple

# * Returns ('Hello My ', 'n', 'ame')

print(b.split('n')) # * This returns a list

print(b.encode(encoding='utf-8')) # * Encodes the string in utf-8

a = b.encode(encoding='utf-8')

print(a.decode()) # * Decodes the above encoded value