import csv
import numpy as np
total_entries=[]
def mean():
    with open("SOCR-HeightWeight.csv",newline="") as f:
        reader = csv.reader(f)
        filedata=list(reader)
    filedata.pop(0)
    total=0
    total_entries = len(filedata)

    for height in filedata:
        total += float(height[1])
    print(total_entries)
    print("Mean:"+str(total))
def median():
    with open("SOCR-HeightWeight.csv",newline="") as f:
        reader = csv.reader(f)
        filedata=list(reader)
    filedata.pop(0)
    newdata=[]
    for i in range(len(filedata)):
        nnump = filedata[i][1]
        newdata.append(float(nnump))
    n = len(newdata)
    newdata.sort()
    if n%2 == 0:
        median1=float(newdata[n//2])
        median2=float(newdata[n//2-1])
        median=(median1+median2)/2
    else:
        median = newdata[n//2] 
        print(n)
    print("Median:"+median)       
def mode():
    from collections import Counter 
    with open("SOCR-HeightWeight.csv",newline="") as f:
        reader = csv.reader(f)
        filedata=list(reader)
    filedata.pop(0)
    newdata=[]
    for i in total_entries:
        nnump = filedata[i][1]
        newdata.append(float(nnump))
    data = Counter(newdata)
    modedataforrange = {
                            "75-85":0,
                            "85-95":0,
                            "95-105":0,
                            "105-115":0,
                            "115-125":0,
                            "125-135":0,
                            "135-145":0,
                            "145-155":0,
                            "155-165":0,
                            "165-175":0
                        }    
    for height ,occurence in data.items():
        if 75<float(height)<85:
            modedataforrange["75-85"]+=occurence
        elif 85<float(height)<95:
            modedataforrange["85-95"]+=occurence 
        elif 95<float(height)<105:
            modedataforrange["95-105"]+=occurence
        elif 105<float(height)<115:
            modedataforrange["105-115"]+=occurence 
        elif 115<float(height)<125:
            modedataforrange["115-125"]+=occurence   
        elif 125<float(height)<135:
            modedataforrange["125-135"]+=occurence               
        elif 135<float(height)<145:
            modedataforrange["135-145"]+=occurence 
        elif 145<float(height)<155:
            modedataforrange["145-155"]+=occurence
        elif 155<float(height)<165:
            modedataforrange["155-165"]+=occurence
        elif 165<float(height)<175:
            modedataforrange["165-175"]+=occurence               
    moderange,modeoccurence=0,0
    for range, occurence in modedataforrange.items():
        if occurence > modeoccurence:
            moderange, modeoccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((moderange[0] + moderange[1]) / 2)
    print(f"Mode is -> {mode:2f}  "+mode)
    print()
              
        
mean()
median()
mode()  
"""newdata=[]
for i in range(len(filedata)):
    nnump = filedata[i][1]
    newdata.append(float(nnump))
    
n = len(newdata)
total = 0 
for x in newdata:
      total+=x
mean=total/n    

print()  """
