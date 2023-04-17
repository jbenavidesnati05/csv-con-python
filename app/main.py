import read_csv
import charts
import matplotlib.pyplot as plt 
import csv

def run():
    data = read_csv.read_csv('./data.csv')
    
    countries = list(map(lambda x: x['Country'], data))
    porcentages = list(map(lambda x :['World Population Percentage'],data))
    charts.generate_pie_char(countries, porcentages) 