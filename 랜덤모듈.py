# 랜덤 모듈 불러오기
import random
import myModule as my

x = random.randint(0, 1)  # 0,1의 랜덤 숫자 생성

if x == 1:
    print("앞면")

else:
    print("뒷면")

print(my.pi)

# 점심값내기
names_string = input("내기를 할 친구들의 이름을 적습니다. 콤마(,)로 분리해서 적습니다.\n")
names = names_string.split(",")

# print(names)
# print(len(names))

n = random.randint(0, len(names))  # 랜덤 인덱스 숫자(사람수 만큼)
print(f"오늘의 커피는 {names[n]}가 쏜다")
