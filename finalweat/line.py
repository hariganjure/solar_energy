import matplotlib.pyplot as plt
plt.plot([9,10,11,12,13,14], [10,15,20,30,40,45], 'ro')
plt.ylabel('Battery Percentage')
plt.xlabel('Time in Hours')

plt.axis([0,24 ,0, 50])
plt.show()