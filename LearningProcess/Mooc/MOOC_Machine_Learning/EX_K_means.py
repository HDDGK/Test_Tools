import numpy as np

'''
    cluster:样本簇
    centroid：簇中心

'''

class KMeans():
    def __int__(self,data,num_clustres):
        self.data=data
        self.num_clustres=num_clustres
    def train(self,max_iterations):
        centroids=KMeans.centroids_init(self.data,self.num_clustres)
        num_examples=self.data.shape[0]
        closest_centroids_ids=np.empty((num_examples,1))
        for i in range(max_iterations):
            closest_centroids_ids=KMeans.centroids_find_closest(self.data,centroids)
            centroids=KMeans.centroids_compute(self.data,closest_centroids_ids,self.num_clustres)
        return centroids,closest_centroids_ids


    @staticmethod
    def centroids_init(self,data,num_clustres):
        num_examples=data.shape[0]
        random_ids=np.random.permutation(num_examples)
        centroids=data[random_ids[:num_clustres],:]
        return centroids
    @staticmethod
    def centroids_find_closest(self,data,centroids):
        num_examples=self.data.shape[0]
        num_centroids=centroids.shape[0]
        closest_centroids_ids=np.zeros((num_examples,1))
        for example_index in range(num_examples):
            distance=np.zeros(num_centroids,1)
            for centroid_index in range(num_centroids):
                distance_diff=data[example_index,:]-centroids[centroid_index,:]
                distance[centroid_index]=(distance_diff**2)
            closest_centroids_ids[example_index]=np.argmin(distance)
        return closest_centroids_ids
    @staticmethod
    def centroids_compute(self,data,closest_centroids_ids,num_clustres):
        num_feature=data.shape[1]
        centroids=np.zeros((num_clustres,num_feature))
        for centroids_id in range(num_clustres):
            closest_ids=closest_centroids_ids==centroids_id
            centroids[closest_ids]=np.mean(data[closest_ids.flatten(),:],axis=0)
        return centroids