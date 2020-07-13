import numpy as np
from skimage import io, color

class Cluster(object):
    cluster_index = 0

    def __init__(self, l, a, b, y, x):
        self.update(l, a, b, y, x)
        self.number = cluster_index
        Cluster.cluster_index += 1

    def update(self, l, a, b, y, x):
        self.l = l
        self.a = a
        self.b = b
        self.y = y
        self.x = x

class Slic(object):
    @staticmethod
    def read_image(inputimage):
        image_rgb = io.imread(inputimage)
        image_lab = color.rgb2lab(image_rgb)
        return image_lab

    @staticmethod
    def save_image(inputimage):
        pass

    def __init__(self, inputimage, K, M):
        self.K = K
        self.M = M

        self.image = read_image(inputimage)
        self.height = self.image.shape[0]
        self.width = self.image.shape[1]
        self.S = int(np.sqrt((self.height * self.width) / self.K))

        self.clusters = []
        self.label = np.fill((self.height, self.width), -1)
        self.distance = np.fill((self.height, self.width), np.inf)
