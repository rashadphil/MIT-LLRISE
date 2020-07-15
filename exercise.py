import numpy as np
import matplotlib.pyplot as plt

#1
num1 = np.arange(1, 11)
#2
num2 = np.arange(0, 1, 0.1)
#3
num3 = np.linspace(5, 10, 8)


#4
N = 0.1 #sample rate
t = np.arange(0, 2, N)
Fc = 1
x = np.sin(2*np.pi*Fc * t)
plt.plot(t, x)
plt.show()
plt.clf()

#5
plt.scatter(t, x, c='red')
plt.show()
plt.clf()

#6
N = 0.2 #sample rate
t = np.arange(0, 2, N)
Fc = 1
x = np.sin(2*np.pi*Fc * t)
plt.title('Sinusoidal Waves')
plt.xlabel("Time")
plt.ylabel('Amplitude')
plt.plot(t, x)
plt.show()
plt.clf()

#7
N = 0.2 #sample rate
t = np.arange(0, 2, N)
Fc = 1
x = np.cos(2*np.pi*Fc * t)
plt.scatter(t, x, c='blue', marker= "s")
plt.show()
plt.clf()
#Difference is cosine starts at 1, sine starts at 0

#8
N = 0.02 #sample rate
t = np.arange(8, 12, N)
Fc = 1/1.5
x0 = np.cos(2*np.pi*Fc * t)
x0 = np.sin(2*np.pi*Fc * t)
plt.title('Sinusoidal Waves')
plt.xlabel("Time")
plt.ylabel('Amplitude')
plt.plot(t, x)
plt.show()
plt.clf()



