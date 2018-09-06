import matplotlib.pyplot as plt
import numpy as np

# y = ax + b

a = np.random.randint(10)
b = np.random.uniform(0, 1)

# dataset
x = []
y = []
for repeat in range(10):
    data_x = np.random.uniform(0, 1)
    data_y = np.random.uniform(0, 1)
    x.append(data_x)
    y.append(data_y)

for real_y in y:
    print(real_y)

#def f(x) :
#    return a * x + b
#
#def cost(x) :
#    sum = 0
#    for real_y in y:
#        sum += (f(x) - real_y)**2
#    return sum / len(y)
#
#frame = plt.figure()
#
#graph1 = frame.add_subplot(321)
#grpha2 = frame.add_subplot(322)
#graph3 = frame.add_subplot(325)
#graph4 = frame.add_subplot(326)