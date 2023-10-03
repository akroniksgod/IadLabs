import matplotlib.pyplot as plt
import requests
import datetime
from matplotlib.dates import DateFormatter


def calc(col):
    ax = plt.figure().add_subplot(projection='3d')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    ax.set_xlabel("Дата")
    ax.set_ylabel("Курс доллара")
    ax.set_zlabel("Изменение")

    x = []
    y = []
    z = []

    for i in col:
        x.append(datetime.datetime.strptime(i.get("date"), '%Y-%m-%d'))
        y.append(i.get("usd"))
        z.append(i.get("delta"))

    ax.errorbar(x, y, z, 0.2)
    plt.show()


def get_calculated_delta_dict(col):
    new_col = []
    next_item = None
    length = len(col)
    for index, obj in enumerate(col):
        if index < (length - 1):
            next_item = col[index + 1]

        key = "usd"
        prev_usd = obj[key]
        current_usd = next_item[key]
        new_col.append({**obj, "delta": (prev_usd - current_usd) / current_usd * 100})

    return new_col


def get_dict():
    col = []
    days_count = 14
    date = datetime.datetime.today()
    for i in range(days_count):
        prev_date = date - datetime.timedelta(days=1)
        date = prev_date

        if prev_date.weekday() == 0 or prev_date.weekday() == 6:
            continue

        prepared_link = 'https://www.cbr-xml-daily.ru/archive/{}/{}/{}/daily_json.js'

        month = '0' + str(prev_date.month) if prev_date.month < 10 else prev_date.month
        day = '0' + str(prev_date.day) if prev_date.day < 10 else prev_date.day

        link = prepared_link.format(prev_date.year, month, day)
        current_request = requests.get(link)
        current_parsed_request = current_request.json()
        usd = current_parsed_request['Valute']['USD']['Value']

        col.append({"date": str(prev_date.date()), "usd": usd})

    return col


if __name__ == '__main__':
    base_collection = get_dict()
    prepared_collection = get_calculated_delta_dict(base_collection)
    calc(prepared_collection)
