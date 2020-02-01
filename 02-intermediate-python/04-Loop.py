
### Basic while loop ###
# Initialize offset
offset=8

# Code the while loop
while offset!=0:
    print("correcting...")
    offset-=1
    print(offset)


### Add conditionals ###
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset-=1
    else : 
      offset+=1    
    print(offset)
    
    
### Loop over a list ###
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for i in areas:
 print(i)
 
 
### Indexes and values (1) ###
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index,a in enumerate(areas) :
    print("room {}: {}".format(index,a))
    
  
### Indexes and values (2) ###
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))
    
    
### Loop over list of lists ###
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for x, y in house:
 print("the {} is {} sqm".format(x,y))
 
 
### Loop over dictionary ###
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items():
    print("the capital of {} is {}".format(key, value))
    
    
### Loop over Numpy Array ###
# Import numpy as np
import numpy as np

# For loop over np_height
for x in np_height:
    print("{} inches".format(x))

# For loop over np_baseball
for i in np.nditer(np_baseball):
    print(i)
    
    
### Loop over DataFrame (1) ###
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)
    
    
### Loop over DataFrame (2) ###
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print("{}: {}".format(lab,row['cars_per_cap']))
    
    
### Add column (1) ###
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"]=row["country"].upper()

# Print cars
print(cars)


### Add column(2) ###
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)
