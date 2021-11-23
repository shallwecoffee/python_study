# # while 반복문
# while True:
#     print("무한반복")

# count = 0
# while count < 3:
#     print('횟수:', count)
#     count += 1

# name = ''
# while name != '펭수':
#     name = input('펭수를 입력해 주세요 : ')

#     print("thank you")

total = 0
for x in range(1, 10):
    total += x

    print("1에서 100까지 더한값: ", total)

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j}')

# 별나타내기
    n = 10
    i = 1
    while i <= n:
        print('*'*i)
        i += 1
