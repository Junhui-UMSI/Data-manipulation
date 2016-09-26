import re
import datetime
input_file = open('access_log.txt','rU')
outfile1 = open('valid_log_summary_junhui.txt', 'w')
outfile2 = open('invalid_access_log_junhui.txt', 'w')

def valid(line):
    match = re.match(r'(\d+.\d+.\d+.\d+).*?[\s]+"(GET|POST)\s*(.*).*?"[\s]+(\d+)', line)  #strping out the parts inside the log and filtering on the GET/POST
    if match:
        ip = match.group(1)
        verb = match.group(2)
        url = match.group(3)
        statuscode = match.group(4)
        if ((verb == "GET")|(verb == "POST")):
            if(statuscode == '200'):
                match = re.match(r'https?://([A-Za-z]+)(.*?)[.]([A-Za-z]+)/|https?://([A-Za-z]+)(.*?)[.]([A-Za-z]+):|https?://([A-Za-z]+).*?[.]([A-Za-z]+)\s+HTTP/', url)  #top level domain search and URL
                if match:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


for line in input_file:
    if valid(line):
        outfile1.write(line)
    else:
        outfile2.write(line)

input_file.close()
outfile1.close()
outfile2.close()

input_file = open('valid_log_summary_junhui.txt', 'rU')

def get_date(line):
	match = re.search(r'\[(.+?)\:', line)
	date = match.group(1)
	return date

def get_topdomian(line):
    searchmatch = re.match(r'(\d+.\d+.\d+.\d+).*?[\s]+"(GET|POST)\s*(.*).*?"[\s]+(\d+)', line)
    url = searchmatch.group(3)
    match = re.match(r'https?://([A-Za-z]+)(.*?)[.]([A-Za-z]+)/|https?://([A-Za-z]+)(.*?)[.]([A-Za-z]+):|https?://([A-Za-z]+).*?[.]([A-Za-z]+)\s+HTTP/',url)
    if match.group(3):
        return match.group(3)
    elif match.group(6):
        return match.group(6)
    elif match.group(8):
        return match.group(8)

valid_list = []
for line in input_file:
    a = get_date(line)
    b = get_topdomian(line)
    b = b.lower()
    valid_list.append([a,b])

first_column_init = []
for item in valid_list:
    first_column_init.append(item[0])

first_column = []
for item in set(first_column_init):
    first_column.append(item)
    first_column.sort(key = lambda x: x.split('/')[0])

column_1 = []
column_2 = []
column_3 = []
column_4 = []
column_5 = []
column_6 = []

for item in valid_list:
    if item[0] == first_column[0]:
        column_1.append(item[1])
    if item[0] == first_column[1]:
        column_2.append(item[1])
    if item[0] == first_column[2]:
        column_3.append(item[1])
    if item[0] == first_column[3]:
        column_4.append(item[1])
    if item[0] == first_column[4]:
        column_5.append(item[1])
    if item[0] == first_column[5]:
        column_6.append(item[1])

column_all = [column_1,column_2,column_3,column_4,column_5,column_6]


final_column_new = []
for column in column_all:
    final_column = {}
    for item in column:
        keys = final_column.keys()
        if item in keys:
            final_column[item] += 1
        else:
            final_column.update({item: 1})
    newcolumn = final_column
    final_column_new.append(newcolumn)

output_column = []
for item in first_column:
    output_column.append([item])

count = 0
for row in final_column_new:
    for key,value in row.iteritems():
        item = key+':'+str(value)
        output_column[count].append(item)
    count += 1

for row in output_column:  # sort
    row.sort()

input_file.close()


output_file = open('valid_log_summary_junhui.txt', 'w')
for row in output_column:
    for item in row:
        output_file.write(item+'\t')
    output_file.write('\n')
output_file.close()




