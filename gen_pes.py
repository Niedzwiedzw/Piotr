# GenPes-number-generator
#Generator of personal identity numbers for one year and male sex.
from random import randint, choice
#generujący losowo numery pesel algorytm dla mężczyzny urodzonego w 1983 r.
def genpes():
  for t in range(span):
    a = 8
    b = 3 #jako warunek zadania przyjęto z góry konkretny rok
    c = randint(0, 1)
    if c == 0:
      d = randint(1, 9)
    elif c == 1:
      d = randint(0, 2) # dla tych miejsc generuję miesiąc
    mons1 = [1, 3, 5, 7, 8, 10, 12]
    mons2 = [4, 6, 9, 11]
    if c + d in mons1:
      D = randint(1,31)
    elif c + d in mons2:
      D = randint(1, 30)
    elif c + d == 2 and c != 1:
      D = randint(1, 28)
    if D < 10:
      day = '0' + str(D)
    elif D >= 10:
      day = str(D) # te linijki generują dni zależnie od wygenerowanego miesiąca
    e = randint(0, 9)
    f = randint(0, 9)
    g = randint(0, 9)
    h = choice([1, 3, 5, 7, 9]) #cyfry nieparzyste oznaczają pleć męską
    i = 8 + 9 + 7 * c + 9 * d + int(day[0])  + int(day[1]) * 3 + e * 7 + f * 9 + g + h * 3
    j = (10 - (i % 10))
    if j == 10:
      k = 0
    elif j != 10:
      k = j
    pesel = str(a) + str(b) + str(c) + str(d) + str(day) + str(e) + str(f) + str(g) + str(h) + str(k) #cyfra kontrolna 'k' jest wynikiem sumy zważonych cyfr poprzedzających podzielonej przez 10 i odjętej od 10; jeśli wynik jest równy 10, przyjmuje się 0
    rejestr.append(pesel) #dolączam pesel do przygotowanej listy
    yield 'nr pesel to: ' + pesel + ' || cyfrą kontrolną jest: ' + str(k)

rejestr = [] #przygotowanie listy
span = int(input('wprowadź liczbę generowanych losowo numerów:  '))
print('\n')
for t in genpes():
  print(t) #wyświetla kolejne iteracje
zbior = list(set(rejestr))
zbior.sort()
 #tworzy zbiór dla wykluczenia powtarzających się elementów i posortowaną listę, bo miala być lista :)
print('\nlista zbiorcza stringów dla numerów pesel:\n \n', '_rejestr =>', zbior, '\n-------------------\nDlugość listy: ', len(zbior)) #wyświetla listę zbiorczą i dlugość (sprawdzam, czy generator powtarza liczby; widoczna różnica przy np. 3000 generowanych numerów)
print('Różnica: ', span - len(zbior))#różnica między pożądaną liczbą iteracji a faktyczną liczbą numerów 
