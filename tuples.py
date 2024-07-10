tuple1 = (10, 20, 30, 40, 50)
tuple2 = (5, 15, 25, 35, 45)
max_value = max(tuple1)
min_value = min(tuple1)
print(f"Max value in tuple1: {max_value}")
print(f"Min value in tuple1: {min_value}")
sum_tuples = tuple(a + b for a, b in zip(tuple1, tuple2))
print(f"Sum of tuple1 and tuple2: {sum_tuples}")
duplicate_tuple = tuple1 * 2
print(f"Duplicated tuple: {duplicate_tuple}")
sliced_tuple = tuple1[1:4]  
print(f"Sliced tuple: {sliced_tuple}")
tuple_as_list = list(tuple1)
print(f"List obtained from tuple1: {tuple_as_list}")
