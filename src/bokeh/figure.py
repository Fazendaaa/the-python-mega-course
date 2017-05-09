"""Uses bokeh for plotting"""
from bokeh.plotting import figure, output_file, show

FG = figure(plot_width=500, plot_height=400, title='Earthquake')

FG.circle([1, 2, 3, 4, 5], [5, 6, 5, 5, 3], size=[2, 12, 34, 25, 20], color='red', alpha=0.5)
output_file('../output/figure_plotting.html')
show(FG)
