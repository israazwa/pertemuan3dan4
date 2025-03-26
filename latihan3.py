def hitung_bmi():
    weight = float(input("Masukkan berat badan (kg): "))
    height = float(input("Masukkan tinggi badan (m): "))

    bmi = weight / (height * 2)

    if bmi < 18.5:
        kategori = "Underweight (Kurus)"
    elif 18.5 <= bmi < 25:
        kategori = "Normal"
    elif 25 <= bmi < 30:
        kategori = "Overweight (Kelebihan berat badan)"
    else:
        kategori = "Obese (Obesitas)"

    print(f"BMI Anda: {bmi:.2f} - {kategori}")

hitung_bmi()