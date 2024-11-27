berat= int(input('MAsukan Berat Badan (Kg): '))
tinggi= float(input('Masukan Tinggi Badan (M): '))






print()

bmi= berat/(tinggi**2)
print(f'Berat Badan : {berat}')
print(f'Tinggi Badan : {tinggi}')
print(f'Nilai BMI Anda : {bmi}')

if bmi<18.5:
    print(f'Katagori BMI : Berat Badan Kurang' )
elif  (bmi>= 18.5 and bmi<24.9):
    print(f'Katagori BMI : Berat Badan Normal')
elif (bmi>= 25 and bmi <29.9):
    print(f'Katagori BMI : Kelebihan Berat Badan')
elif bmi>=30:
    print(f'Katagori BMI : Obesitas')
