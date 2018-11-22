import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
installs = []
ratings = []

with open('data/googeplaystore.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            print('pushing categories into a separate array')
            categories.append(row)
            line_count += 1
        else:
            print('pushing ratings data into the ratings arrray')
            ratingsData = row[2]
            ratingsData = ratingsData.replace("NaN", "0")
            ratings.append(float(ratingsData))
            installData = row[5]
            installData = installData.replace(",", "")

            installs.append(np.char.strip(installData, "+"))
            line_count += 1

# get some values we can work with
# how many ratings are 4+
# how many are below 2
# how many are in the middle
np_ratings = np.array(ratings)
popular_apps = np_ratings > 4
print("popular apps:", len(np_ratings[popular_apps]))

percent_popular = len(np_ratings[popular_apps]) / len(np_ratings) * 100
print(percent_popular)

unpopular_apps = np_ratings < 2
print("unpopular apps:", len(np_ratings[unpopular_apps]))

percent_unpopular = len(np_ratings[unpopular_apps]) / len(np_ratings) * 100
print(percent_unpopular)

kinda_popular = 100 - (percent_popular + percent_unpopular)
print(kinda_popular)

# do a visualization with our shiny new data
labels = "Sucks", "Meh", "Love it"
sizes = [percent_unpopular, kinda_popular, percent_popular]
colors = ["darkgreen", "green", "yellow"]
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140) #  the problem is here somewher

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Do we love us some apps?")
plt.xlabel("User Ratings - App Installs (10,000+ apps")
plt.show()

# print('processed', line_count, 'lines of data')
# print(categories)
# print('first row of data: ', installs[0])
# print('last row of data:', installs[-1])
