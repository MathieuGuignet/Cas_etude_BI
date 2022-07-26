import csv
import numpy as np
import pandas as pd
import math
from statistics import mean
from functools import reduce
from operator import itemgetter
import matplotlib.pyplot as plt
import datetime as dt

cities = pd.read_csv('cities.csv')
shapes = pd.read_csv('shapes.txt')
smmag_line_clusters = pd.read_csv('smmag_line_clusters.csv')
smmag_line_stops = pd.read_csv('smmag_line_stops.csv')
smmag_lines = pd.read_csv('smmag_lines.csv')
smmag_stop_occupancy = pd.read_csv('smmag_stop_occupancy.csv')

stop_times = pd.read_csv('stop_times.txt')
stops = pd.read_csv('stops.txt')
trips = pd.read_csv('trips.txt')

updown_per_cluster_and_mode = pd.read_csv('updown_per_cluster_and_mode.csv')
updown_per_cluster_and_semline = pd.read_csv('updown_per_cluster_and_semline.csv')
updown_per_cluster_inout = pd.read_csv('updown_per_cluster_inout.csv')

# print('Cities\n', cities.head(), '\n')
# print('Shape\n',shapes.head(),'\n')
# print('SMMAG line clusters\n',smmag_line_clusters.head(),'\n')
# print('SMMAG line stops\n', smmag_line_stops.head(),'\n')
# print('SMMAG line\n', smmag_lines.head(),'\n')
print('SMMAG stop occupancy\n', smmag_stop_occupancy.head(150),'\n')
print('info\n',smmag_stop_occupancy.info())
smmag_stop_occupancy['timeSlot']= pd.to_datetime(smmag_stop_occupancy['timeSlot'],format= '%H:%M').dt.strftime('%H:%M')
#tweets_df['Time'] = pd.to_datetime(tweets_df['Time'])
print('info timeSlot\n',smmag_stop_occupancy.info())

print('Stop times\n',stop_times,'\n')
print('Stops\n',stops,'\n')
print('Trips\n',trips,'\n')

print('Updown per cluster and mode\n',updown_per_cluster_and_mode,'\n')
print('Describe Updown per cluster and mode\n',updown_per_cluster_and_mode.describe(),'\n')
print('Updown per cluster and semline\n',updown_per_cluster_and_semline,'\n')
print('Describe Updown per cluster and semline\n',updown_per_cluster_and_semline.describe(),'\n')
print('Updown per cluster inout\n',updown_per_cluster_inout,'\n')
print('Describe Updown per cluster inout\n',updown_per_cluster_inout.describe(),'\n')


#plot occupancy as functio of time

fig1 = plt.figure()
plt.plot(smmag_stop_occupancy['timeSlot'],smmag_stop_occupancy['occupancy'])

# plt.show()
fig2=plt.figure()
#smmag_stop_occupancy.set_index('timeSlot', inplace=True)
smmag_stop_occupancy_group = smmag_stop_occupancy.groupby('routeDirection')['occupancy','timeSlot']
smmag_stop_occupancy.groupby('routeDirection')['occupancy','timeSlot'].plot(x='timeSlot', legend=True)
print(smmag_stop_occupancy_group.head())
plt.show()