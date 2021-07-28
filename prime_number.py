'''
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
"17"	3
"011"	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.
출처
'''

from itertools import permutations

# 예시
number = "173"


def solution(number):  
    a = [] 
    x = [] # number 로 만들수있는 숫자 경우의수

    # 경우의수 구하기
    nums = list(number) #문자열 리스트화
    for i in range(2,len(nums)+1):
        k = set(list(permutations(nums, i)))
        a.append(k) #리스트화한것을 경우의수대로 묶어줌, set을넣어서 중복을 제거한상태로


    # a가 리스트안에 리스트안에 튜플형태라서 리스트로 바꿔주고 join이용해서 하나로합침
    for i in a:
        for j in i: 
            j = list(j)
            s = "".join(j)
            x.append(s) 
    

    # x+nums로 모든 경우의수 합치고 map으로 int형으로 바꾸고 set으로 중복제거
    x = list(set(map(int, x+nums))) 

    return prime_num(x)



# 소수판별
def prime_num(x):
    count=0
    for i in x:
        root_i = int(i**0.5)# 루트구하기

        for j in range(2,(root_i+2)): # 소수를 판별하기위해서 자신의 루트값+1까지만 나눠보면되서

            if i == 1 or i == 0: # 0과 1은 들어오면안되니까 
                break
            
            if i == 2: # i=2인 경우에 2%2=0이되서 카운트가 안된다. 그래서 카운트 할려고 하나 넣어줌
                count +=1

            if i % j == 0:
                break
            
            if j == root_i+1: # root_i+1까지 나눴는데 나눠떨어지는게 없으면 소수니까
                count +=1
    print(count)
    return count


if __name__=="__main__":
    solution(number)
