# 하노이의 탑
def solution(n):
    answer = []
    
    # 옮길 원반이 현재 있는 출발점 기둥 from_pos
    # 원반을 옮길 도착점 기둥 to_pos
    # 옮기는 과정에서 사용할 보조 기둥 aux_pos
    # 옮기려는 원반의 갯수 n
    def hanoi(from_pos, to_pos, aux_pos, n):
        if n == 1:  # 원반 한 개를 옮기는 문제면 그냥 옮기면 됨
            print(from_pos, "->", to_pos)
            answer.append([from_pos, to_pos])
            return

        # 원반 n - 1개를 aux_pos로 이동(to_pos를 보조 기둥으로)
        hanoi(from_pos, aux_pos, to_pos, n-1)
        
        # 가장 큰 원반을 목적지로 이동
        print(from_pos, "->", to_pos)
        answer.append([from_pos, to_pos])

        # aux_pos에 있는 원반 n-1개를 목적지로 이동(from_pos를 보조 기둥으로)
        hanoi(aux_pos, to_pos, from_pos, n-1)

    hanoi(1,3,2,n)
    
    return answer