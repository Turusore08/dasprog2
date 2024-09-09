# berat diganti variabel b
# tinggi diganti variabel t
#rating bmi variabel bmi

b=float(input("Masukkan berat anda(satuan pound)    :"))
t=float (input("Masukkan tinggi anda (satuan inch)  :"))

bmi = 703 * b / t**2


print("Skor anda adalah", bmi)

if (bmi < 18.5 ) :
    status = "Underweight" 
elif (bmi >= 18.5 and bmi <= 24.9):
    status = "Normal"
elif (bmi >= 25 and bmi <= 29.9):
    status = "Overweight"
else :
    status = "Obese"

print(f"Skor BMI anda adalah {bmi:,.2f} dan anda termasuk {status}")

