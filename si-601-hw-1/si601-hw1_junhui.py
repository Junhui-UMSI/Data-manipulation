import csv, math
from math import exp, expm1, log
from operator import itemgetter, attrgetter
input_file = open('world_bank_indicators.txt','rU')
header = (input_file.readline()).split('\t')

# print all the rows that contained date with 2000 or 2010, convert them into an array, each item in array is a row of data
allrows = []
index = 0
for line in input_file:
    entries = line.split('\t')
    date = entries[1].split('/')[2]
    if date == '2000' or date == '2010':
        allrows.append(entries)


i = 0
for x in header:
    if x == 'Country Name':
        idCountry = i
    elif x == 'Date':
        idDate = i
    elif x == 'Population: Total (count)':
        idPopulation = i
    elif x == 'Business: Mobile phone subscribers':
        idMobile = i
    elif x == 'Business: Internet users (per 100 people)':
        idInternet = i
    elif x == '"Health: Mortality, under-5 (per 1,000 live births)"':
        idHealth = i
    elif x == 'Finance: GDP per capita (current US$)\n':
        idGDP = i
    i += 1

# print idCountry, idDate, idMobile, idInternet, idHealth, idPopulation, idGDP  # the index of the columes that we want to keep

firsteditrow=[]
editrow = []
for row in allrows:
    if row[idDate] != '':
        row[idDate] = row[idDate].strip('"')
    if row[idMobile] != '':
        row[idMobile] = int(row[idMobile].strip('"').replace(',',''))
    if row[idInternet] != '':
        row[idInternet] = int(row[idInternet].strip('"').replace(',',''))
    if row[idHealth] != '':
        row[idHealth] = int(row[idHealth].strip('"').replace(',',''))
    if row[idPopulation] != '':
        row[idPopulation] = int(row[idPopulation].strip('"').replace(',',''))
    if row[idGDP] != '':
        row[idGDP] = row[idGDP].replace('"','').replace(',','').rstrip('\n')
    newrow = [row[idCountry], row[idDate], row[idPopulation], row[idMobile], row[idHealth], row[idInternet], row[idGDP]]
    firsteditrow.append(newrow)

# Exclude data that is missing
for row in firsteditrow:
    if '' in row:
        del row
    else:
        editrow.append(row)

for row in editrow:
    if row[6] == '':
        row[6] = int(0)
    elif row[6] != '':
        row[6] = int(row[6])
    if row[4] == '':
        row[4] = int(0)
    elif row[4] != '':
        row[4] = int(row[4])
    if row[5] == '':
        row[5] = int(0)
    elif row[5] != '':
        row[5] = int(row[5])
    if row[3] == '':
        row[3] = int(0)
    elif row[3] != '':
        row[3] = int(row[3])    #some data format cleaning regarding str and int

# ##output datasets that have the exact data we want left

#(c)
for row in editrow:
    MobileCapita = float(row[3])/row[2]
    row.append(MobileCapita)
# print "MobileCapita added",row[7]

for row in editrow:
    if row[6] != 0:
        GDPCapita = math.log(row[6])
        row.append(GDPCapita)
    if row[6] == 0:
        GDPCapita = 0
        row.append(GDPCapita)
# print "Capita added", row[8]

for row in editrow:
    if row[4] != 0:
        HealthLog = math.log(row[4])
        row.append(HealthLog)
    if row[4] == 0:
        HealthLog = 0
        row.append(HealthLog)
# print "HealthLog added", row[9]


#(d) # formatting the decimal
for num in (7,8,9):
    for row in editrow:
        if row[num] != 0:
            row[num] = '{0:5f}'.format(row[num])

input_file.close()

###########################################   Step 2

input_file = open('world_bank_regions.txt','rU')
# use dictionary structure for look up
Regions = {} #setting up an empty dictionary for loop up
header = (input_file.readline()).split('\t')
for line in input_file:
    entries = line.split('\t')
    for num in (0,2):
        entries[2] = entries[2].rstrip('\n')
        Regions[entries[2]] = entries[0]

RegionKey = []
RegionDict = []
for value in Regions.iteritems():
    RegionDict.append(value)
for dict in RegionDict:
    RegionKey.append(dict[0])


# adding regions into the editrow, change data structure and get ready for sorting
neweditrow=[]
index = -1
for row in editrow:
    index += 1
    if row[0] in RegionKey:
        for key in RegionKey:
            if row[0] == key:
                row.append(Regions[key])
                neweditrow.append(row)  #only include countries data that could match with the region file

row = ()
sortrow = []
for rows in neweditrow:
    row = tuple(rows)
    sortrow.append(row)
sortrow.sort(key=itemgetter(1,10,8))
#Sort by asceding year, region, GDP per Capita)


###################################  Step 6   Output into CSV file

outfile = open('worldbank_output_junhui.csv', 'w')
outfile.write('Country Name,Date,Total Population,Mobile subscribers,Health:mortality under-5,Internet users per 100 people,GDP per capita,Mobile subscribers per capita,log(GDP per capita),log(Health:mortality under-5),Region\n')


for row in sortrow:
    outfile.write(row[0]+','+row[1]+','+str(row[2])+','+str(row[3])+','+str(row[4])+','+str(row[5])+','+str(row[6])+','+str(row[7])+','+str(row[8])+','+str(row[9])+','+row[10]+'\n')
outfile.close()














