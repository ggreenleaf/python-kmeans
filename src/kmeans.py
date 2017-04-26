# import numpy as np
import color_utils as cu
from itertools import groupby
import numpy as np

def find_nearest(array, value):
    idx = (np.abs(array - value)).argmin()
    return idx

class Kmeans(object):
    def __init__(self, inputs, means):
        self.inputs = inputs
        self.centroids = means
        self.change_made = True

    def start(self):
        gen = 0
        while self.change_made:
            self.assignment()
            self.update()
            print("generation: ", gen)
            gen += 1

    def assignment(self):
        '''assign inputs to their new clusters'''
        self.change_made = False
        for item in self.inputs:
            did_update = self.update_item(item)
            if (did_update):
                self.change_made = True

    def update_item(self, item):
        updated = False
        distances = [cu.euclidean_distance(item.data, centroid) for centroid in self.centroids]
        min_distance = min(distances)
        new_cluster = find_nearest(distances, min_distance)
        if (new_cluster != item.cluster_assignment):
            item.cluster_assignment = new_cluster
            return True
        return False

    def update(self):
        '''calculate the new centroid values'''
        #slow and bad need to fix
        for i in range((len(self.centroids))):
            cluster = [item for item in self.inputs if item.cluster_assignment == i]
            self.update_centroid(cluster, i)


    def update_centroid(self, cluster, index):
        self.centroids[index] = cu.average(cluster)
