from bisect import bisect_left, bisect_right

a = [0, 1, 2, 3, 4, 5, 8, 10]
x = 3
y = 7
print(bisect_left(a, x))  # 3
print(bisect_left(a, y))  #


# 시간계산 분단위 출력
def calTime(stime, etime):
    st, sm = map(int, stime.split(":"))
    et, em = map(int, etime.split(":"))
    mtemp = em - sm
    if mtemp < 0:
        et -= 1
        em += 60
        mtemp = em - sm
    ttemp = et - st
    minutes = ttemp * 60 + mtemp
    return minutes
