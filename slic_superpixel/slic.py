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
    def show_image():
        pass

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

    def iterate(self, iteration=10):
        self.init_clusters()
        self.move_to_lowest_gradient()

        for i in range(iteration):
            cluster_pixels()
            update_cluster_position()
       
    def init_clusters(self):
        y = self.S // 2
        x = self.S // 2

        while h < self.height:
            while w < self.width:
                self.clusters.append(self.make_cluster(y, x))
                x += self.S

            x = self.S // 2
            y += self.S

    def make_cluster(self, h: int, w: int):
        return Cluster(self.image[h][w][0], self.image[h][w][1], self.image[h][w][2],
                       h, w)

    def move_to_lowest_gradient(self):
        for cluster in self.clusters:
            current_gradient = self.get_gradient(cluster.y, cluster.x)

            for dh in range(-1, 2):
                for dw in range(-1, 2):
                    _y = cluster.h + dh
                    _x = cluster.w + dw
                    new_gradient = self.get_gradient(_y, _x)
                    if new_gradient < current_gradient:
                        cluster.update(self.image[_y][_x][0],
                                       self.image[_y][_x][1],
                                       self.image[_y][_x][2],
                                       _y,
                                       _x)
                        current_gradient = new_gradient

    def get_gradient(self, y, x):
        if y + 1 > self.width:
            y = self.width - 2 
        if x + 1 > self.height:
            x = self.height - 2

        return self.image[y + 1][x + 1][0] - self.image[y][x][0] + \
               self.image[y + 1][x + 1][1] - self.image[y][x][1] + \
               self.image[y + 1][x + 1][2] - self.image[y][x][2]

    def cluster_pixels(self):
        pass

    def update_cluster_position(self):
        pass
