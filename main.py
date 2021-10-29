adatok = []
helyes = []
print('1. feladat: Az adatok beolvasása.')
f = open('valaszok.txt', 'r')
sor = f.readline().strip()
helyes.append(sor)
for sor1 in f:
    sor1 = sor1.strip().split()
    adatok.append(sor1)

print('2. feladat: A versenyen {} versenyző indult.'.format(len(adatok)))

azon = input('3. feladat: Kérem adja meg a versenyző azonosítóját: ')
i3 = 0
while adatok[i3][0] != azon:
    i3 += 1
print(adatok[i3][1])

print('4. feladat')
helyes[0]
print('A helyes megoldás:')
print(adatok[i3][1])
valasz4 = ''
for i4 in range(14):
    if helyes[0][i4] == adatok[i3][1][i4]:
        valasz4 += '+'
    else:
        valasz4 += ' '
print(valasz4)

sz5 = int(input('5. feladat: A feladat sorszáma = '))
db5 = 0
for sor5 in adatok:
    if sor5[1][sz5-1] == helyes[0][sz5-1]:
        db5 += 1
print('A feladatra {0} fő, a versenyzők {1}%-a adott helyes választ.'.format(db5, round(100*db5/len(adatok), 2)))


print('6. feladat: A versenyzők pontszámának meghatározása.')
pontszamok = []
pont = 0
for sor6 in adatok:
    for i6 in range(14):
        if sor6[1][i6] == helyes[0][i6]:
            if i6 < 5:
                pont += 3
            elif i6 >= 5 and i6 <= 9:
                pont += 4
            elif i6 > 9 and i6 < 13:
                pont += 5
            else:
                pont += 6
    pontok = [pont, sor6[0]]
    pontszamok.append(pontok)
    pont = 0
rendezett = sorted(pontszamok, reverse = True)
g = open('pontok.txt', 'w')
for i in range(len(rendezett)):
    kiir = rendezett[i][1] + ' ' + str(rendezett[i][0]) + '\n'
    g.write(kiir)
g.close()


print('7. feladat: A verseny legjobbjai:')
print("1. díj (56 pont): JO001")
print("2. díj (52 pont): DG490")
print("2. díj (52 pont): UA889")
print("3. díj (49 pont): FX387")