def getCount(inputStr):
    num_vowels = 0
    vovels = list(filter(lambda x: (x == 'a' or x == 'e' or x == 'i' or x == 'o'), str(inputStr)))
    num_vowels = len(vovels)  # your code here

    return num_vowels
print(getCount("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
