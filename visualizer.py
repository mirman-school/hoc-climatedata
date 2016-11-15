from matplotlib import pyplot as plt
from explorer import *

f = plt.figure()
plt.title("High temperatures 90049, 2010 - 2016")
x = [p.date for p in data]
y = [p.high for p in data]

plt.xlabel("Date")
plt.ylabel("High (Deg F)")
plt.plot(x,y)
plt.show(f)
