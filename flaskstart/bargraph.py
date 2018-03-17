#!C:\Users\Aai\AppData\Local\Continuum\Anaconda3\python.exe

import matplotlib.pyplot as plt;
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('1-feb', '2-feb', '3-feb', '4-feb', '5-feb', '6-feb')
y_pos = np.arange(len(objects))
performance = [1.2, 1.0, 1.2, 1.1, 1.3, 1.0]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('solar energy generation')
plt.title('energy ')

plt.show()