
'''
암호추적

문제 설명
당신에게 적군의 코드를 해석하라는 비밀 미션이 주어졌다. 당신은 그들이 메세지를 다음과 같은 방법으로 암호화한다는 것을 이미 알아냈다. 'a'와 'z'사이의 알파벳을 두자리수 01과 26 사이의 숫자에 할당한다. 메세지는 각 알파벳을 할당된 숫자로 변환하여 암호화된다. 예를 들어, 't'는 20에 할당되고, 'e'는 05에 할당되고, 's'는 19에 할당되어 "test"는 "20051920"으로 암호화된다. 모든 원본 메세지는 소문자만으로 구성되어 있다.

주어진 string code에는 숫자와 문자의 할당이 나타나 있다. 첫번째 문자는 01에 할당되고, 두번째 문자는 02에 할당되는 식으로 26까지 이어진다. 또한 주어진 string message에는 암호화되지 않은 원본 메세지 혹은 암호화된 메시지가 있다. 만약 원본 메세지가 주어졌다면 메세지를 암호화하여 반환하고, 암호화된 메세지가 주어졌다면 원본 메세지를 반환하라.

참고 / 제약 사항
code는 정확히 26개의 문자를 가진다.
'a'에서부터 'z'까지의 소문자는 code에 정확히 한번만 나타난다.
message는 최소 1개, 최대 50개의 문자를 가진다.
message는 오직 소문자만을 가지거나 ('a'-'z') 혹은 오직 숫자만을 가진다 ('0'-'9').
만약 message가 오직 숫자만으로 구성되어있다면, 이는 01부터 26까지의 두자리 숫자의 연속적인 결합이다.
테스트 케이스
string code = "abcdefghijklmnopqrstuvwxyz"
string message = "test"리턴(정답): "20051920"
문제 내용에 언급된 예제이다. 문자는 알파벳 순서대로 암호화된다.

string code = "abcdefghijklmnopqrstuvwxyz"
string message = "20051920"리턴(정답): "test"
상기 예제의 암호 해석이다.

'''
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
