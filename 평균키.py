# π¨ μ¬κΈ°λ κ·Έλλ‘ π
student_heights = input("νμλ€μ ν€λ₯Ό μλ ₯νμΈμ\n").split()
# split() => κΈ°λ³Έκ³΅λ°±(μ€νμ΄μ€)λ‘ μλ ₯λ κ°μ λ¦¬μ€νΈλ‘ μ μ₯
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)
# π¨ μ¬κΈ°λ κ·Έλλ‘ π

# μλμ μ½λ μμ± π

total_height = 0
for height in student_heights:
    total_height += height
print(f"μ μ²΄ ν€μ ν© = {total_height}")
print(f"νμ μ = {len(total_heights)}")
print(f"νκ·  ν€ = {total_height}/len{total_heights}")
