import pymongo
import pandas as pd
import matplotlib.pyplot as plt

url='mongodb://localhost:27017'
mydb=pymongo.MongoClient(url) #pastikan mongodb aktif
newdb=mydb['Kampus']
newcol=newdb['Dosen']
newcol2=newdb['Mahasiswa']

cursor=newcol.find()
data=pd.DataFrame(list(cursor))
data.status='dosen'
print(data.loc[:,["asal","nama","status","usia"]])
cursor2=newcol2.find()
data2=pd.DataFrame(list(cursor2))
data2.index = [0,1,2]
data2['status'] = ['mahasiswa', 'mahasiswa', 'mahasiswa']
data2=data2.loc[:,["asal","nama","status","usia"]]
print(data2)
plt.title('Usia Warga Kampus')
plt.bar(data.nama,data.usia, color='steelblue')
plt.bar(data2.nama,data2.usia,color='orange')
plt.grid(True)
plt.legend(['Dosen','Mahasiswa'])
plt.show()