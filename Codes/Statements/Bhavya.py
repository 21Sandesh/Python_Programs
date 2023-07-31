import random
import statistics


def gaussian_distribution():
    l = []
    for a in range(1000):
        l.append(random.gauss(100, 10))
    return l


a = gaussian_distribution()
print("Mean:", statistics.mean(a))
print("Standard Deviation:", statistics.stdev(a))
