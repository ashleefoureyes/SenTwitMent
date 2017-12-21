import csv
from bokeh.plotting import figure
from bokeh.io import show, output_file
import numpy as np

def collect_values(file_read):

    counter = 0
    values = []

    for row in file_read:
        if row[3] != None:
            values_float =float(row[3])
            values.append(values_float)
        counter += 1
    return (values)

valueTweets = csv.reader(open('csv_files/tentreetweets.csv', 'r'))

list_values = collect_values(valueTweets)



def y_value(list):

    rating_list = []
    for i in range (0, len(list)):
        if list[i] > 0:
            rating_list.append('Positive')
            i+=1
        elif list[i] == 0:
            rating_list.append('Neutral')
            i+=1
        elif list[i] < 0:
            rating_list.append('Negative')

    return rating_list

factors = y_value(list_values)


output_file("sentimentcount.html")



p = figure(plot_width=400,plot_height=400,title="Sentiment Scatter")
p.circle(list_values,list_values,size=15,fill_color="orange",line_color="green",line_width=3)

show(p)
