
1. menentukan nilai
  A = 80.100
  B = 70.79
  C = 60.69
  Jika nilai > 101 > data tidak ada
  Jika nilai < 59. -0 > data tidak ada

tugas :
  - dibuatkan sketsa
  - dibuatkan konsep (logic/kondisi)

sketsa :
1. masukan nama dengan tipa data string, data tidak boleh lebih dari 50 karakter
2. masukan nilai tidak boleh lebih dari 100, dan tidak boleh kurang dari 60, jika lebih dari 100 maka hasilnya "data tidak ada"
3. .....
4. nama anda "arif" 
   nilai anda 80
   huruf mutu A
5. logic : 

kode peserta :
nama peserta :

STORE "nama" WITH "komang"
STORE "nilai" WITH ANY VALUE 
STORE "result" WITHOUT ANY VALUE
IF "nilai" >= 80 AND "nilai" <=100:
  SET "result WITH "A"
ELSEIF "nilai" < 80 AND "nilai" >= 70:
  SET "result WITH "B"
ELSEIF "nilai" < 70 AND "nilai" >= 60:
  SET "result" WITH "C"
ELSE:
  SET "result" WITH "data tidak ada"

DISPLAY "nama anda" + "nama"
DISPLAY "nilai anda " + "nilai"
DISPLAY "huruf mutu " + "result"