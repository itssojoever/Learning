import numpy as np
import csv
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use("fivethirtyeight")
#plt.xkcd()

data = pd.read_csv("Matplotlib\data.csv")
ids = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(";"))



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