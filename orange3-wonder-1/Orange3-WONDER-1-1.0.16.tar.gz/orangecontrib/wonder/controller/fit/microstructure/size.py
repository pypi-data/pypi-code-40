import numpy

from orangecontrib.wonder.controller.fit.fit_parameter import ParametersList
from orangecontrib.wonder.controller.fit.wppm_functions import Normalization, Distribution, \
    lognormal_distribution, delta_distribution, gamma_distribution, york_distribution, lognormal_average

class Shape:
    NONE = "none"
    SPHERE = "sphere"
    CUBE = "cube"
    TETRAHEDRON = "tetrahedron"
    OCTAHEDRON = "octahedron"
    CYLINDER = "cylinder"

    @classmethod
    def tuple(cls):
        return [cls.NONE, cls.SPHERE, cls.CUBE, cls.TETRAHEDRON, cls.OCTAHEDRON, cls.CYLINDER]


class SizeParameters(ParametersList):

    shape = Shape.SPHERE
    distribution = Distribution.LOGNORMAL
    mu = None
    sigma = None
    add_saxs = False
    normalize_to = Normalization.NORMALIZE_TO_N

    @classmethod
    def get_parameters_prefix(cls):
        return "size_"

    def __init__(self, shape, distribution, mu, sigma, add_saxs=False, normalize_to=Normalization.NORMALIZE_TO_N):
        super(SizeParameters, self).__init__()

        self.shape = shape
        self.distribution = distribution
        self.mu = mu
        self.sigma = sigma
        self.add_saxs = add_saxs
        self.normalize_to = normalize_to

    def get_distribution(self, auto=True, D_min=None, D_max=None):
        if auto:
            D_min = 0
            D_max = 1000

        step  = (D_max-D_min)/1000
        x     = numpy.arange(start=D_min, stop=D_max, step=step)
        D_avg = self.get_D_average()
        sigma = self.sigma.value

        try:
            y = self.__get_distribution_values(x)

            if auto:
                D_min, D_max = self.__get_auto_limits(x, y)

                x, y, D_min, D_max, D_avg, sigma = self.get_distribution(auto=False, D_min=D_min, D_max=D_max)
        except:
            pass

        return x, y, D_min, D_max, D_avg, sigma

    def get_D_average(self):
        if self.distribution == Distribution.LOGNORMAL:
            return lognormal_average(self.mu.value, self.sigma.value)
        elif self.distribution == Distribution.GAMMA or self.distribution == Distribution.YORK:
            return self.mu.value
        else:
            return 0.0

    def __get_distribution_values(self, x):
        if self.distribution == Distribution.LOGNORMAL:
            y = lognormal_distribution(self.mu.value, self.sigma.value, x)
        elif self.distribution == Distribution.GAMMA:
            y = gamma_distribution(self.mu.value, self.sigma.value, x)
        elif self.distribution == Distribution.YORK:
            y = york_distribution(self.mu.value, self.sigma.value, x)
        elif self.distribution == Distribution.DELTA:
            y = delta_distribution(self.mu.value, x)
        else:
            y = numpy.zeros(len(x))

        y[numpy.where(numpy.logical_or(numpy.isnan(y), numpy.isinf(y)))] = 0.0

        return y

    def __get_auto_limits(self, x, y):
        good = x[numpy.where(y > 1e-5)]

        D_min = good[0]
        D_max = good[-1]

        if D_min == D_max: D_min = x[0]
        if D_min < 5: D_min = 0.0

        return D_min, D_max
