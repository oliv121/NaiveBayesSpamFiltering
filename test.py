import training
import csv
import re

result = 0
n = 0
with open('TestData.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        p1 = 1
        p2 = 1
        p = 0
        n += 1
        row[1] = row[1].lower()
        row[1] = re.sub(r'[^\w\s]', '', row[1])
        text = row[1].split()
        for word in text:
            if word in training.psw:
                if training.psw[word] < 0.49 or training.psw[word] > 0.51:
                    p1 *= training.psw[word]
                    p2 *= (1-training.psw[word])
        p = round(p1/(p1+p2), 4)
        if (p >= 0.5 and row[0] == 'spam') or (p < 0.5 and row[0] == 'ham'):
            result += 1

print('Количесво сообщений: ', n)
print('Количесво верно классифицированных сообщений: ', result)
print('Точность классификации: ', round((result*100/n)), '%')
