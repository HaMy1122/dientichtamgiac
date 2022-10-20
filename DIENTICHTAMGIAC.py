import math

a = float(input ("nhap vao do dai canh 1: ")) #mac dinh la kieu du lieu string nen fai them int de thanh so nguyen hoac float thanh so thap phan' 
b = float(input ("nhap vao do dai canh 2: "))
c = float(input ("nhap vao do dai canh 3: "))

#ktra 3 canh co fai 3 canh cua tam giac ko
#xai try exeption (tu ngcuu them)
#begin
#input a,b,c
#if (a+b)>c and (b+c)>a and (a+c)>b then
#display "3 do dai vua nhap la 3 canh cua 1 tam giac"
#else
#display "3 do dai vua nhap ko fai la 3 canh cua 1 tam giac"
if (a+b)>c and (b+c)>a and (a+c)>b:
 print("3 do dai vua nhap la 3 canh cua 1 tam giac")
else:
 print("3 do dai vua nhap ko fai la 3 canh cua 1 tam giac")

#print
print ("do dai canh 1 la: " + str(a)) #xai str de ep thanh cung 1 kieu du lieu =str
print ("do dai canh 2 la: " + str(b))
print ("do dai canh 3 la: " + str(c))

#tinh s nua chu vi
s = (a+b+c)/2

#tinh dien tich tam giac theo cthuc heron
dien_tich = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("hien thi dien tich tam giac la: " + str(dien_tich))

