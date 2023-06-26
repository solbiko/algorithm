"""
트럭에 실을 수 있는 재활용 택배 상자의 최대 개수 cap,
배달할 집의 개수를 나타내는 정수 n,
각 집에 배달할 재활용 택배 상자의 개수를 담은 1차원 정수 배열 deliveries
각 집에서 수거할 빈 재활용 택배 상자의 개수를 담은 1차원 정수 배열 pickups

트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리
"""


def solution(cap, n, deliveries, pickups):
    answer = 0

    # 먼곳부터 배달하기위해 뒤집기
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    print("cap", cap)
    print(deliveries, pickups)

    # 배달해야 하는 양
    have_to_deli = 0
    have_to_pick = 0

    for i in range(n):

        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]

        # 음수인 경우 : 직전 배달 거리에 포함되어 배달
        while have_to_deli > 0 or have_to_pick > 0:  # 배달 할 거 있으면 배달하고 거리 더함
            have_to_deli -= cap
            have_to_pick -= cap
            answer += (n-i) * 2

    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))

