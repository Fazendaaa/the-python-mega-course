"""Uses bokeh for plotting"""
from bokeh.charts import Scatter, output_file, show
import pandas

DF = pandas.DataFrame(columns=['X', 'Y'])
DF['X'] = [1, 2, 3, 4, 5]
DF['Y'] = [5, 6, 4, 5, 3]

# pylint: disable=line-too-long
SC = Scatter(DF, x='X', y='Y', title='Temperature Observations', xlabel='Day of observations', ylabel='Temperature')
output_file('../output/Scatter_charts.html')
show(SC)
