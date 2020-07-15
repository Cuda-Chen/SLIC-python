import numpy as np
from skimage import io, color

class Cluster(object):
    cluster_index = 0

    def __init__(self, l, a, b, y, x):
        self.update(l, a, b, y, x)
        self.pixels = []
        self.index = cluster_index
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
    def save_image():
        pass

    def __init__(self, inputimage, K, M):
        self.K = K
        self.M = M

        self.image = read_image(inputimage)
        self.height = self.image.shape[0]
        self.width = self.image.shape[1]
        self.S = int(np.sqrt((self.height * self.width) / self.K))

        self.clusters = []
        self.label = {}
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
        for cluster in self.clusters:
            for y in range(cluster.y - 2 * self.S, cluster.y + 2 * self.S):
                if y < 0 or y >= self.height:
                    continue

                for x in range(cluster.x - 2 * self.S, cluster.x + 2 * self.S):
                    if x < 0 or x >= self.width:
                        continue

                    L, A, B = self.image[y][x]
                    Dc = np.sqrt(np.power(L - cluster.l, 2) +
                                 np.power(A - cluster.a, 2) + 
                                 np.power(B - cluster.b, 2))
                    Ds = np.sqrt(np.power(y - cluster.y, 2) +
                                 np.power(x - cluster.x, 2))
                    D = np.sqrt(np.power(Dc / self.M, 2) + np.power(Ds / self.S, 2))

                    if D < self.distance[y][x]:
                        if (y, x) not in self.label:
                            self.label[(y, x)] = cluster
                            cluster.pixels.append((y, x))
                        else:
                            self.label[(y, x)].pixels.remove((y, x))
                            self.label[(y, x)] = cluster
                            cluster.pixels.append((y, x))
                        self.distance[y][x] = D
                            

    def update_cluster_position(self):
        for cluster in self.clusters:
            sum_h = sum_w = 0
            pixel_count = len(cluster.pixels)

            for pixel in cluster.pixels:
                sum_h += pixel[0]
                sum_w += pixel[1]
                
            new_y = sum_h // pixel_count
            new_x = sum_w // pixel_count
            cluster.update(self.image[new_y][new_x][0], 
                           self.image[new_y][new_x][1],
                           self.image[new_y][new_x][2],
                           new_y,
                           new_x)

if __name__ == '__main__':
    print("I am fine")
