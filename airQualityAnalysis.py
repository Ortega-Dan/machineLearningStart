import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')
# plt.style.use('default')

air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)

print(air_quality.head())

# air_quality["station_paris"].plot()
# plt.show()


air_quality.plot.area(subplots=True)
# plt.savefig("test.png")
plt.show()
