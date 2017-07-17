# -*- coding: utf-8 -*-


# oo
class Averager(object):
    """Docstring for Averager. """

    def __init__(self):
        """ """
        self.series = []

    def __call__(self, new_value):
        """ Docstring for __call__.

        """
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def averager():
    """docstring for averager"""
    series = []

    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return average


def average_v1():
    """python 2 average_v1"""
    d = dict(sum=0, total=0)

    def averager(new_value):
        """docstring for averager"""

        d['sum'] = d['sum'] + new_value
        d['total'] += 1
        return d['sum'] / d['total']
    return averager


if __name__ == '__main__':
    #  ave = averager()
    ave = average_v1()
    print ave(10)
    print ave(12)
    print ave(14)
