import numpy
import matplotlib.pyplot as pyplot

ra = [45, 40, 90, -75, 80.2, 102.63]            # angle  --> change to buffer_angle[4000]
ra = [x/180.0*3.141593 for x in ra]             # convert angle to radian

dec = [1.01, 6.05, 5.6, 4.02, 9.1, 7.85]        # distance --> change to buffer_distance[4000]

fig = pyplot.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
ax.set_ylim(0,10)
ax.set_yticks(numpy.arange(0, 10, 2))
ax.scatter(ra, dec, c='r')                      # plot the first microphone

#ax.scatter(rb, dec, c = 'b')                   # plot the second microphone
#ax.scatter(rh, dec, c = 'g')                   # plot the human voice



pyplot.show()