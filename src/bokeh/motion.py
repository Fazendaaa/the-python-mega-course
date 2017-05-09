"""Using bokeh for plotting data from camera motion detector"""
# pylint: disable=multiple-imports
import sys, os
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
# pylint: disable=import-error
sys.path.append(os.path.abspath('../openCV'))
# pylint: disable=wrong-import-position
from motion_detector import DF

DF['Start_string'] = DF['Start'].dt.strftime('%Y-%m-%d %H:%M:%S')
DF['End_string'] = DF['End'].dt.strftime('%Y-%m-%d %H:%M:%S')

CDS = ColumnDataSource(DF)

FIG = figure(x_axis_type='datetime', height=100, width=500, responsive=True, title='Motion Graph')
FIG.yaxis.minor_tick_line_color = None
FIG.ygrid[0].ticker.desired_num_ticks = 1

HOVER = HoverTool(tooltips=[('Start: ', '@Start_string'), ('End: ', '@End_string')])
FIG.add_tools(HOVER)

QUA = FIG.quad(left='Start', right='End', bottom=0, top=1, color='green', source=CDS)

output_file('../output/graph.html')
show(FIG)
