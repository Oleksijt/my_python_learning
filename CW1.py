import re

def song_decoder(song):
    s = song.replace('WUB', ' ')
    # s.replace('  ', '')
    s1 = s.replace(' +', '')
    s.strip()
    # re.sub(" +", '', s)
    # if s[0] == ' ':
    #     s = s[1:]
    # if s[len(s)-1] == ' ':
    #     s = s[:(len(s) - 1)]

    return s1

print(song_decoder('WUBAWUBWUBWUBBWUBWUBWUBC'))