s1 = input('vedite slovo: ')
s2 = input('vedite slovo: ')
s1="".join(set(s1))
s2="".join(set(s2))
k = 0
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            k += 1
print(k,' sovpadeniye')
if k > 0:
    print('YES')
else:
    print('NO')

    # ss1="".join(set(s1))
    # ss2="".join(set(s2))
    # k = 0
    # for i in range(len(ss1)):
    #     for j in range(len(ss2)):
    #         if ss1[i] == ss2[j]:
    #             k += 1
    # if k > 0:
    #     return 'YES'
    # else:
    #     return 'NO'