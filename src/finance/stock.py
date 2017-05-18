"""Fetch and analize stock data from the internet"""
import datetime
from pandas_datareader import data
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN
from flask import Flask, render_template

def in_dec(c, o):
    if c > o:
        value = 'Increase'
    elif c < o:
        value = 'Decrease'
    else:
        value = 'Equal'
    
    return value

app = Flask( __name__ )

@app.route( '/' )
def plot():
    START = datetime.datetime(2016, 10, 1)
    END = datetime.datetime(2017, 1, 15)

    #   Do not use Yahoo as data source, the link is often broken
    DF = data.DataReader(name='GOOG', data_source='google', start=START, end=END)

    DF['Status'] = [in_dec(c, o) for c, o in zip(DF.Close, DF.Open)]
    DF['Middle'] = (DF.Open+DF.Close)/2
    DF['Height'] = abs(DF.Close-DF.Open)

    HOURS_12 = 12*60*60*1000

    FIG = figure(x_axis_type='datetime', width=1000, height=300, title='Candlestick Chart', responsive=True)
    FIG.grid.grid_line_alpha=0.3

    FIG.segment(DF.index, DF.High, DF.index, DF.Low, color='Black')

    FIG.rect(DF.index['Increase' == DF.Status], DF.Middle['Increase' == DF.Status],
            HOURS_12, DF.Height['Increase' == DF.Status], fill_color='#1A237E', line_color='black')
    FIG.rect(DF.index['Decrease' == DF.Status], DF.Middle['Decrease' == DF.Status],
            HOURS_12, DF.Height['Decrease' == DF.Status], fill_color='#00BCD4', line_color='black')

    #output_file('../output/stocks.html')
    #show(FIG)

    SCRIPT_1, DIV_1 = components(FIG)
    CDN_JS = CDN.js_files[0]
    CDN_CSS = CDN.css_files[0]

    return render_template('plot.html', SCRIPT_1=SCRIPT_1, DIV_1=DIV_1, CDN_CSS=CDN_CSS, CDN_JS=CDN_JS)

if '__main__' == __name__:
    app.run(debug = True)
