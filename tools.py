import matplotlib.pyplot as plt
import csv

def ReadData(filename='./showcases.2011.csv'):
    """Reads a CSV file of data.

    Args:
      filename: string filename

    Returns: sequence of (price1 price2 bid1 bid2 diff1 diff2) tuples
    """
    fp = open(filename)
    reader = csv.reader(fp)
    res = []

    for t in reader:
        _heading = t[0]
        data = t[1:]
        try:
            data = [int(x) for x in data]
            # print heading, data[0], len(data)
            res.append(data)
        except ValueError:
            pass

    fp.close()
    return zip(*res)

def Plot(p):
    x = []
    prob = []
    for _x, _prob in sorted(p.Items()):
        x.append(_x)
        prob.append(_prob)
    plt.plot(x, prob)
    plt.show()
