def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:(x*4)[:4], reverse=True)
    return ''.join(numbers) if numbers[0]!='0' else '0'