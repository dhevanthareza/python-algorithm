#function

def ratusan(Ratusan,Puluhan):
	puluh, satuan = divmod(Puluhan, 10)
	print(Ratusan + ' ' + kata[puluh] + ' ' + kata[satuan])
	
def angka(Angka):
    if 0 <= Angka <= 9:
       print(kata[Angka])
    elif 10 <= Angka <= 99:
       puluh, satuan = divmod(Angka, 10)
       print(kata[puluh] + ' ' + kata[satuan])
    elif 100 <= Angka < 1000:
    	puluhan, satuaja = divmod(Angka, 100)
    	i = kata[puluhan]
    	y = ratus[puluhan] * 100
    	z = Angka - y
    	ratusan(i,z)
    else:
        print("Angka terlalu besar")
    print("_____________")
    main()
        
def main():
    num = int(input("Masukan angka kurang dari 1000 =  "))
    if num >= 0 and num%2 == 0:
    	print('Bilangan Positif Genap')
    elif num >= 0 and num%2 != 0:
    	print('Bilangan Positif Ganjil')
    elif num < 0 and num%2 == 0:
    	print('Bilangan Negatif Genap')
    else :
    	print('Bilangan Negatif Ganjil')
    num1 = abs(num)
    angka(num1)
    

#list
kata = ['nol', 'satu','dua','tiga','empat','lima','enam','tujuh','delapan','sembilan']
ratus = [0,1,2,3,4,5,6,7,8,9]

main()
