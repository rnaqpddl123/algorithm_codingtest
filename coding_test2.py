
'''
방위각 구하기

문제 설명
로봇이 평면 위에서 다음과 같은 명령을 받아서 움직이고 있다.
LEFT – 왼쪽으로 90도 회전
RIGHT – 오른쪽으로 90도 회전
TURN AROUND – 반 바퀴 회전 (180도 회전)
LEFT X – 왼쪽으로 X도 회전 (X는 양의 정수)
RIGHT X – 오른쪽으로 X도 회전 (X는 양의 정수)
HALT – 명령어를 수행 중지, 앞으로 모든 명령을 수행하지 않는다

로봇의 명령어는 문자열의 배열 vector<string> instructions 로 주어진다. 명령을 전부 수행 한 다음에 로봇의 방위각을 구하시오.
(방위각은 북쪽을 기존으로 로봇이 바라보는 각도이며, 방위각은 시계방향으로 측정이 된다. 즉, 로봇이 서쪽을 바라보고 있다면 방위각은 270이 된다.)

참고 / 제약 사항
명령어는 총 1개 이상, 50개 이하다.
각 명령어는 위에 언급한대로 유효한 명령어다
LEFT X, RIGHT X에서 1 <= X <= 179
테스트 케이스
vector<string> instructions = ["RIGHT"]리턴(정답): 90
오른쪽으로 90도를 회전하면 방위각은 90이 된다.

vector<string> instructions = ["LEFT","LEFT","TURN AROUND"]리턴(정답): 0
왼쪽으로 90도 회전하면 로봇은 서쪽을 바라보게 된다 (방위각 270). 다시 왼쪽으로 90도 회전하면 로봇은 남쪽을 바라보게 된다 (방위각 180). 마지막으로 반 바퀴를 회전하면 로봇은 북쪽을 바라보게 된다 (방위각 0).

vector<string> instructions = ["LEFT 5","RIGHT 10","LEFT 15","RIGHT 20","LEFT 25","RIGHT 30","LEFT 35","RIGHT 40"]리턴(정답): 20
로봇은 왼쪽으로 5도 회전, 오른쪽으로 10도 회전 함으로써 결국 오른쪽으로 5도씩 4번 움직이게 된다.

vector<string> instructions = ["RIGHT 59","RIGHT","RIGHT","HALT","LEFT","LEFT","LEFT"]리턴(정답): 239
네 번째 명령은 HALT다. 즉 다음에 등장하는 LEFT 명령어들은 실행되지 않는다.

vector<string> instructions = ["TURN AROUND","HALT","LEFT 5","HALT","LEFT 5","HALT"]리턴(정답): 180
한번 이상의 HALT 명령이 주어질 수 있다.
'''



instructions = ["LEFT 5","RIGHT 10","LEFT 15","RIGHT 20","LEFT 25","RIGHT 30","LEFT 35","RIGHT 40"]

class Solution:
    def solution(self, instructions):
        answer = 0
        for i in instructions:
            if "RIGHT" in i:
                if i =="RIGHT":
                    answer += 90
                else:
                    answer += int(i[6:])

            elif "LEFT" in i:
                if i =="LEFT":
                    answer -= 90
                else:
                    answer -= int(i[5:])

            elif "TURN AROUND" == i:
                answer += 180

            elif "HALT" == i:
                break

            else:
                print("잘못된 명령어입니다")

        #  answer값이 0~360안에 자리잡게하기위한식
        while answer<0 or answer > 359:
            if answer <0:
                answer +=360
            else:
                answer -=360

        print(answer)

        return answer






if __name__ == "__main__":
    Solution = Solution()
    Solution.solution(instructions)
