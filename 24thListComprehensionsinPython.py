
# ! List Comprehensions

# Syntax: listvariable = [expression for <variable> in <iterable> [if condition]]

l = [i for i in range(11) if i%2==0] # * Even no. are put in the list

l = [i ** 3 for i in range(11)] # * Cube of no. till 10 are put in list

words = ['Hi','how','are','you']

items = [i[-1] for i in words] # * Last letter of each word is put in the list

l1 = [1,2,3,4]

l2 = [2,3,4,5]

print([a for a in l1 for b in l2 if a == b]) # * To print similar elements

city = ['Bangalore', 'Mysore', 'Chennai', 'Hyderabad']

a = [[i,len(i)] for i in city] # * City with their length

print(a)

a = [i ** 2 for i in range(11) if i%2==1] # * Odd sqaures are printed

print(a)

# * Transpose of a matrix

mat = [[1,2], [3,4], [5,6], [7,8]]

transpose = [[row[i] for row in mat] for i in range(2)]
