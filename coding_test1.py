
code = "abcdefghijklmnopqrstuvwxyz"
message = "20051920"    
# 메세지가 영어면 숫자로 리턴을 숫자면 영어로 리턴을줘라 

class Solution:
    def solution1(self, code, message):
        answer = ""
        # message가 문자인지 숫자인지 먼저 구분을 해줌
        if (message.isdigit()):
            # 2개단위로 자른뒤에 해당 숫자code에 대입해서 answer에 더해줌
            for i in range(int(len(message)/2)):
                k = int(message[i*2:i*2+2])
                answer += code[k-1]
                
            print(answer)
        else: 
            # 메세지의 문자가 몇번째 문자인지 알아내고 1자리수는 0을 붙인뒤에 정답에 더해줌
            for i in message:
                count = 0
                for j in code:
                    count = count +1
                    if i == j:
                        if count < 10:
                            answer = answer + "0" + str(count)
                        else : 
                            answer = answer + str(count)
            print(answer)

        return answer




if __name__ == "__main__":
    Solution = Solution()
    # Solution.solution1(code, message)
