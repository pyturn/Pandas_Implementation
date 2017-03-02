import pandas as pd
#import datetime
#import pandas.io.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np 

web_stats = {'Day':[1,2,3,4,5,6],
			 'Visitors':[43,53,34,45,64,34],
			 'Bounce_Rate':[65,72,62,64,54,66]
			}
# Our python Dataframe is a form of representation of Dicyionary.
# Here we can use
df = pd.DataFrame(web_stats)

#print df
#print df.head(2) To print first two dataframes.
#print df.tail(2) To print last two sets of dataframe.

#We can change the index of dataframe also.
print df.set_index('Day')
print df.head()
#Here the return type of function is also a dataframe. So in order to make permanent changes we have to store it again in dataframe.

#df = df.set_index('Day')
#print df
# Now in order to avoid the problem which is occouring above we can modify df.set_index() like this. This will modify our original dataframe.
df.set_index('Day',inplace = True)
print df

# To refrence column in our dataframe.
print df['Bounce_Rate']
print df.Visitors
#and for slicing 
print df[['Visitors','Bounce_Rate']]

print df.Visitors.tolist() #Here from this statement of code we will get list.
#print df[['Bounce_Rate','Visitors']].tolist()# This statement will throw an error and that is because
                                             # we cant convert two columns to the list.
# So in order to converts slicing part as list we have to do something else.
print np.array(df[['Bounce_Rate','Visitors']])

#Now we can again convert the numpy array into a dataframe.
df2 = pd.DataFrame(np.array(df[['Bounce_Rate','Visitors']]))