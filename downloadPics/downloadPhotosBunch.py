import requests
import os
pathNamePrefix = "https://pzy.be/i/2/"
name = "neoslut"
start = 5485
stop = 5500

dirName = "neo"+str(start)+"_"+str(stop)
os.mkdir(dirName)
for i in range(start,stop):
    picName = name + str(i) + ".jpg"
    pathName = pathNamePrefix+picName
    print(picName)
    with open(dirName+"/"+picName, 'wb') as f:
        f.write(requests.get(pathName).content)




