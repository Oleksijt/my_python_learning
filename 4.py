def accum(s):
    zm = '-'.join((a*i).title() for i, a in enumerate(s, 1))

    return zm

print(accum('dsgsgjyjktyyt'))
