from re import X
import plotly.express as pe
import csv
import numpy as np

with open("AverageTvWatchingHours.csv") as f:
    data1 = csv.DictReader(f)
    graph1 = pe.scatter(data1,"Size of TV","Average time spent watching TV in a week",color = "Average time spent watching TV in a week" )
    graph1.show()


def Correlation_Coffee_Sleep(data1):
    Coffee = []
    Sleep = []

    with open(data1) as f:
        data2 = csv.DictReader(f)
        #graph2 = pe.scatter(data2,"sleep in hours","Coffee in ml",color = "Coffee in ml")
        #graph2.show()
        for x in data2:
            Coffee.append(float(x["Size of TV"]))
            Sleep.append(float(x["Average time spent watching TV in a week"]))
        
    return{"x":Coffee,"y":Sleep}

def Calculate_Correlation(data):
    Correlation = np.corrcoef(data["x"],data["y"])
    print("Correlation is equal to: " + str(Correlation[0,1]))

def Main():
    data = "./AverageTvWatchingHours.csv"
    data2 = Correlation_Coffee_Sleep(data)
    Calculate_Correlation(data2)

Main()




