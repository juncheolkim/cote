now = list(map(int,input().split(':')))
now = now[0]*60*60 + now[1]*60 + now[2]
start = list(map(int,input().split(':')))
start = start[0]*60*60 + start[1]*60 + start[2]
answer = 0
# 하루가 지났는가?
if now < start:
    answer = start - now
else:
    answer = start + 24 * 60 * 60 - now

answer, sec = divmod(answer, 60)
sec = str(sec)
hour, min = map(str,divmod(answer, 60))
if len(hour) == 1:
    hour = "0"+hour
if len(min) == 1:
    min = "0" + min
if len(sec) == 1:
    sec = "0" + sec
print(":".join([hour, min, sec]))