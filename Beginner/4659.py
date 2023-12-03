
vowel = "aeiou"
res = []
while (t := input()) != 'end':
    answer = ''
    tmp_s = ''
    cnt_vowel = 0
    cnt_consonant = 0
    # 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    if len(set(t) & set(vowel)) == 0:
        answer = f"<{t}> is not acceptable."
        res.append(answer)
        continue

    for i in t:
        if i in vowel:
            cnt_vowel += 1
            cnt_consonant = 0
        else : 
            cnt_vowel = 0
            cnt_consonant += 1
        # 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
        if cnt_vowel + cnt_consonant == 3:
            answer = f"<{t}> is not acceptable."
            break
        # 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
        if tmp_s == i:
            if tmp_s == 'e' or tmp_s == 'o':
                pass
            else:
                answer = f"<{t}> is not acceptable."
                break
        tmp_s = i
    
    if answer :
        res.append(answer)
    else:
        res.append(f"<{t}> is acceptable.")

for i in res:
    print(i)