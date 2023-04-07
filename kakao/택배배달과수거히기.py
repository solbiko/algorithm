"""
트럭에 실을 수 있는 재활용 택배 상자의 최대 개수 cap,
배달할 집의 개수를 나타내는 정수 n,
각 집에 배달할 재활용 택배 상자의 개수를 담은 1차원 정수 배열 deliveries
각 집에서 수거할 빈 재활용 택배 상자의 개수를 담은 1차원 정수 배열 pickups

트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리
"""


def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    have_to_deli = 0
    have_to_pick = 0

    for i in range(n):
        print(i)
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]
        print(have_to_deli, have_to_pick)

        while have_to_deli > 0 or have_to_pick > 0:
            have_to_deli -= cap
            have_to_pick -= cap
            answer += (n - i) * 2

    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))

