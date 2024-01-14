# In Python, a tuple is an ordered,
# immutable collection of elements.
# Tuples are similar to lists
# but have the key difference that once a tuple is created,
# its elements cannot be modified, added, or removed.
# Tuples are defined using parentheses ()
# can contain elements of different data types.

tup = (1, 2, 3, 'a', 'a')
print(tup)

print(tup.count("a"))
print(tup.index("a"))

# Tuple to List
t_to_l = list(tup)
print(t_to_l)

# List to Tuple
l_to_t = tuple(t_to_l)
print(l_to_t)
