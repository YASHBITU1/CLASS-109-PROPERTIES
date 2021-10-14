import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data) / len(data)
std = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

StdF1, StdE1 = mean-std, mean+std
StdF2, StdE2 = mean-(2*std), mean+(2*std)
StdF3, StdE3 = mean-(3*std), mean+(3*std)


list_of_std1 = [result for result in data if result > StdF1 and result < StdE1]
list_of_std2 = [result for result in data if result > StdF2 and result < StdE2]
list_of_std3 = [result for result in data if result > StdF3 and result < StdE3]
print("Mean  is {}".format(mean))
print("Median  is {}".format(median))
print("Mode is {}".format(mode))
print("Standard deviation is {}".format(std))
print("{}% of data in standard deviation".format(len(list_of_std1)*100.0/len(data)))
print("{}% of data in standard deviations".format(len(list_of_std2)*100.0/len(data)))
print("{}% of data in standard deviations".format(len(list_of_std3)*100.0/len(data)))