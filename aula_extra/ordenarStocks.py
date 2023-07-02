def companyVolume(stocks, city):
    for i in stocks:
        if city == i[1]:
            print(i[0], i[4])



stocks = [('INTC', 'London', 34.249, 34.451, 1792860),
('TSLA', 'London', 221.33, 220.63, 398520),
('EA', 'Paris', 72.63, 68.98, 1189510),
('INTC', 'Tokyo', 33.22001, 34.28999, 4509110),
('TSLA', 'Paris', 217.35, 217.75, 252500),
('ATML', 'Frankfurt', 8.23, 8.36, 810440),
]


