import random
import numpy as np
import matplotlib.pyplot as plt
import statistics
''' 
    https://towardsdatascience.com/law-of-large-numbers-in-finance-using-python-86945eaee444

    Law of large numbers 

    Xn -> E(x) when n -> infinity

    Xn er gennemsnit af eksemplevis højden på n personer
    
'''

'''
    
    Eksemple med brug af Law of Large numbers
    
    10 mønt kast forventer man 50/50 plat og krone
    
    10: kast resultat 7/3 = 70% / 30% hvilket afviger fra forvented
    
    100: kast blev resultat 52/48 52% / 48% tættere på det forventede
    
    1000: kast 502 / 498 -> 50.2% / 49.8%
    
    when the sample sice increase we get closer to the expected result
    
'''

'''

    Home work test the Law Of Large Numbers for N random normally distribute numbers with 
    mean = 0:
    stdev = 1:
        
    Create a python script tat will count how many of these numbers fall between -1 and 1 
    and divide by the total quantity of N
    
    You know that E(x) = 68.2%
    
    Check that mean(Xn) -> E(x) as you rerun your script while increasing N

'''
n_numbers=1000
probhead=[]
flip=[]

head=0
tail=0

for n in range(n_numbers):
    if random.randint(0,1)==0:
        head+=1
    else:
        tail+=1
    h=head/(head+tail)
    probhead.append(h)
    flip.append(n)

print(statistics.mean(probhead)) # mean
print(statistics.stdev(probhead)) #standard deviation

plt.subplot(2,1,1)
plt.hist(probhead,100,label='Probality of Heads')
plt.legend()
plt.xlim(-1,1)

plt.subplot(2,1,2)
plt.plot(flip,probhead)
plt.xlabel('Number of Flips')
plt.ylabel('Probability of Heads')
plt.grid(True)
plt.ylim(0,1)
plt.show()