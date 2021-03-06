import numpy as np 
import pandas as pd 
from matplotlib import style 
from math import sqrt 
import matplotlib.pyplot as plt 
from collections import Counter
from warnings import warn 
style.use('fivethirtyeight')


dataset = {'k' : [[3,4],[2,1],[4,5]], 'r':[[9,8],[8,6],[7,10]] }
new_feature = [5,6]


def knalgo(data, predict, k=3):
	if(len(data)>= k):
		warnings.warn('length of data should be less than k')
	distances = [] 

	for i in data:
		for j in data[i]:
			euc_dist = np.linalg.norm(np.array(j) - np.array(predict))
			distances.append([euc_dist, i])

	votes = [a[1] for a in sorted(distances)[:k]]
	vote_result = Counter(votes).most_common(1)[0][0]

	return vote_result

result = knalgo(dataset , new_feature , k=3)
print(result)


		

for i in dataset:
	for j in dataset[i]:
		plt.scatter(j[0],j[1],s=100,c=i)
plt.scatter(new_feature[0],new_feature[1],s=100)
plt.show()