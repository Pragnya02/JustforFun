from urllib import urlopen
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse
import pandas as pd
from pandas import *
from collections import Counter
import csv
import matplotlib.pyplot as plt
import os
#listdir- lists all available files in the directory
#week=[]
#satur=[]
#holi=[]
column_name=[]
df_name=[]
location='C:\Users\pragn_000\Desktop\Masters\Python\Pandas_Project\MBTA_CapeCod'
def conversion():	#main funct
	filename=[]
	filedir=[]
	# Taking a list of files from the directory
	filelist=os.listdir('C:\Users\pragn_000\Desktop\Masters\Python\Pandas_Project\MBTA_CapeCod')
	
	#stores the filename and filedirectory location for each file
	for i in range(0,len(filelist)):
		if '.txt' in filelist[i]:	#does it only for the .txt file
			filename.append((str((filelist[i]).rstrip('.txt'))+'.'+'csv'))
			filedir.append((location+'/'+filelist[i]))

	#print filename
	#print filedir
	
	#Converting text to DF, then converting it to CSV
	for i in range(0,len(filename)):
		df_text=pd.read_csv(filedir[i])
		convert_csv(df_text,filename[i])
		#df_text.to_csv(os.path.join(location,filename[i]),index=0)

	print "To CSV conversion Done"
	group_data(filename,filedir)

def group_data(filename,filedir):
	print "Hey"
	df=[]
	fd=[]
	item=[]
	for i in range(0,len(filename)):
		df.append((pd.read_csv(filedir[i])))
		fd=[]
	#print df
		#print " "
	for i in range(len(filename)):
		if 'trip_id' in  df[i]:		#Checksif there is any column called 'trip_id' and returns all the dataframe with that id
			fd.append(df[i])	#Gives the result for each df that contains the column 'trip_id' 

	#print fd[0]		
	#print fd[1]
	
	joined = pd.merge(fd[0],fd[1],on='trip_id', how='inner',right_index=True)
	joined = pd.merge(joined,fd[2],on='trip_id', how='inner',right_index=True)
	joined.to_csv(os.path.join(location,'joined.csv'),index=None)
	join_df=pd.read_csv(r'C:\Users\pragn_000\Desktop\Masters\Python\Pandas_Project\MBTA_CapeCod/joined.csv')

#Print the items that match with service_id==weekday; saturday and holiday separately
	column_name = list(join_df.columns.values)
	for grp in join_df['service_id'].unique():
		if grp=='Summer_Sun-Thu':
			df_SumST=pd.DataFrame((join_df[join_df['service_id'] == grp]),columns=column_name)
			df_name.append(grp+'.csv')
		elif grp=='Summer_Fri-Sat':
			df_SumFS=pd.DataFrame((join_df[join_df['service_id'] == grp]),columns=column_name)
			df_name.append(grp+'.csv')
		elif grp=='Summer_Hyannis':
			df_SH=pd.DataFrame((join_df[join_df['service_id'] == grp]),columns=column_name)
			df_name.append(grp+'.csv')
		elif grp=='Summer_Ptown':
			df_SP=pd.DataFrame((join_df[join_df['service_id'] == grp]),columns=column_name)
			df_name.append(grp+'.csv')
		elif grp=='Summer_Bike':
			df_SB=pd.DataFrame((join_df[join_df['service_id'] == grp]),columns=column_name)
			df_name.append(grp+'.csv')			
		elif grp=='SprShoulder_Fri-Sat':
			df_SprFS=pd.DataFrame((join_df[join_df['service_id'] == grp]),columns=column_name)
			df_name.append(grp+'.csv')			
		elif grp=='SprShoulder_Sun':
			df_SprSS=pd.DataFrame((join_df[join_df['service_id'] == grp]),columns=column_name)
			df_name.append(grp+'.csv')		
		elif grp=='FallShoulder_Fri-Sat':
			df_FallFS=pd.DataFrame((join_df[join_df['service_id'] == grp]),columns=column_name)
			df_name.append(grp+'.csv')		
		else:
			df_FallSun=pd.DataFrame((join_df[join_df['service_id'] == grp]), columns=column_name)
			df_name.append(grp+'.csv')
	
	#print df_name
	list_df=[df_SumST,df_SumFS,df_SH,df_SP,df_SB,df_SprFS,df_SprSS,df_FallFS,df_FallSun]
	#Converting the above list into CSV
	for i in range(0,len(list_df)):
		convert_csv(list_df[i],df_name[i])
	
	print "To CSV Convertion done"
	
	#Plotting
	plot_1 = df_SumST['arrival_time']
	plot_2= df_SumFS['arrival_time']
	plot_3=df_SH['arrival_time']
	plot_4 = df_SP['arrival_time']
	plot_5= df_SB['arrival_time']
	plot_6=df_SprFS['arrival_time']
	plot_7 = df_SprSS['arrival_time']
	plot_8= df_FallFS['arrival_time']
	plot_9=df_FallSun['arrival_time']	
	plot_list=map(None,plot_1,plot_2,plot_3,plot_4,plot_5,plot_6,plot_7,plot_8,plot_9)
	df_plot=pd.DataFrame(plot_list, columns=list_df) #.fillna(0)

	
	print df_plot
	#df_plot["TimeWeek"]=pd.to_timedelta(df_plot["TimeWeek"])
	#print df_plot['TimeWeek']
	'''
	if df_plot['TimeWeek'].shift() > df_plot['TimeWeek']:
		df_plot['Week_diff'] = (df_plot['TimeWeek']-df_plot['TimeWeek'].shift()).fillna(pd.to_timedelta("00:00:00"))
	'''
	#print df_plot
	'''
	freq_arrival=df_plot.count(axis=0, level=None,numeric_only=False)
	convert_csv(freq_arrival,'freq_arrival.csv')
	
	freq_arrival.plot(kind='pie')
	plt.show(freq_arrival)			#plots the total frequency for Weekday, Saturday and Holiday
	#print len_sat
	#print len_holi
	print "plotting done"

	#print thefile
	'''
	'''
	column_name = list(join_df.columns.values)    #Print the column name in the list
	print column_name
	'''
	
	#print week 
	#weekday = convert_df(week,column_name)
	#print weekday
	#weekday.to_csv(os.path.join(location,'weekday.csv'),index=None)
	

#Compare thedata for weekdays,weekends, Holidays and check the frequencies. Find average time difference
#can also find the number of times the bus stops at a particular station (frequency)
	

#Print the items that match with service_id==weekday
'''
	filt = join_df['service_id'] == 'weekday'
	dfj = join_df[filt]['trip_id']
	print dfj #http://stackoverflow.com/questions/28387180/python-print-row-name-in-csv-with-matching-column-contents-using-pandas
'''

def convert_csv(df,filename):
	return df.to_csv(os.path.join(location,filename),index=None)


conversion()	