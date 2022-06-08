
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.cluster import KMeans
import json


data = pd.read_csv(
    r'D:\ClientProjects\CustomerSigmentation\Mall_Customers.csv')
x = data.iloc[:, [3, 4]].values


def elbow_method():
    wcss = []
    for i in range(1, 11):
        km = KMeans(n_clusters=i, init='k-means++',
                    max_iter=300, n_init=10, random_state=0)
        km.fit(x)
        wcss.append(km.inertia_)
    print(wcss)
    return wcss


def kmeans_cluster():
    kmeans = KMeans(n_clusters=5, init='k-means++',
                    max_iter=300, n_init=10, random_state=0)
    ymeans = kmeans.fit_predict(x)
    usual_customers = [x[ymeans == 0, 0]] +[ x[ymeans == 0, 1]]
    priority_customer = [x[ymeans == 1, 0]]+[x[ymeans == 1, 1]]
    target_customer_young = [x[ymeans == 2, 0]]+[x[ymeans == 2, 1]]
    target_customer_old = [x[ymeans == 3, 0]]+[x[ymeans == 3, 1]]
    list_4 = [x[ymeans == 4, 0]]+[x[ymeans == 4, 1]]
    kmean_cluster = [kmeans.cluster_centers_[
        :, 0]]+[kmeans.cluster_centers_[:, 1]]
    print(ymeans)
    return {'ymeans': ymeans, 'usual_customers': usual_customers, 'priority_customer': priority_customer, 'target_customer_young': target_customer_young, 'target_customer_old': target_customer_old,'list_4':list_4,'kmean_cluster': kmean_cluster}


def gender():
    size = data['Gender'].value_counts().to_list()
    return size
