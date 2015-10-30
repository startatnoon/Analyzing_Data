import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import scipy.stats as stats
import collections

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(x)
count_sum = sum(c.values())

for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)


plt.boxplot(x)
plt.title("Boxplot")
plt.savefig("boxplot.png")
plt.show()


plt.hist(x, histtype='bar')
plt.title("Histogram")
plt.savefig("historam.png")
plt.show()

plt.figure(1)
test_data = np.random.normal(size=1000)   
graph1 = stats.probplot(x, dist="norm", plot=plt)
plt.title("QQ Plot")
plt.savefig("qqplot.png")
plt.show() #this will generate the first graph

plt.figure(2)
test_data2 = np.random.uniform(size=1000)   
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show() #this will generate the second graph