# 문자열치환

number = "31415926"
dictionary = ["may","i","have","a","large","container","of","coffee"]
answer_list = []
answer = ""

def solution1(number,dictionary):
    # 알파벳순으로 정렬
    dictionary.sort()
    for i in list(number): # number리스트화해서 하나씩 추출
        i = int(i) 
        for j in dictionary: 
            if i == len(j): # number의 숫자와 값이 같을때 
                answer_list.append(j) # answer리스트에 추가하고
                dictionary.remove(j) # dictionary에서 제거
                break
    
    print(answer_list)
    answer = " ".join(answer_list) # 리스트 하나의 문자열로 합치기
    
    print(answer)
    return answer

# 앞뒤가 똑같은 문자열

s = "qwerty"
def solution2(s):
    plus_s = ""
    answer = "" 
    while s != "": # 길이가 0이 아니고 끝까지 돌리기 위해서설정
        revers_s = s[::-1] # 현재 문자열이 팰린드롬인지 확인하기위해 뒤집은 문자열 생성
        if s == revers_s:  #문자열이 팰린드롬이라면
            answer = plus_s + s + plus_s[::-1] # 제거한 문자열 + 팰린드롬이 맞는 문자열 + 제거한문자열 뒤집은것을 더해줌
            break
        else: 
            plus_s += s[0]  # 제거하려하는 앞글자 체크해 놓기
            s = s[1:] # 문자열s의 앞글자 하나씩 제거
    return(len(answer))


# 길걷기
X = 3
Y = 0
walkTime = 12
sneakTime = 10

def solution3(X, Y, walkTime, sneakTime):
    if sneakTime >= walkTime*2: # sneakTime이 정석대로 갈대보다 더오래걸리므로 사용할 이유가 없음
        answer = walkTime*X + walkTime*Y


    elif sneakTime >= walkTime: # sneakTime이 가로세로 거쳐서가는것보다는 빠르고 하나 움직일대보다는 같거나 느릴떄
        if X >= Y:
            answer = sneakTime*Y + walkTime*(X-Y)
        else:
            answer = sneakTime*X + walkTime*(Y-X)


    else: # sneakTime이 walkTime보다 빨라서 두칸이상 한방향으로 움직일때 지름길 두번이용하는게 더빠를때
        if X >= Y: # X방향이 길 경우
            if (X-Y) % 2 == 0:
                answer = sneakTime*Y + sneakTime*(X-Y)
            else: # X방향으로 한번만 이동이 필요할때는 지름길만 이용해서는 영원히 갈수 없으므로 walktime을 한번은 써야함
                answer = sneakTime*Y + sneakTime*((X-Y)//2) + walkTime
        else:  # 방향이 길 경우
            if (Y-X) % 2 == 0:
                answer = sneakTime*X + sneakTime*(Y-X)

            else: 
                answer = sneakTime*X + sneakTime*((Y-X)//2) + walkTime


    print(answer)
    return answer



if __name__=="__main__":
    # solution1(number, dictionary)
    # solution2(s)
    solution3(X, Y, walkTime, sneakTime)


