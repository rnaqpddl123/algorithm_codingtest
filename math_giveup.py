
from queue import Queue #queue쓰기위해서 선언

def solution(answers):
    check = []   # 각 순서대로 몇개씩 맞힌순서 저장용
    supoza1 = Queue()   # 속도를 위해서 list대신에 queue이용함
    supoza2 = Queue()   
    supoza3 = Queue()
    s1_count = 0    # 맞힌숫자 카운팅용도
    s2_count = 0
    s3_count = 0
    

    for i in range(len(answers)): #수포자1,2,3의 찍기패턴들
        if i % 5 == 0:
            supoza1.put(1) 
        elif i % 5 == 1:
            supoza1.put(2) 
        elif i % 5 == 2:
            supoza1.put(3) 
        elif i % 5 == 3:
            supoza1.put(4) 
        else:
            supoza1.put(5) 

    for i in range(len(answers)):
        if i % 8 == 0 or i % 8 == 2 or i % 8 == 4  or i % 8 == 6: 
            supoza2.put(2)
        elif i % 8 == 1:
            supoza2.put(1)
        elif i % 8 == 3:
            supoza2.put(3)
        elif i % 8 == 5:
            supoza2.put(4)
        else:
            supoza2.put(5)

    for i in range(len(answers)):
        if i % 10 == 0 or i % 10 == 1 :
            supoza3.put(3)
        elif i % 10 == 2 or i % 10 == 3:
            supoza3.put(1)
        elif i % 10 == 4 or i % 10 == 5:
            supoza3.put(2)
        elif i % 10 == 6 or i % 10 == 7:
            supoza3.put(4)
        elif i % 10 == 8 or i % 10 == 9:
            supoza3.put(5)


    for i in answers:   
        s1 = supoza1.get()  # 정답 1번부터 맞춰보기위해서 수포자들이 찍은 답 1번부터 뺴오기
        s2 = supoza2.get()
        s3 = supoza3.get()

        if s1 == i:         # 정답 맞춰보기 정답이 맞다면 s1_count로 맞힌숫자 올려줌
            s1_count += 1
        if s2 == i:
            s2_count += 1
        if s3 == i:
            s3_count += 1

    # print("수포자 1은 %d개만큼 문제를 풀었습니다" % (s1_count))
    # print("수포자 2은 %d개만큼 문제를 풀었습니다" % (s2_count))
    # print("수포자 3은 %d개만큼 문제를 풀었습니다" % (s3_count))

    check.append(s1_count) # check = []에다가 몇개씩 맞췄는지 입력해줌
    check.append(s2_count)
    check.append(s3_count)


    lucky_guy = 0     # 가장 많이 맞춘숫자 저장값
    lucky_guy_num = []  # 몇번 학생이 가장 많이 맞췄는지를 저장하는 리스트
    for i in range(len(check)):
        if check[i] > lucky_guy:
            lucky_guy_num = []   # 최고점자가 새로 나왔으니 앞에것은 필요없으니 초기화 
            lucky_guy = check[i]  # 가장많이 맞춘숫자 바꿔주기
            lucky_guy_num.append(i+1) # 최고점자의 몇번수포자인지 리스트에 저장

        elif check[i] == lucky_guy:   # 최고점자와 동점자가 나왔을경우
            lucky_guy_num.append(i+1) # 최고점자가 몇번수포자인지만 리스트에 추가
        

    return lucky_guy_num


# 확인용
answers = [1,2,3,4,5]	
print(solution(answers))

answers = [1,3,2,4,2]
print(solution(answers))
