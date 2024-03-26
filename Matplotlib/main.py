import lxml
import json
import os
import numpy as np
import csv
from timeit import default_timer as timer
from apscheduler.schedulers.background import BlockingScheduler
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from collections import Counter

#plt.style.use("fivethirtyeight")
plt.xkcd()

with open("data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row["LanguagesWorkedWith"].split(";"))

languages = []
utilisation = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    utilisation.append(item[1])

plt.barh(languages, utilisation)
plt.title("Most popular languages")
plt.xlabel("Programming languages")
plt.ylabel("Number of users self-reported")
plt.show()
# #print(plt.style.available)
# #plt.xkcd()

# # Median Developer Salaries by Age
# ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# x_indexes = np.arange(len(ages_x))
# width = 0.25

# dev_y = [38496, 42000, 46752, 49320, 53200,
#          56000, 62316, 64928, 67317, 68748, 73752]
# plt.bar(x_indexes - width, dev_y, width=width, color="k", linestyle="--", label="All developers")

# # Median Python Developer Salaries by Age
# py_dev_y = [45372, 48876, 53850, 57287, 63016,
#             65998, 70003, 70000, 71496, 75370, 83640]
# plt.bar(x_indexes, py_dev_y, width=width, color="#5a7d9a", label="Python developers")

#js_dev_y = [37810, 43515, 46823, 49293, 53437,
            #56373, 62375, 66674, 68745, 68746, 74583]
#plt.bar(x_indexes + width, js_dev_y, width=width, color="#adad3b", label="JavaScript developers")



# plt.xlabel("Ages")
# plt.ylabel("Salary (USD)")
# plt.title("Median salary (USD) by age")

# plt.tight_layout()

# plt.legend()

# plt.xticks(ticks=x_indexes, labels=ages_x)

# plt.grid(True)

#plt.show()