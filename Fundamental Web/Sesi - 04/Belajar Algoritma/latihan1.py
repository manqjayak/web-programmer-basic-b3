nama = input("masukkan nama: ")
nilai = int(input("masukkan nilai: "))


if nilai >= 80 and nilai <= 100:
  result = "A"
elif nilai < 80 and nilai >= 70:
  result = "B"
elif nilai < 70 and nilai >= 60:
  result = "C"
else:
  result = "data tidak ada"
  
print("nama anda ", nama)
print("nilai anda ", nilai)
print("nilai mutu ", result)
