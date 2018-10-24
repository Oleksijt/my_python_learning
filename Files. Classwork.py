with open('files_test1.txt','a') as f:
    f.write('Some line.\nAnother line.\nMore line.\n')

with open('files_test1.txt','r') as f:
    info = f.read()
    print(info)

with open('files_test1.txt', 'r') as rf:
    # lines = rf.readlines()
    # for index, line in enumerate(lines):
    #     lines[index] = line.strip()
    # print(lines)

# with open('files_test1.txt', 'w') as wf:
#     wf.write('#\n'.join(lines))
