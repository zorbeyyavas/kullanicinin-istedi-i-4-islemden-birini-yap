#klavyeden girilen 2 sayıyı kullanıcının istediği 4 işlemden birine sokan programı yap
sayi=int(input("1.sayıyı giriniz"))
sayi2=int(input("2.sayıyı giriniz"))
print("(1) toplama")
print("(2) çıkartma")
print("(3) bölme")
print("(4) çarpma")
islem=int(input("yapmak istediğiniz işlemi seçiniz"))
if (islem==1):
    print(sayi+sayi2)
elif(islem==2):
    print(sayi-sayi2)
elif(islem==3):
    print(sayi/sayi2)
elif(islem==4):
    print(sayi*sayi2)