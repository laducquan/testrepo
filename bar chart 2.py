# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:32:15 2021

@author: FPT
"""
from matplotlib import pyplot as plt
from collections import Counter
# A counter turrns a sequence off values into a dict, with values are keys and number of appearence as values

grades = [83, 75, 92, 71, 27, 36, 33, 83, 76, 77, 26, 99, 58, 88, 96]
decile = lambda grade : grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x for x in histogram.keys()], histogram.values(), 8)
#give each bar a width of 8, thus leaves a small gap 
#between each bar, since the buckets have width 10

plt.axis([-5, 105, 0, 5])   #x-axis from -5 to 105
                            #y-axis from 0 to 5
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of students")
plt.title("Distribution of Exam Grades")
plt.show()