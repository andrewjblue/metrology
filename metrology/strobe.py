import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np


def plots(dave):
    df = pd.read_csv(dave, delimiter = ",")
    df.head()

    print(df.columns)
    print(df['Strobe0'])
    print(df['Position'])
    chip_id = ['Chip 1', 'Chip 2', 'Chip 3', 'Chip 4', 'Chip 5', 'Chip 6', 'Chip 7', 'Chip 8', 'Chip 9', 'Chip 10']
    Strobe0 = df['Strobe0']
    Strobe1 = df['Strobe1']
    Positions = df['Position']

    x_indexes = np.arange(len(Positions))
    width = 0.25
    plt.bar(x_indexes - width / 2, Strobe0, width = width, color = 'r', label = 'Strobe 0')
    plt.bar(x_indexes + width / 2, Strobe1, width = width, color = 'b', label = 'Strobe 1')

    plt.legend(loc = 'upper left')
    plt.gcf().autofmt_xdate()
    plt.title('Hybrid ' + filename + ' Strobe Delay')
    plt.xlabel("ASIC")
    plt.grid()
    plt.ylabel("Strobe0 Delay (ns)")
    plt.xticks(df['Position'], chip_id)
    plt.ylim(0, 30)
    plt.show(block = True)


filename = sys.argv[1]
plots(filename)
