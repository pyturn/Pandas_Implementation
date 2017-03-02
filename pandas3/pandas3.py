import pandas as pd 

df = pd.read_csv('ZILL-Z77006_5B.csv')
print df.head()

df.set_index('Date',inplace = True)
df.to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv')
print df.head() #Again we notice that our index of Dataframe is lost.

df = pd.read_csv('newcsv2.csv', index_col = 0)
print df.head()

df.columns = ['Austin_HPI'] #We want to give name to the House Column.
print df.head()

df.to_csv('newcsv3.csv')
##What is we do not want header in file.
df.to_csv('newcsv4.csv', header = False)

df = pd.read_csv('newcsv4.csv',names = ['Date','Austin_HPI'],index_col =0) #To add the column names in our dataframe.
print df.head()

# To convert our pandas dataframe into HTML.
df.to_html('example.html')

df = pd.read_csv('newcsv4.csv',names = ['Date','Austin_HPI'])
print df.head()
#To rename a column.
df.rename(columns = {'Austin_HPI':'77006_HPI'}, inplace=True)

