'''
두개의 정수 a와 b에 대하여 a와 b 사이에 있는 모든 정수가 한번씩만 등장했을 때, 이를 정수가 연속한다고 말한다.

당신의 아들이 연속된 양의 정수를 임의의 순서대로 종이에 쓰고 있었다. 이 때, 각 숫자는 정확히 한번만 쓰여졌다. 그리고나서 그 중 하나의 숫자를 지웠다. 아들은 어느 숫자를 지웠는지 맞춰보라고 한다.

예를 들어, (10, 7, 12, 8, 11)이 종이에 남아 있었다면 지운 숫자는 9가 된다. 만약 남은 숫자가 (2, 3)이라면 지운 숫자는 1 혹은 4가 된다. 남은 숫자가 (3, 6)이라면 당신의 아들이 실수한 것이다.

종이에 남은 숫자는 numbers로 주어진다. 당신의 아들이 지웠을 가능성이 있는 모든 숫자를 정수 배열의 형태로 반환하여라. 숫자들은 높은 차순으로 정렬되어야하며 중복되는 숫자는 없어야 한다. 만약 아들이 실수를 했다면 아무것도 들어있지 않은 정수 배열을 반환하여라.
numbers = [10,7,12,8,11]
리턴(정답): [9]
'''
numbers = [10,7,12,8,11]
numbers = [3,6]
numbers = [5,6,7,8]
# numbers = [1000000000]
numbers = [1,6,9,3,8,12,7,4,11,5,10,10]
# numbers = [10,7,12,9,11]


def solution(numbers):
    numbers.sort()
    first_num = numbers[0]
    last_num = numbers[-1]
    while True :
        try:
            a = numbers.pop(-1)
            b = numbers[-1]
            if (a-1) != b:
                break
        except:
            break
    print(a)
    print(b)
    print(len(numbers))
    print(first_num, last_num)
    if len(numbers) == 0:
        if first_num == 1:
            return [last_num+1]
        elif last_num == 1000000000:
            return [first_num-1]
        else: 
            return [first_num-1, last_num+1]
    elif b == (a-2):
        return [a-1]
    else:
        return []

if __name__ == "__main__": 
    print(solution(numbers))
