
# ! Filter Function

# * If we want to remove some elements from an iterable, we can use do it in one line

# * We can still keep the iterable

m = [59, 78, 90, 43]

r = list(filter(lambda x: x >= 70, m)) # * We want elements which are above 70

print(r)

# * Checking if vowels exist in a given word

a = list('hello')

r = list(filter(lambda x : x in 'aeiou', a))

print(r)

# * To check if no.s are divisible by 3

a = [1, 2, 3, 4, 5, 6]

print(list(filter(lambda x:x%3==0,a)))

# * Example of using both map and filter

a = ['Ram', 'Tejas', 'Aditya', 'Ravi', 'Dinesh', 'Raghu']

print(list(map(str.upper, filter(lambda x : len(x) > 5, a))))

# * For readability, we can write the above code as

r = filter(lambda x:len(x)> 5, a) # * Names with length above 5 are used

rr = map(str.upper, r) # * Used to uppercase the names we got above

print(list(rr))