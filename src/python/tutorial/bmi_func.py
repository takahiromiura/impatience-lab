# 身長・体重
A = {"height": 1.64, "weight": 82}
B = {"height": 1.83, "weight": 56}
C = {"height": 1.60, "weight": 60}


# BMI 計算
def calc_BMI(height, weight):
    return weight / height**2


# BMI
BMI_A = calc_BMI(A["height"], A["weight"])
BMI_B = calc_BMI(B["height"], B["weight"])
BMI_C = calc_BMI(C["height"], C["weight"])


# BMI から肥満度に分類する
def classify_BMI(bmi):
    if bmi > 25:
        return "Overweight"

    elif bmi < 18.5:
        return "Underweight"

    else:
        return "Normal"


# 結果出力
print(round(BMI_A, 2), classify_BMI(BMI_A))
print(round(BMI_B, 2), classify_BMI(BMI_B))
print(round(BMI_C, 2), classify_BMI(BMI_C))
