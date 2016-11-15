from matplotlib import pyplot as plt
from explorer import *

def demo_graph():
    '''
    A Demonstration graph
    '''
    plt.title("High temperatures 90049, 2010 - 2016")
    x = [p.date for p in data]
    y = [p.high for p in data]

    plt.xlabel("Date")
    plt.ylabel("High (Deg F)")
    plt.plot(x,y)
    plt.show()

def print_data():
    '''
    A simple printout of all the data
    '''
    for d in data:
        print(d)

# Call your visualizer function here:
# print_data()
demo_graph()
