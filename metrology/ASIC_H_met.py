import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches
import sys


def plots(dave, mm):
    df = pd.read_csv(dave, delimiter = ",")
    df.head()

    print(df.columns)
    print(df['Height'])
    print(df['Position'])

    Heights = df['Height']
    Positions = df['Position']
    Heights = Heights * -1000

    overall_median = mm
    top = [mm + 20] * 10
    bottom = [mm - 20] * 10
    bob = top[0]
    print(bob)

    fig, ax1 = plt.subplots()

    ax1.fill_between(Positions, Heights, overall_median, where = (Heights > overall_median), interpolate = True,
                     color = '#ff8000', alpha = 0.25)
    ax1.fill_between(Positions, Heights, overall_median, where = (Heights <= overall_median), interpolate = True,
                     color = '#ff8000', alpha = 0.25)

    ax1.fill_between(Positions, Heights, bottom, where = (Heights <= bottom), interpolate = True, color = '#FF0000')
    ax1.fill_between(Positions, Heights, top, where = (Heights > top), interpolate = True, color = '#FF0000')

    a1 = ax1.plot(Positions, top, linestyle = 'dotted', color = 'k', label = 'Upper/Lower Tolerances')
    a2 = ax1.plot(Positions, bottom, linestyle = 'dotted', color = 'k')
    ax1.plot(Positions, Heights, color = 'k', label = 'Hybrid 2023')

    red_patch = mpatches.Patch(color = '#FF0000', label = 'Out of Spec')
    pink_patch = mpatches.Patch(color = '#ff8000', label = 'In  Spec')
    ax1.legend(loc = [0.1, 0.2])

    leg1 = ax1.legend(loc = 'upper left')
    leg2 = ax1.legend([pink_patch, red_patch], ['In Spec', 'Out of Spec'], loc = 'upper right', frameon = False)
    ax1.add_artist(leg1)

    plt.title("ASIC-Hybrid Glue Thickess")
    plt.xlabel("ASIC Position")
    plt.ylabel("Glue Heigh (um)")
    plt.xticks(df['Position'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    plt.ylim(0, bob + 30)
    plt.show(block = True)
    fig.savefig('Height.png')


filename = sys.argv[1]
med = int(sys.argv[2])

plots(filename, med)
