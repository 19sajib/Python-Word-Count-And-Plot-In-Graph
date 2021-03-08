def count(fname, words_list):
 if fname:
    try:
        file = open(str(fname), 'r')
        full_text = file.readlines()
        file.close()
        count_result = dict()
        for word in words_list:
            for text in full_text:
                if word in count_result:
                    count_result[word] = count_result[word] + text.count(word)
                else:
                    count_result[word] = text.count(word)
        return count_result
    except:
        print('Something really bad just happened!')

badWord = count('test.txt', ["rape","injury", "victim"])
goodWord = count('test.txt', ["champions","enormous", "development"])
print(badWord)
print(goodWord)
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("Bad Words")

#plot 2:
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "hotpink")

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("Good Words")

plt.suptitle("Word Accuracy")
plt.show()
