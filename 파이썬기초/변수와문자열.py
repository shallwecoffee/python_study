# # 여러개의 변수를 동시에 초기화
# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)


# # 문자열

# # 긴 문자열은 따옴표 3개(''',"""")
# var3 = '''
# '따옴표' 3개는
# 끝나는 "문장"까지
# 모두를 문자열로 처리
# ----------------------!
# '''

# print(type("문자열!"))
# var1 = '한따옴표'
# var2 = "쌍따옴표"
# print("문자열은"+var1+var2)

# 성 = '홍'
# 이름 = "길동"
# name = 성 + '' + 이름
# print(name)


# print(type(int(str(100))))

# a = str(100)
# b = int(a)
# c = type(b)
# print(c)

# str1 =    '\tIt\'s "kind of" sunny\n Have a nice Day!'
# print(str1)


# 밴드 이름 만들기 프로그램 환영합니다
print("밴드 이름 만들기 프로그램에 환영합니다.")

# 2 유저에게 태어난 도시를 물어봅니다.
city = input('태어난 도시가 어딘가요?\n')
# 3 유저에게 애완동물의 이름을 물어봅니다.
petName = input('애완동물의 이름은?\n')
# 4 도시와 애완동물 이름을 조합하여 밴드이름을 만들어 출력합니다
print('당신의 밴드이름은 '+city+' '+petName)
