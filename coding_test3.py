
# candles = [2,2,2]
candles = [1,2,3,4,5,6,7,8]
# 리턴(정답): 3


# 하루 지날수 있을떄마다 count +=1해주고 count숫자가 남아있는 리스트내에 0이외에 숫자보다 많아야함
# 리스트에서 가장 높은양초먼저 태우면 좀더 오래 태울수있음




class Solution:
    def solution(self, candles):
        count = 1
        
        while len(candles) !=0:
            try:
                # candles내에 모든 0제거
                while True:
                    candles.remove(0)
            except:
                pass
            finally:
                candles.sort()


            print(candles)
            # i번째 날에 i개의 양초가 남아있지않다면 종료
            if count > len(candles):
                
                break

            # 길이가 긴 양초먼저 밝히기
            else:
                for i in range(count):
                    candles[-i-1] = candles[-i-1] -1

            count += 1

        print(count-1)
        return count-1






if __name__ == "__main__":
    Solution = Solution()
    Solution.solution(candles)
