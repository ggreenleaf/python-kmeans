

#so we can use kmeans with anyinput type we have a data attribute
#data in this case will be a pixel with RGB color values
#since this will change we need to keep the original position as we assign it to clusters

class InputType(object):
    def __init__(self, pos, data):
        self.position = pos
        self.data = data
        self.cluster_assignment = None
