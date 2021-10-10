'''
문제 설명
스미드 교수는 논리 수업을 가르친다. 어느 날 그는 다음과 같은 문장을 칠판에 썼다.
이 문장들 중 정확히 a개의 문장이 참이다.
이 문장들 중 정확히 b개의 문장이 참이다.
이 문장들 중 정확히 c개의 문장이 참이다.
.
.
.
a, b, c 등은 각각 숫자이다. 그리고 그는 학생들에게 이 중 몇개의 문장이 참인지 물어보았다.

주어진 정수 배열 statements에 Smith 교수가 쓴 숫자들이 적혀있다. 모두 몇 개의 문장이 참인지 리턴하시오.
만약 가능한 답이 두개 이상이라면 그 중 더 큰 숫자를 반환하여라. 가능한 답이 없다면 -1을 리턴하시오.

참고 / 제약 사항
statements는 1개 이상, 50개 이하의 요소를 가지고 있다.
statements의 각 요소는 0 이상, 50 이하이다.
테스트 케이스
statements = [0,1,2,3]리턴(정답): 1
2번째 문장만이 참이고 (이 문장들 중 정확히 하나의 문장만이 참이다) 나머지는 다 거짓이다.

statements = [0]리턴(정답): -1
이 문제는 역설이다. 만약 문장이 참이라면 그것은 거짓을 주장하는 것이 되고, 거짓이라면 그것이 곧 참이 된다.

statements = [0,3,1,3,2,3]리턴(정답): 3
3번째 문장이 (1개의 문장이 참이다) 참이되는 경우와 2, 4, 6번째 문장이 (3개의 문장이 참이다) 참이 되는 경우 2가지가 있다. 더 큰 숫자를 반환하여야 하므로 답은 3이 된다.

statements = [1,1]리턴(정답): 0
statements = [1]리턴(정답): 1

'''

# statements에서 0은 무조건 틀리고 1은 1개,2는2개,3은3개...가 n은n개가 있을경우에 그문장이 참이된다
# 역설인 경우는 0개의 문장이 참입니다가 있는데 다른문장이 전부 거짓일경우 역설

statements = [0,3,1,3,2,3]
statements = [0,1,2,3]
statements = [0]
statements = [1,1]

def solution(statements):
    answer = 0
    statements.sort()

    while len(statements) !=0:
        count = 0
        last_num = statements[-1]

        if last_num !=0:
            try:
                while last_num == statements[-1]:
                    # 마지막 숫자에서 계속 같은경우 
                    statements.pop(-1)
                    count +=1
                    print(count)
            except:
                print("statements문장 처음부터 끝까지 검사함")

            print("처음숫자, 카운트", last_num, count)

            if count == last_num:
                answer = count  
                break

        # last_num == 0일경우
        else: 
            answer = -1
            break
            

    return answer 

if __name__ == "__main__": 
    print(solution(statements))