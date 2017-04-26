import numpy as np

def euclidean_distance(pixel_one, pixel_two):
        rgb_one = np.asarray(pixel_one)
        rgb_two = np.asarray(pixel_two)
        average = np.linalg.norm(rgb_one - rgb_two)
        return average

def average(inputs):
    '''find the average color that is the sum of each component over the length'''
    mapped = np.asarray(list(map(lambda x: x.data, inputs)))
    return np.sum(mapped, axis=-2) / len(mapped)
    # return np.average(inputs, axis=-2) #might work?
