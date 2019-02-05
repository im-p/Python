# Kuplalajittelu
# käyttää sisäistä silmukkaa
import random
import time
import string
from random import choices
from string import ascii_uppercase



def bubblesort(list):
    #käynnistää ajastimen
    start = time.time()
    
    #Käydään lista läpi
    for i in range (0, len(list)-1):
        
        
        #muuttujaan vaihto talletaan tieto, siitä onko vaihto tehty
        IsSorted = False
        
        #käydään lista läpi uudelleen, jotta voidaan tarkistaa tehdäänkö vaihtoja
        # len(list) - i - 1 estää algoritmia käymästä läpi jo järjestyksessä perällä olevia elementtejä
        for j in range(0, len(list) - i - 1):
            
            #katsotaan onko oikeilla puolella oleva elementti suurempi kuin vasemmalla oleva
            if list[j] > list [j+1]:
                
                #jos vasemmanpuoleinen elementti on suurempi kuin oikea, vaihdetaan niiden paikka
                #jatketaan niin piktaan kunnes viimeinen elementti i on on paikallan
                list[j], list[j+1] = list[j+1], list[j]
                IsSorted = True
               
                
        #jos kahta elementtia ei vaihdeta niin lopetataan
        if IsSorted == False:
            break
    #pysäyttää ajastimen
    stop = time.time()
    #tulostaa ajan
    print("Aikaa kului: ",stop-start)
    
    return list
    
#paras skenaario
def Best(x):
    list = [i for i in range(x)]
    return list
   
#huonoin skenaario
def Worst(x):
    reverse = Best(x)[::-1]
    return reverse
    
#satunnaislukuja/keskiarvo
def Average(a,b):
    randoms = random.sample(range(a),b)
    return randoms
    
#omaa lisää satunnaiset merkkijonot
def Strings(x):
    three_letter_words = ["".join(choices(ascii_uppercase, k=3)) for _ in range(x)]
    return three_letter_words

    
print("Worst case")
print(bubblesort(Worst(10)))
print("Average case")
print(bubblesort(Average(10,10)))
print("Best case")
print(bubblesort(Best(10)))
print("Strings")
print(bubblesort(Strings(10)))
