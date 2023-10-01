import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import xlrd


def loadData(filePath):
    wb=xlrd.open_workbook(r"C:\Users\HK145-TP\Desktop\city.xlsx")
    # wb=xlrd.open_workbook(filePath)
    name=wb.sheet_names()
    # print(name)
    v_data=wb.sheets()[0]
    row=v_data.nrows
    col=v_data.ncols
    print(row)
    print(col)


    # print(v_data.cell(0,0).value)


    # txtStr = fr.read()
    # print(txtStr)
    # lines=fr.readlines()
    # retData=[]
    # retCityName=[]
    # for line in lines:
    #     items=line.strip().split(',')
    #     retCityName.append(items[0])
    #     retData.append([float(items[1]) for i in range(1,len(items))])
    #     return retData,retCityName


def createDataSet():
    print('DataCreat')
    return [[1,1],[1,2],[2,1],[6,4],[6,3],[5,4]]


def calcDis(dataset, centroids, k):
    print("计算欧拉距离")
    clalist=[]
    for data in dataset:
        diff=np.tile(data,(k,1))-centroids
        squaredDiff=diff**2
        squaredDist=np.sum(squaredDiff,axis=1)
        distance=squaredDist**0.5
        clalist.append(distance)
    clalist=np.array(clalist)
    return clalist


def classify(dataset, centroids, k):
    print("计算质心")
    clalist=calcDis(dataset,centroids,k)
    minDistIndices=np.argmin(clalist,axis=2)
    newCentroids=pd.DataFrame(dataset).groupby(minDistIndices).mean()
    newCentroids=newCentroids.values
    print(newCentroids)
    print(centroids)
    changed=newCentroids-centroids
    print(changed)
    return changed,newCentroids

def kmeans(dataset, k):
    print("分类")
    centroids=random.sample(dataset,k)
    changed,newcentroids=classify(dataset,centroids,k)
    while np.any(changed!=0):
        changed,newcentroids=classify(dataset,centroids,k)
    centroids =sorted(newcentroids.tolist())

    print("分类over1")
    cluster=[]
    clalist=calcDis(dataset,centroids,k)
    minDistIndices=np.argmin(clalist,axis=1)
    print("分类over2")
    for i in range(k):
        cluster.append([])
    print("分类over3")
    for i,j in enumerate(minDistIndices):
        cluster[j].append(dataset[i])
    print("分类over4")
    return centroids,cluster


def main():
    dataset=createDataSet()
    centriods,cluster=kmeans(dataset,1)
    print("finall")
    print("质心为：%s"%centriods)
    print("集群为：%s"%cluster)
    for i  in range(len(dataset)):
        plt.scatter(dataset[i][0],dataset[i][1],marker='o',color='green',s=40,label='Orignal')
    for j in range(len(centriods)):
        plt.scatter(centriods[j][0],centriods[j][1],marker='x',color='red',s=50,label='center')
    plt.show()
if __name__ == '__main__':
    '''
    聚类算法之一
    分为K簇
    1、随机K点聚类中心
    2、剩余点算离中心点距离，归入最近簇
    3、每个簇，计算均值为新的聚类中心
    4、重复2、3步。直至不变
    '''
    print("run")
    main()

'''
    data,cityName=loadData('./city.xls')
    # km=KMeans(n_clusters=3)
    # #n_clusters=聚类中心个数
    #
    # label=km.fit_predict(data)
    # expenses=np.sum(km.cluster_centers_,axis=1)
    # print(expenses)
    # CityCluster=[[],[],[]]
    # for i in range(len(cityName)):
    #     CityCluster[label[i].append(cityName[i])]
    # for i in range(len(CityCluster)):
    #     print("Expenses:%.2f"%expenses[i])
    #     print(CityCluster[i])
'''