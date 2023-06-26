def solution(users, emoticons):

    from itertools import product
    answer = [0, 0]

    # 모든 할인율 중복 조합
    combi = product((40, 30, 20, 10), repeat=len(emoticons))
    for discounts in combi:

        sold = [0, 0]  # 이모티콘, 판매액

        # 각 유저
        for user_discount, user_money in users:

            sold_emoticons = 0

            # 각 이모티콘과 할인율
            for emoticon, discount in zip(emoticons, discounts):

                # 사용자 할인율 기준보다 많이 할인하면 구매
                if discount >= user_discount:
                    sold_emoticons += emoticon * (1 - discount / 100)


            # 구매비용이 임티플러스 기준금액보다 크면 임티플러스 가입
            if sold_emoticons >= user_money:
                sold[0] += 1
            else: # 아니면 그냥 구매
                sold[1] += sold_emoticons

        # print(answer)
        answer = max(answer, sold)
    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000] ))