"""Подвиг 4"""
# put your python code here
num1, num2 = input().split()

try:
    if (num1+num2).count('.') == 2:
        res = float(num1) + float(num2)
    else:
        res = int(float(num1)) + int(float(num2))
except:
    res = num1 + num2
finally:
    print(res)


