'''
두 정수 사이의 합
문제 설명
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

제한 조건
a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
a와 b의 대소관계는 정해져있지 않습니다.
입출력 예
a	b	return
3	5	12
3	3	3
5	3	12
'''

def solution1(a, b):
    answer = 0
    if b > a:
        for i in range(a,b+1):
            answer += i
    elif a > b:
        for i in range(b,a+1):
            answer += i
    else:
        answer = a

    return answer


'''
문제 설명
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

제한 조건
n은 길이 10,000이하인 자연수입니다.
입출력 예
n	return
3	"수박수"
4	"수박수박"
'''

def solution2(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer = answer + '' + '수'
        else:
            answer = answer + '' + '박'

    return answer

'''
서울에서 김서방 찾기
문제 설명
String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

제한 사항
seoul은 길이 1 이상, 1000 이하인 배열입니다.
seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
"Kim"은 반드시 seoul 안에 포함되어 있습니다.
입출력 예
seoul	return
["Jane", "Kim"]	"김서방은 1에 있다"
'''

def solution3(seoul):
    k = 0    
    answer = ''
    for i in seoul:
        if i == 'Kim':
            break
        k += 1
        
    answer = ('김서방은 %d에 있다' % k)
        
    return answer


'''
약수의 합
문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.
입출력 예
n	return
12	28
5	6
입출력 예 설명
입출력 예 #1
12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.

입출력 예 #2
5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.
'''
def solution4(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
    return answer


'''
가운데 글자 가져오기

문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
입출력 예
s	return
"abcde"	"c"
"qwer"	"we"
'''

def solution5(s):
    a = len(s) // 2
    
    if len(s) % 2 == 0:
        middle_str = s[a-1] + s[a]
    
    else:
        middle_str = s[a]

    
    return middle_str




'''
x만큼 간격이 있는 n개의 숫자

문제 설명
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

제한 조건
x는 -10000000 이상, 10000000 이하인 정수입니다.
n은 1000 이하인 자연수입니다.
'''

def solution6(x, n):
    answer = []
    for i in range(n):
        a = x*(i+1)
        answer.append(a)
        
    return answer



'''
평균 구하기
문제 설명
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

제한사항
arr은 길이 1 이상, 100 이하인 배열입니다.
arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
입출력 예
arr	return
[1,2,3,4]	2.5
[5,5]	5
'''

# arr = [1,2,3,4]
def solution7(arr):
    # count=0
    # for i in arr:
    #     count += i
    # answer = count/len(arr)

    answer = sum(arr,0.0)/len(arr)

    print(answer)
    return answer

'''
행렬의 덧셈
문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
입출력 예
arr1	arr2	return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	[[3],[4]]	[[4],[6]]
'''
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
def solution8(arr1,arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        answer.append([x+y for x,y in (zip(i,j))])
    print(answer)    
    return answer

'''
짝수와 홀수
문제 설명
정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

제한 조건
num은 int 범위의 정수입니다.
0은 짝수입니다.
입출력 예
num	return
3	"Odd"
4	"Even"
'''

num = 4
def solution9(num):
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer



    
        


if __name__=="__main__":
    # solution1()
    # solution2()
    # solution3()
    # solution4()
    # solution5()
    # solution6()
    # solution7(arr)
    # solution8(arr1, arr2)
    solution9(num)

