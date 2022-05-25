import csv
import random
import datetime

#  Run file to generate a csv of transactions to import into the app



# Number of entries you want
records=100

fieldnames=['date','merchant','amount']
writer = csv.DictWriter(open("example.csv", "w"), fieldnames=fieldnames)

# start date
startdate=datetime.date(2021,6,15)
# date range (days)
date_range = [1,365]

# list of uk merchants
merchants=['Amazon','Argos','Apple','Tesco','Asda','Next','Marks & Spencer','Asos','Netflix','National Rail','John Lewis','Trainline','B&Q','Debenhams','Thomson','Expedia','EasyJet','Boots','Sports Direct','Currys','Ryanair','Thomas Cook','O2','Ticketmaster','New Look','Very','LastMinute','IKEA','Sainsburys','Homebase','Travel Republic','River Island','Premier Inn','British Airways','Screwfix','House of Fraser','Halfords','Littlewoods','PC World','Wickes','Travelodge','JD Sports','Mataln','Boohoo','Cineworld','National Express']

#amount
pounds_range = [0,50]
pence_range = [0,99]    

writer.writerow(dict(zip(fieldnames, fieldnames)))
for number in range(0, records):
  writer.writerow(dict([
    ('date', (startdate+datetime.timedelta(random.randint(date_range[0],date_range[1]))).strftime('%d/%m/%Y')),
    ('merchant', random.choice(merchants)),
    ('amount', f'{random.randint(pounds_range[0],pounds_range[1])}.{random.randint(pence_range[0],pence_range[1])}')]))
