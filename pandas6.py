                             ## CONCATING AND APPENDING DATAFRAME ##
import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

#Data-FRame 1 and 3, they have the same index but different columns.
#Data-FRame 1 and 2, they have the same columns but different indexes.

#Concatenation- 
concat1 = pd.concat([df1,df2])
print concat1

concat2 = pd.concat([df1,df3])
print concat2

concat3 = pd.concat([df1,df2,df3])
print concat3

append1 = df1.append(df2)
print append1

append2 = df1.append(df3)
print append2
#appending and concating giving the same results.

#Now appending with series.
s = pd.Series([80,2,50])
df4 = df1.append(s, ignore_index = True)
print df4

# Now giving the name to the index also.
#Here we are observing that this is appending under that dataframe only because we are giving name same as that column.
s1 = pd.Series([80,2,50], index = ['HPI','Int_rate','US_GDP_Thousands'])
df5 = df1.append(s1, ignore_index = True)
print df5