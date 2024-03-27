from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.125,0]

plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=0,
        autopct="%1.1f%%", wedgeprops={"edgecolor": "black"})

plt.title("My pie chart")
plt.tight_layout()

plt.show()