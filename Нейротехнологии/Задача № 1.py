from numpy import array
from numpy.fft import fft, irfft
import matplotlib.pyplot as plt

d = array(list(map(int, open("data_1.csv").read().split(',\n')[:-1])))
t = array(list(map(int, open("data_2.csv").read().split(',\n')[:-1])))

# график из точек которые нам предложили
plt.plot(d)
plt.show()                                                                            # 1

# ответ 1 вопрос 1-ой части
d1 = abs(array(fft(d)))[0:len(d)//2]
plt.plot(d1)
plt.show()                                                                            # 2

# Ответ на 2 вопрос 1-ой части
a = [0 for i in range(249)]
a.insert(8, d1[8])
d2 = irfft(a)
plt.plot(d2)
plt.show()                                                                            # 3

# Ответ на 3 вопрос 1-ой части
m = 0
u = 0
i = 0
while u < len(d)-10:
    ud = d[u:u+10]
    mu = max(ud)
    mm = min(ud)
    if mu-mm > m:
        m = mu-mm
        u += 5
        i = u+list(ud).index(mu)
    u += 5
print(m)

# подготовка к работе со 2-ой частью
t1 = abs(array(fft(t)))[0:len(t)//2]
t1[200] = 0
t1 = irfft(t1)
plt.plot(t1)
plt.show()                                                                           # 4

# график из точек которые нам предложили
plt.plot(t)
plt.show()                                                                           # 5

# ответ на 1 вопрос 2-ой части
a = [0 for i in range(249)]
a.insert(8, t1[100])
d2 = irfft(a)
plt.plot(d2)
plt.show()                                                                           # 6
