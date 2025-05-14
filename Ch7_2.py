'''
Ch7, Part 2
Matplotlib
    - Matplotlib is a Python library for creating static, animated, and interactive visualizations, commonly used for plotting graphs like line charts, bar graphs, and histograms.


EASY TRICK  
    - if you want to make a scatter plot, just write .scatter, for boxplot write .boxplot ... etc
    - in other words, whatever you want to make, just write plt.(whatever you want to make) and then add the data likewise
    - not applicable to all, but applicable to most


Marker
    - a symbol used to represent data points on a plot, like dots or circles, and can be customized in terms of shape, size, and color.
'''

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()
'''
Line
    - A line in Matplotlib connects data points in a plot, typically used in line charts to show trends over a continuous range of values.
'''
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted', color='r')
plt.show() 


'''
Labels
    - labels the line/graph
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show() 


'''
Grid Lines
    - adds maths copy type lines
    - makes it look like a graph paper
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show() 


'''
Scatter plot
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()

'''
Bar graphs
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show() 


'''
Histograms
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()  


'''
Pie Charts
'''
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()  


'''
Finished!!!
'''