"""Uses bokeh for plotting"""
from bokeh.plotting import figure, output_file, show
import pandas

# pylint: disable=line-too-long
DF = pandas.read_csv('http://ichart.yahoo.com/table.csv?s=AAPL&a=0&b=1&c=2000&d=0&e=1&f=2010', parse_dates=['Date'])
FG = figure(width=500, height=250, x_axis_type='datetime', responsive=True)
FG.line(DF['Date'], DF['Close'], color='Orange', alpha=0.5)

output_file('../output/line_plotting.html')
show(FG)
