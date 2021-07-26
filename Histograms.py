

import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

def SaveHist(HList, FName, Title, XLabel, YLabel):

	plt.hist(HList, 150)
	plt.xlabel(XLabel)
	plt.ylabel(YLabel)
	plt.title(Title)
	plt.grid(True)
	plt.savefig(FName)
	plt.close()


#x = np.random.randn(100000)

#SaveHist(x, "test.out.pdf", "Titel", "X Label", "Y Label")

PuL = {}
DoL = {}
FIn=open("C:\\Work\\NYTaxi-old\\YellowAllCleanup.csv","r")
reader=csv.reader(FIn)

next(reader, None)


#for row in reader:
    #if int(row[7]) not in PuL.keys():
     #   PuL[int(row[7])]=[]
    #if int(row[7]) in PuL.keys():
     #   PuL[int(row[7])].append(float(row[16]))

#print(PuL)
 
for row in reader:
    if int(row[8]) not in DoL.keys():
        DoL[int(row[8])]=[]
    if int(row[8]) in DoL.keys():
        DoL[int(row[8])].append(1)

#print(DoL)
FOut=open("DropoffCounter.csv","w",newline="")
writer=csv.writer(FOut)
row1=("Drop of Zone","Frequency")
writer.writerow(row1)

for key in DoL:
    row=(key,len(DoL[key]))
    writer.writerow(row)


#for key in PuL:
    #ZoneNumber=key
    #FileName="ZoneNumber-%05d" %ZoneNumber
    #SaveHist(PuL[key],FileName,FileName,"Fare","frequency")

    #row=(key,len(PuL[key]),np.mean(PuL[key]),np.std(PuL[key]))
    #writer.writerow(row)

FOut.close()