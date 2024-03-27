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

plt.style.use("fivethirtyeight")
#plt.xkcd()

with open("Matplotlib\data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row["LanguagesWorkedWith"].split(";"))



languages = []
utilisation = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    utilisation.append(item[1])

languages.reverse()
utilisation.reverse()

plt.barh(languages, utilisation)
plt.title("Most popular languages")
plt.xlabel("Programming languages")
plt.ylabel("Number of users self-reported")
plt.show()