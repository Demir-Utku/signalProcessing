# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:22:49 2019

@author: Utku Demir
"""
 
import pandas as pd 

##CREATING DATAFRAME
#ser = pd.Series([1,2,3,4],['a','b','c','d'])
#print(ser)
#
#ser['a'] = 'foo'
#print(ser)
#
#print(ser.index)
#x = ser.loc[['b','c']]
#y = ser.iloc[[1,2]]

#d  ={'bir' : pd.Series([10,20,30],index = ['elma','armut','erik']),
#     'iki' : pd.Series([111,222,333,444], index = ['kiraz','muz','kivi','portakal'])}
#df = pd.DataFrame(d)
#
#
#
#cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
#        'Price': [22000,25000,27000,35000]}
#df1 = pd.DataFrame(cars,columns= ['Brand', 'Price'])
#
#labels = ["Marka", "Fiyat"]
#df1.columns = labels
#
#
#price = "10000"
#Brand = ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4']
#data = {'price':price, 'city':Brand}
#df = pd.DataFrame(data)
#
###///////////////////////////////////////////////////////////////
##LOADING DATA
#election1 = pd.read_csv("election.csv")
#election1.head() 
#election1.tail()
#election1.shape
#election1.columns
##election1.info()
#election1.describe()
#election1['winner'].value_counts(dropna=False)
#election1['county'].value_counts(dropna=False)
#
###///////////////////////////////////////////////////////////////
###DATA READING
#population = pd.read_csv("population.csv")
#new_labels = ["Yıl","Kişi Sayısı"]
#population2 = pd.read_csv("population.csv", header=0, names=new_labels)
#
#
#df_messy = pd.read_csv("messy.csv", header=3, comment='#')
#                     
###///////////////////////////////////////////////////////////////
###COMBINING DATA
###CONCAT
#uber = pd.read_csv("uber.csv")
#
#april = uber.loc[0:98,:]
#may = uber.loc[99:197,:]
#june = uber.loc[198:297,:]
#
#row_concat = pd.concat([april,may,june])
#print(row_concat.shape)
#
#
##status_country = ebola_melt.iloc[:,5:7]
##column_concat = pd.concat([ebola_melt, status_country], axis=1)
#
###///////////////////////////////////////////////////////////////
##INDEXING
#election = pd.read_csv("election.csv", index_col='county')
#results = election[["winner","total","voters"]]
#print(results.head())
#
##SLICING ROWS
#p_counties = election.loc["Perry":"Potter"]
#p_counties_rev = election.loc["Potter":"Perry":-1]
#
##SLICING COLUMNS
#left_columns = election.loc[:, :'Obama']
#middle_columns = election.loc[:, 'Obama':'winner']
#
#
#rows = ['Philadelphia', 'Centre', 'Fulton']
#cols = ['winner', 'Obama', 'Romney']
#three_counties = election.loc[rows,cols]
#
##FILTERING
#high_turnout = election.turnout>70
#high_turnout_df = election.loc[high_turnout]
##
#import numpy as np
#too_close = election['margin'] < 1
#election.loc[too_close, 'winner'] = np.nan
#print(election.info())
#
#titanic = pd.read_csv("titanic.csv")
#nan = titanic[["age","cabin"]]
#print(nan.shape)
#print(nan.dropna(how="any").shape)
#print(nan.dropna(how="all").shape)
#print(titanic.dropna(thresh=1000, axis='columns').info())
#
#
##TRANSFORMING
##Using apply
#weather = pd.read_csv("weather2.csv")
#def to_celsius(F):
#    return 5/9*(F - 32)
#df_celsius = weather[['Mean TemperatureF','Mean Dew PointF']].apply(to_celsius)
#df_celsius.columns = ['Mean TemperatureC', 'Mean Dew PointC']
#print(df_celsius.head())
#
##Using map
#red_vs_blue = {'Obama':'blue','Romney':'red'}
#election['color'] = election["winner"].map(red_vs_blue)
#print(election.head())
##
##INDEX NAME
#sales = pd.read_csv("sales.csv")
#sales.index.name="MONTHS"
#sales.columns.name="PRODUCTS"
#print(sales)
##
##
#state = ["CA","NY","TX","NA","BR","CH"]
#months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN']
#sales.index = state
#print(sales)
##
#sorted = sales.sort_index()
#
###MERGING DATAFRAME
#cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
#        'Price': [22000,25000,27000,35000]}
#df1 = pd.DataFrame(cars,columns= ['Brand', 'Price'])
#
#
#cars2 = {'Marka': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
#        'Yıl': [1996,2005,2001,2019]}
#df2 = pd.DataFrame(cars2,columns= ['Marka', 'Yıl'])
#
#merge = pd.merge(left = df1, right = df2, left_on = "Brand", right_on = "Marka" )       