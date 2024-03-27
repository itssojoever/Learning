from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("Matplotlib\data1.csv")
ages = data["Age"]
dev_salaries = data["All_Devs"]
python_salaries = data["Python"]
js_salaries = data["JavaScript"]

#all developers
plt.plot(ages, dev_salaries, color="#444444", linestyle ="--", label="All developers")

#python developers
plt.plot(ages, python_salaries, label="Python developers")

median = 57287

plt.fill_between(ages, python_salaries, median, where=(python_salaries > median), interpolate=True, alpha=0.25, label="above median salary")
plt.fill_between(ages, python_salaries, median, where=(python_salaries <= median), interpolate=True, color="red", alpha=0.25, label="below median salary")


plt.legend()

plt.title("Median salary by age")
plt.xlabel("Ages")
plt.ylabel("Median salary")

plt.tight_layout

plt.show()