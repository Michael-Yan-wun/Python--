#K-Means計算距離
class KMeans:
    def cal_dist(self, p0, p1):
#         """
#         比較兩點的距離
#         """
        return np.sqrt(np.sum((p0-p1)**2))
    
    def nearest_cluster_center(self, point, cluster_centers):
#         """
#         找到距離 point 最近的中心點
#         """
        min_dist = float("inf")
        m = cluster_centers.shape[0]
        for i in range(m):
            d = self.cal_dist(point, cluster_centers[i])
            if min_dist > d:
                min_dist = d
        return min_dist 

    def get_centroids(self, datapoints, k):
#         """
#         K-means++ 演算法，取得初始化中心點
#         """
        clusters = np.array([random.choice(datapoints)])
        dist = np.zeros(len(datapoints))
        
        for i in range(k-1):
            sum_dist = 0
            for j, point in enumerate(datapoints):
                dist[j] = self.nearest_cluster_center(point, clusters)
                sum_dist += dist[j]
            
            sum_dist *= random.random()
            for j, d in enumerate(dist):
                sum_dist = sum_dist - d
                if sum_dist <= 0:
                    clusters = np.append(clusters, [datapoints[j]], axis=0)
                    break
        
        return clusters
        
        
    def kmeans_plus_plus(self, datapoints, k=2):
#         """
#         K-means 演算法
#         """
        # 定義資料維度
        d = datapoints.shape[1]
        # 最大的迭代次數
        Max_Iterations = 1000

        cluster = np.zeros(datapoints.shape[0])
        prev_cluster = np.ones(datapoints.shape[0])

        cluster_centers = self.get_centroids(datapoints, k)

        iteration = 0
        while np.array_equal(cluster, prev_cluster) is False or iteration > Max_Iterations:
            iteration += 1
            prev_cluster = cluster.copy()

            # 將每一個點做分群
            for idx, point in enumerate(datapoints):
                min_dist = float("inf")
                for c, cluster_center in enumerate(cluster_centers):
                    dist = self.cal_dist(point, cluster_center)
                    if dist < min_dist:
                        min_dist = dist  
                        cluster[idx] = c   # 指定該點屬於哪個分群

            # 更新分群的中心
            for k in range(len(cluster_centers)):
                new_center = np.zeros(d)
                members = 0
                for point, c in zip(datapoints, cluster):
                    if c == k:
                        new_center += point
                        members += 1
                if members > 0:
                    new_center = new_center / members
                cluster_centers[k] = new_center

        return cluster

