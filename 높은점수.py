@ @ -0, 0 + 1, 13 @ @
# ๐จ ์ฌ๊ธฐ๋ ๊ทธ๋๋ก ๐
student_scores = input("ํ์๋ค์ ์ฑ์ ์ ์๋ ฅ :\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    # ์ฑ์  ์๋ ฅ์ ๋ฌธ์์ด๋ก ๋ฐ๊ธฐ ๋๋ฌธ์ ๋ค์ ์ ์๋ก ๋ณํํด์ ๋ฆฌ์คํธ์ ์๋ ฅ
print(student_scores)
# ๐จ ์ฌ๊ธฐ๋ ๊ทธ๋๋ก ๐

# ์๋์ ์ฝ๋ ์์ฑ ๐
highest_score = 0


print(f"๊ฐ์ฅ ๋์ ์ ์๋ : {highest_score}")
print(f"๊ฐ์ฅ ๋ฎ์ ์ ์๋ : {min(scores)}")
