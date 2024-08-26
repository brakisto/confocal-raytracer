import numpy as np


class Ray(object):

    def __init__(self, y0, z0, theta, wavelenght=600):
        self.y0 = y0
        self.z0 = z0
        self.theta = theta
        self.wavelenght = wavelenght
        self.ray = _init_vec(np.cos(theta), np.sin(theta))
        self.path = [(y0, z0)]
        self.thetas = [theta]

    def update_ray(self, y0, z0, theta):
        self.y0, self.z0, self.theta = y0, z0, theta
        self.ray = _init_vec(np.cos(theta), np.sin(theta))
        self.path.append((y0, z0))
        self.thetas.append(theta)


def _init_vec(x, y):
    vec = np.empty(2)
    vec[0] = x
    vec[1] = y
    return vec
