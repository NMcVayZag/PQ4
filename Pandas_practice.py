import numpy as np
import pandas as pd

#series is a one-dimensional array of indexed data
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)
#series wraps both a sequence of values and a sequence of indicies, which we can access with the values and index attributes
print(data.values)
print(data.index) #gives index information on the container "data"
#slicing
print(data[1:3]) #gives second and thrid element

#integer definitiion
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                index = ['a','b','c','d'])
print(data)
print(data['d'])
#series as a specialized dictionary
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
print(population)
print(population['California'])

#unlike a dictionary though, a series can support slicing in this setting
print(population['Texas':'Florida'])

#CONSTRUCTING SERIES OBJECTS
print(pd.Series(5, index=[100, 200, 300]))
#dictionary notation
print(pd.Series({2:'a', 1:'b', 3:'c'}))
#we can specify which indexes we want to be printed/defined
print(pd.Series({2:'a', 1:'b', 3:'c'}, index=[3,2]))

#THE PANDAS DATAFRAME OBJECT
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
print(area)
states = pd.DataFrame({'population': population,
                       'area': area})
print(states)
print(states.index) #grab all indexes from dataframe
print(states.columns) #grab all collumns from dataframe
print(states['area']) #grab the area collumn with indexes from database

#create database with only the population figures
pop_db = pd.DataFrame(population, columns = ['Population'])
print(pop_db)