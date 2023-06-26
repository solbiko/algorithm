"""
오늘 날짜를 의미하는 문자열 today,
약관의 유효기간을 담은 1차원 문자열 배열 terms 1 ≤ terms의 길이 ≤ 20
수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies 1 ≤ privacies의 길이 ≤ 100
파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return
"""
def solution(today, terms, privacies):
    answer = []

    #오늘 날짜
    nyear = int(today[:4])
    nmonth = int(today[5:7])
    nday = int(today[8:])

    for i in range(len(terms)):
        for j in range(len(privacies)):

            if terms[i][0] == privacies[j][-1]:  # 약관종류

                # 개인정보 수집일자
                year = int(privacies[j][:4])
                month = int(privacies[j][5:7]) + int(terms[i][2:])
                day = int(privacies[j][8:10]) - 1

                # print(privacies[j], year, month, day)

                while month > 12:
                    month -= 12
                    year += 1

                if day <= 0:
                    day = 28
                    month -= 1
                    if month <= 0:
                        month = 12
                        year -= 1

                if nyear > year:
                    answer.append(j + 1)
                elif nyear == year:
                    if nmonth > month:
                        answer.append(j + 1)
                    elif nmonth == month:
                        if nday > day:
                            answer.append(j + 1)
    answer.sort()
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))