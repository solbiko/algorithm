def solution(book_time):
    check = [0]*1440

    for times in book_time:
        sh, sm = map(int, times[0].split(':'))
        eh, em = map(int, times[1].split(':'))

        start = sh * 60 + sm
        end = eh * 60 + em + 10    # 청소시간 10분 포함

        if end > 1440:    # 24시를 넘어가는 경우 24시로 통일
            end = 1440

        for idx in range(start, end):    # 대실하는 시간에 체크
            check[idx] += 1

    return max(check)    # 방의 수가 가장 많이 대실하고 있을 때 값을 출력
