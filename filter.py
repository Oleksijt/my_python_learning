
list_a = [1, 2, 3, 4, 5]

filter_obj = filter(lambda x: x % 2 == 0, list_a) # filter object <filter at 0x4e45890>

even_num = list(filter_obj) # Converts the filer obj to a list

print(filter_obj) # Output: [2, 4]