import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.image as mpimg

df = pd.read_csv("z_height.txt", delimiter = ",")
df.head()

logo = mpimg.imread('../logo.png')

print(df.columns)
print(df['Height'])
print(df['Position'])

Heights = df['Height']
Positions = df['Position']

Heights = Heights * -1
Heights = Heights * 1000

overall_median = 80
top=[100,100,100,100,100,100,100,100,100,100]
bottom=[60,60,60,60,60,60,60,60,60,60]

plt.fill_between(Positions, Heights, overall_median, where=(Heights>overall_median), interpolate = True,  color='#ff8000', alpha=0.25)
plt.fill_between(Positions, Heights, overall_median, where=(Heights<=overall_median), interpolate =True, color='#ff8000', alpha=0.25)
plt.fill_between(Positions, Heights, bottom, where=(Heights<=bottom), interpolate = True, color='#FF0000', alpha=0.25)


plt.legend()
plt.plot(Positions, top, linestyle='dotted', color='k')

plt.legend()
plt.plot(Positions, bottom, linestyle='dotted', color='k')

plt.plot(Positions, Heights, color='k')
# plt.tight_layout()

# plt.figure(logo, alpha=.15, zorder=1)

plt.title("ASIC-Hybrid Glue Thickess")
plt.xlabel("ASIC Position")
plt.ylabel("Glue Heigh (um)")
plt.xticks(df['Position'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.ylim(0, 110)
plt.show(block = True)
