

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
