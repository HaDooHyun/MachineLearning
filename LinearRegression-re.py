import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

# y = ax + b

a = 10
b = 1

# init learning_rate
learning_rate_a = 0.3
learning_rate_b = 0.007

# dataset
#x = []
#y = []
#for repeat in range(20):
#    data_x = np.random.uniform(0.3, 0.7)
#    data_y = np.random.uniform(0.3, 0.7)
#    x.append(data_x)
#    y.append(data_y)
x = np.arange(0, 1, 0.05)
y = np.arange(0, 1, 0.05)

#init hyperthesis
t = np.arange(0, 10, 1)

def f(x) :
    return a * x + b

def cost() :
    sum = 0
    for i in range(len(x)):
        sum += (a * x[i] + b - y[i])**2
    return sum / len(x)

def costA(a):
    sum = 0
    for i in range(len(x)):
        sum += (a*x[i] + b - y[i])**2
    return sum / len(x)

def costB(b):
    sum = 0
    for i in range(len(x)):
        sum += (a*x[i] + b - y[i])**2
    return sum / len(x)

def w(a) :
    sum = 0
    for repeat in range(len(x)):
        #sum += 2 * x[repeat]**2 * a + 2 * (b - y[repeat]) * x[repeat]
        sum += x[repeat]**2 * a - (x[repeat]*y[repeat])
    return sum / len(x)

def bias(b) :
    sum = 0
    for repeat in range(len(x)):
        sum += 2*a*x[repeat] + 2*b - 2*y[repeat]
    return sum / len(x)

frame = plt.figure()

graph1 = frame.add_subplot(331)
graph1.set_xlabel('x')
graph1.set_ylabel('y')
graph1.axis([0,1,0,1])
graph2 = frame.add_subplot(333)
graph2.set_xlabel('a')
graph2.set_ylabel('cost()')
graph3 = frame.add_subplot(337)
graph3.set_xlabel('b')
graph3.set_ylabel('cost()')
graph4 = frame.add_subplot(339)
graph4.set_xlabel('a')
graph4.set_ylabel('b')

#graph1.axis([0,1,0,1])
graph1.scatter(x, y, color='green')
line, = graph1.plot(t, f(t))

error = cost()

while error > 0.0005 :
    graph2.scatter(a, costA(a), 2)
    graph3.scatter(b, costB(b), 2)
    graph4.scatter(a, b, cost())
    a = a - (w(a) * learning_rate_a)
    b = b - (bias(b) * learning_rate_b)
    line.set_ydata(f(t))
    error = cost()
    
    print(error)
    plt.pause(0.05)
print("STOP ERROR VALUE : {0} < 0.0005".format(error))
plt.show()