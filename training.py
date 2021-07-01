import csv
import re

spam = 0
ham = 0
text = []
ws = dict()
wh = dict()
psw = dict()
with open('TrainingData.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        row[1] = row[1].lower()
        row[1] = re.sub(r'[^\w\s]', '', row[1])
        text = row[1].split()
        for word in text:
            if word in psw:
                pass
            else:
                psw[word] = 0.001
            if row[0] == 'spam':
                spam += 1
                if word in ws:
                    ws[word] += 1
                else:
                    ws[word] = 1
            else:
                ham += 1
                if word in wh:
                    wh[word] += 1
                else:
                    wh[word] = 1
for word in psw:
    if word in ws:
        if word in wh:
            psw[word] = round(((ws[word]/spam)*spam/(ham+spam)) /
                              ((ws[word]/spam) * spam / (ham+spam) + (wh[word]/ham) * ham / (ham+spam)), 3)
        else:
            psw[word] = 1
