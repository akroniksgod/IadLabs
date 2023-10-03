import matplotlib.pyplot as plt
import numpy as np
import json
import requests
import datetime


def calc():
    ax = plt.figure().add_subplot(projection='3d')

    # setting up a parametric curve
    t = np.arange(0, 2 * np.pi + .1, 0.01)
    x, y, z = np.sin(t), np.cos(3 * t), np.sin(5 * t)

    estep = 15
    i = np.arange(t.size)
    zuplims = (i % estep == 0) & (i // estep % 3 == 0)
    zlolims = (i % estep == 0) & (i // estep % 3 == 2)

    ax.errorbar(x, y, z, 0.2, zuplims=zuplims, zlolims=zlolims, errorevery=estep)

    ax.set_xlabel("X label")
    ax.set_ylabel("Y label")
    ax.set_zlabel("Z label")

    plt.show()


def get_dates():
    days_count = 14
    date = datetime.datetime.today()
    for i in range(days_count):
        prev_date = date - datetime.timedelta(days=1)

        if prev_date.weekday() == 0 or prev_date.weekday() == 6:
            date = prev_date
            continue

        prepared_link = 'https://www.cbr-xml-daily.ru/archive/{}/{}/{}/daily_json.js'

        month = '0' + str(prev_date.month) if prev_date.month < 10 else prev_date.month
        day = '0' + str(prev_date.day) if prev_date.day < 10 else prev_date.day

        link = prepared_link.format(prev_date.year, month, day)

        current_request = requests.get(link)
        current_parsed_request = current_request.json()

        date = prev_date


if __name__ == '__main__':
    get_dates()
