# # # f - string
# # name = '홍길동' 변수명 바로 입력
# # age = 20
# # print(f'안녕하세요 {name}님 나이가 {age}살 이군요')

# # # 2. 문자열.format()
# # number = 20
# # welcome = '환영합니다'
# # base = '{} 번 손님 {}'

# # print('{}번 손님 {}'.format(number, welcome)) 안은 빈칸임. 차례대로 찾아가기 떄문에.

# # 예제

# name = '서상규'
# color = '검정색'
# print('안녕하세요. 제 이름은 {}이고 좋아하는 색상은 {}입니다.'.format(name, color))
# print(f'안녕하세요. 제 이름은 {name}이고 좋아하는 색상은 {color} 입니다.')

# # 문자열 인덱스 : 문자열은 인덱스 번호를 사용가능
# string1 = "abcdefg"
# print(string1[2])  # c
# print(string1[1:5])  # bcde
# # 슬라이싱[시작인덱스 : 끝 인덱스 ], [::증감]
# print(string1[::-1])  # gfedcba

# # 인덱스 번호로 값을 가져오는것은 가능하지만 수정불가

# string1[0] = 'k'

# 코딩예제

# num = ""
# two_digit_number = input("두 자리 숫자를 입력: 'a','b' \n")

###

height = input("키를 미터 단위로 입력하세요:")
weight = input("몸무게를 킬로 단위로 입력하세요:")

BMI = float(weight) / float(height)**2
print(f'당신의 bmi는 {round(BMI, 2)} 입니다.')
