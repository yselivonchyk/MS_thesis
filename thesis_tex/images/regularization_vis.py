import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

figure_shape = [3095, 2352, 3]
plt.figure(num=0, figsize=[figure_shape[0]/300, figure_shape[1]/300], dpi=300)


# Local variables
x = [1,   1.1,   2,   3.6, 6., 7.4, 8.5]
y = [1.6, 1.6, 1.7, 3.1, 4., 3.7, 3.5]


x_sm = np.array(x)
y_sm = np.array(y)
x_smooth = np.linspace(x_sm.min(), x_sm.max(), 200)
y_smooth = spline(x, y, x_smooth)

x_dots, y_dots = x[2:-1], y[2:-1]

splt = plt.figure(num=0, figsize=[figure_shape[0]/300, figure_shape[1]/300], dpi=300).add_subplot(1, 1, 1, axisbg='w')

# noise
noisy_inp = np.asarray([[x_dots[0], y_dots[0]]])
for i, _ in enumerate(x_dots):
  noise = np.random.randn(30, 2) * 0.20 + np.asarray([x_dots[i], y_dots[i]])
  noisy_inp = np.concatenate((noisy_inp, noise), axis=0)

# curve
x3_pred = x_dots[1]*2-x_dots[0], y_dots[1]*2-y_dots[0]

#labels
for i, txt in enumerate(x_dots):
  splt.annotate('x%d' % (i+1), (x_dots[i]-0.12, y_dots[i]-0.4), fontweight='bold')
  # splt.annotate('x%d' % (i+1), (x_dots[i]-0.25, y_dots[i]+0.15), fontweight='bold')
  # splt.add_artist(plt.Circle((x_dots[i], y_dots[i]), 0.2, color='blue'))
splt.annotate('x3*=x2+(x2-x1)', (x3_pred[0]-1., x3_pred[1]+0.10), fontweight='bold', zorder=10)


splt.plot(x_smooth, y_smooth, '--', linewidth=1, c='k', label='trajectory')
splt.scatter(x_dots, y_dots, s=50, c='r', label='encodings', zorder=9)
splt.scatter(x3_pred[0], x3_pred[1], s=50, c='b', label='prediction')
splt.scatter(noisy_inp[:,0], noisy_inp[:,1], marker='o', lw=0.0, s=4, c='b', label='noisy encodings')


splt.tick_params(axis='x')
splt.tick_params(axis='y')

# Put the title and labels
splt.set_title('Prediction on manifold')
splt.set_xlabel('x')
splt.set_ylabel('y')
axes = plt.gca()
extra_space = 0.8
axes.set_xlim([min(x)-extra_space, max(x)+extra_space])
axes.set_ylim([min(y)-extra_space, max(y)+extra_space*1.3])
axes.get_xaxis().set_ticks([])
axes.get_yaxis().set_ticks([])

arr = splt.arrow(x_dots[0]+.04, y_dots[0]+.04, (x_dots[1]-x_dots[0])*0.9, (y_dots[1]-y_dots[0])*0.9,
                 fc="k", ec="k", linewidth=1, head_width=0.15, head_length=0.1, label='x2-x1')

splt.arrow(x_dots[1]+.04, y_dots[1]+.04, (x_dots[1]-x_dots[0])*0.9, (y_dots[1]-y_dots[0])*0.9,
           fc="k", ec="k", linewidth=1, head_width=0.15, head_length=0.1)

# plt.legend([arr,], ['My label',])
plt.legend(shadow=True, fancybox=True, loc='lower right')

# Show the plot/image
plt.tight_layout()
plt.grid(alpha=0.8)
plt.savefig("prediction.png", dpi=300, facecolor='w', edgecolor='w',
                transparent=False, bbox_inches='tight', pad_inches=0.1,
                frameon=None)
plt.show()