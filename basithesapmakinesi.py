sayı1 = int(input("İlk Sayıyı Girin: "))
sayı2 = int(input("İkinci Sayıyı Girin: "))
islem = input("Hangi İşlemi Yapacaksın? (+, -, *, /): ")

if islem == "/" and sayı2 == 0:
    print("Sıfıra bölme hatası! Lütfen geçerli bir işlem seçin.")

elif islem == "+":
    print("Sonuç:", sayı1 + sayı2)

elif islem == "-":
    print("Sonuç:", sayı1 - sayı2)

elif islem == "*":
    print("Sonuç:", sayı1 * sayı2)

elif islem == "/":
    print("Sonuç:", sayı1 / sayı2)

else:
    print("Geçersiz İşlem")