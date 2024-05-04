# 심부름 가는 길

homeToSchool = int(input())
schoolToPc = int(input())
PcToacademy = int(input())
acaToHome = int(input())

timee = homeToSchool + schoolToPc + PcToacademy + acaToHome

print(timee // 60)
print(timee % 60 )