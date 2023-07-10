def solution(numbers):
    answer = []
    
    for x in numbers:
        if x%2==0: # 짝수
            answer.append(x+1)    
        else: # 홀수
            b='0'+bin(x)[2:]
            # 가장 뒤쪽에 있는 0을 1로 바꿔주고 그다음 비트를 0으로 바꿔주면 된다
            b=b[:b.rindex('0')]+'10'+b[b.rindex('0')+2:]
            answer.append(int(b, 2))            

    return answer