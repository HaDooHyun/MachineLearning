import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

# y = ax + b

a = np.random.randint(10)
b = np.random.uniform(0, 1)

# init learning_rate
learning_rate_a = 0.08
learning_rate_b = 0.1

# dataset
x = []
y = []
for repeat in range(20):
    data_x = np.random.uniform(0.4, 0.6)
    data_y = np.random.uniform(0.4, 0.6)
    x.append(data_x)
    y.append(data_y)

#init hyperthesis
t = np.arange(0, 10, 1)

def f(x) :
    return a * x + b

def cost() :
    sum = 0
    for i in range(len(x)):
        sum += (f(x[i]) - y[i])**2
    return sum / len(x)

def w(a) :
    #sum = 0
    #for repeat in range(len(x)):
    #    sum += 2 * x[repeat]**2 * a + 2 * (b - y[repeat]) * x[repeat]
    #return sum / len(x)
    return 2 * x[repeat]**2 * a + 2 * (b - y[repeat]) * x[repeat]

def bias(b) :
    #sum = 0
    #for repeat in range(len(x)):
    #    sum += 2 * a * x[repeat] + 2 * b - 2 * y[repeat]
    #return sum / len(x)
    return 2 * a * x[repeat] + 2 * b - 2 * y[repeat]

frame = plt.figure()

graph1 = frame.add_subplot(321)
graph2 = frame.add_subplot(322)
graph3 = frame.add_subplot(325)
graph4 = frame.add_subplot(326)

graph1.axis([0,1,0,1])
graph1.scatter(x, y, color='green')
line, = graph1.plot(t, f(t))

error = cost()

while error > 0.02 :
    graph2.scatter(a, cost())
    graph3.scatter(b, cost())
    graph4.scatter(a, b, cost())
    a = a - (w(a) * learning_rate_a)
    b = b - (bias(b) * learning_rate_b)
    line.set_ydata(f(t))
    error = cost()
    
    print(error)
    plt.pause(0.05)

plt.show()