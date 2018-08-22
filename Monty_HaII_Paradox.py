print("Oto interaktywna wersja programu sprawdzającego Paradoks Monty'ego Halla \n Użytkownik sam okreśIa liczbę obrotów")
from random import *
statystyka = 0 #number of winnings in case of changes
statystyka_bez_zmian = 0 #number of winnings in case of no changes
obroty = 0 #number of contents
bramka =(1, 2, 3) #gates with probable reward
wybor_gracza = (1, 2, 3) #first choice of player
liczba = int(input("Wprowadź liczbę obrotów: "))#number of contents
while obroty < liczba:
  choice(bramka)
  choice(wybor_gracza)
  x = choice(bramka)
  y = choice(wybor_gracza)
  if x == y:
    statystyka += 0
    obroty +=1 
    statystyka_bez_zmian += 1
  elif x != y:
    statystyka += 1
    obroty += 1
    statystyka_bez_zmian += 0
print("obroty = ", obroty, "\nwygrane =", statystyka, "\nodsetek wygranych =", statystyka * 100/obroty, "%", "\nodsetek wygranych przy braku zmiany =", statystyka_bez_zmian * 100/obroty, "%")
print("Here we have frequency of winnings and losing in strategy thought of as the optimal - player still changes gate in case of choice")