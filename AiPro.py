file = open("test.txt", "r")
data = file.read().lower()
words = data.split()

print('Number of words in text file :', len(words))



badOccurrences = data.count("rape")
badOccurrences1 = data.count("injury")
badOccurrences2 = data.count("victim")
badOccurrences3 = data.count("flood")
badOccurrences4 = data.count("damaged")

badWords = badOccurrences + badOccurrences1 + badOccurrences2 + badOccurrences3 + badOccurrences4

goodOccurrences = data.count("profits")
goodOccurrences1 = data.count("champions")
goodOccurrences2 = data.count("development")
goodOccurrences3 = data.count("gaming")

goodWords = goodOccurrences + goodOccurrences1 + goodOccurrences2 + goodOccurrences3

print('Number of occurrences of the bad word :', badWords)
print('Number of occurrences of the good word :', goodWords)


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import math
figure(num=None, figsize=(16, 6))
font = {'family' : 'Times New Roman',
        'weight' : 'bold',
        'size'   : 15}

plt.rc('font', **font)

# Defining values for the bad words plot
x1 = ["Rape", "Injury", "Victim", "Flood", "Damaged"]
y1 = [badOccurrences, badOccurrences1, badOccurrences2, badOccurrences3, badOccurrences4]

# Defining values for the good words plot
x2 = ["Profits", "Champions", "Development", "Gaming"]
y2 = [goodOccurrences, goodOccurrences1, goodOccurrences2, goodOccurrences3]

# Drawing first subplot
plt.subplot(1, 2, 1)
plt.bar(x1,y1, color = 'red')
plt.xlabel('All The Bad Words')

# Drawing second subplot
plt.subplot(1, 2, 2)
plt.bar(x2,y2, color = 'green')
plt.xlabel('All The Good Words')

plt.show()