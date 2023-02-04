# BMI を計算する
BMI = 68 / 1.76**2
print(BMI)

# BMI から肥満度に分類する
if BMI > 25:
    CATEGORY = "Overweight"

elif BMI < 18.5:
    CATEGORY = "Underweight"

else:
    CATEGORY = "Normal"

print(CATEGORY)
