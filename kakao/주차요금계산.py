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


def solution(fees, records):  # 1 ≤ records의 길이 ≤ 1,000
    import math
    answer = []  # 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return

    # 차번호, 시간순 정렬
    r = []
    for i in records:
        r.append(i.split(" "))
    r.sort(key=lambda x: (x[1], x[0]))
    print(r)

    # 사용시간 합계
    car = {}
    for i in range(len(r)):
        t, c, s = r[i]
        if s == "IN":
            if i == len(r) - 1:  # 출차 안한 경우
                minutes = calTime(t, "23:59")
            else:
                if c != r[i + 1][1]:  # 출차 안한 경우
                    minutes = calTime(t, "23:59")
                elif r[i + 1][2] == "OUT":  # 출차한경우
                    minutes = calTime(t, r[i + 1][0])

            if c not in car:
                car[c] = minutes
            else:
                car[c] += minutes

    print(car)
    for i in car:
        if car[i] <= fees[0]:  # 기본시간보다 적게 이용
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((car[i] - fees[0]) / fees[2]) * fees[3])

    return answer