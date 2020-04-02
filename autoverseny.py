#csapat;versenyzo;eletkor;palya;korido;kor
#   0       1        2      3      4    5
#Versenylovak;Fürge Ferenc;29;Gran Prix Circuit;00:01:11;1

f = open('autoverseny.csv','r',encoding='utf-8-sig')
fejlec = f.readline()
lista = []
for i in f:
    lista.append(i.strip().split(';'))
    
f.close()

print(f'3. feladat: {len(lista)}')

for i in lista:
    if i[1] == 'Fürge Ferenc':
        if i[3] == 'Gran Prix Circuit':
            if i[5] == '3':
                ora = int(i[4][0:2])
                perc = int(i[4][3:5])
                mperc = int(i[4][6:])
                korido_s = ora * 3600 + perc * 60 + mperc
                print(f'4. feladat: {korido_s} másodperc')
                
print(f'5. feladat: ')
print(f'Kérem egy versenyező nevét:')
versenyzo = input()

mini = 9999999
flag = False
for i in lista:
    if i[1] == versenyzo:
        flag = True
        ora = int(i[4][0:2])
        perc = int(i[4][3:5])
        mperc = int(i[4][6:])
        korido_s = ora * 3600 + perc * 60 + mperc
        if korido_s < mini:
            mini = korido_s
            palya = i[3]
            ido = i[4]

if flag:    
    print(f'6. feladat: {palya}, {ido}')
else:
    print(f'Nincs ilyen versenyző az állomanyban')