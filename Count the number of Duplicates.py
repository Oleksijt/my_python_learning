# def duplicate_count(text):
s = 'aabBcde'
# print(len([c for c in set(s.lower()) if s.lower().count(c)>1]))
print([c for c in set(s.lower()) if s.lower().count(c)>1])


# text = text.lower()
# print(text)
# count = 0
# lis_t = list(text)
# my_dict = dict()
# for i in lis_t:
#     if i in my_dict:
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1
# for el in my_dict:
#     if my_dict[el] > 1:
#         count += 1


