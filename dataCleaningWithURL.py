import pandas as pd 
import numpy as np
import urllib3

medals_url = "http://winterolympicsmedals.com/medals.csv" # the website
http = urllib3.PoolManager()  # we used the module urlib3 fot get the list of  winter olympics games.
read_url = http.request('GET',medals_url)
stat=read_url.status # check the status of server
df = read_url.data # this is the data frame the from the httml page
print (stat)
print(df)

archivo = open("urlpractica.txt","w") # create an empty text file
encoding="utf-8" # encoding to utf-8  
decodificar = df.decode(encoding) # translate the binary data to text data
for i in decodificar: # we read all the website transale and write the new textt file
    archivo.write(i)
archivo.close() # close file

lectura = open("urlpractica.txt") # now open the file and read
count=0
main_dict={}
columna = lectura.readline().strip().split(",") # read the first line of the file and see the columns and use sptip and slplit functions
cantidadColumnas = len(columna) # count the columns
print("la cantidad de columnas es:",cantidadColumnas) 

for c in columna:
    main_dict[c] = [] # here we got a sample dict with the key of de title of de table (the first lines of the text)
for line in lectura: # in this for loop we read avery lines in the text 
    values = line.strip().split(",")# we delete spaces and separated with "," for make the columns
    for i in range(len(columna)):
        main_dict[columna[i]].append(values[i])# here we add in the dict all de data for every line 
    count+=1 #simple counter for lines
dfUrl= pd.DataFrame(main_dict) # convert the dict in a data frame 
print ("la cantidad de columnas es:",cantidadColumnas,"la cantidad de filas es:",count)
dfUrl.head()#read ten first line of the data frame with pandas as pd.