x=input("1.sayıyı giriniz:")
x=int(x)
y=input("2.sayıyı giriniz:")
y=int(y)
print("1 Sayısınız:",x)
print("2 Sayısı:",y)
print("Sayıların toplamı",x+y)
if(x-y>0):
  print("Sayıların farkı",x-y)
else:
    print("Sayıların farkı 0 dan küçük olucağından dolayı işleminiz gerçekleştiremmekteyim.")
print("Sayıların çarpımı",x*y)
if(x%y==0):
  print("Sayıların bölümü",x/y)
else:
    print("Sayıların bölümü kesirli olduğundan dolayı işleminiz gerçekleştiremmekteyim.")
print("Sayıların üslü",x^y)