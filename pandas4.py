import quandl 
import pandas as pd 

#df = quandl.get("FMAC/HPI_AK", authtoken="QRzNdTRsaksPZMEF-sW8")
#print df.head() #Notice that quandl module automatically assigns date as the index.

fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#print fifty_states

# this is a dataframe.
#print fifty_states[0]

#this is a column
#print fifty_states[0][0]

for abbv in fifty_states[0][0][1:]:
	print("FMAC/HPI_"+str(abbv))