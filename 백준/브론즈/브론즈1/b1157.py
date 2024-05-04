# 단어 공부

word = input().upper()
words = list(set(word))
cal = []

for i in words:
    cal.append(word.count(i))
    

if cal.count(max(cal)) > 1 :
    print('?')
else : 
    maxWord = cal.index(max(cal))
    print(words[maxWord])