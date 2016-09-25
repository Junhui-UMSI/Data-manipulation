print "hello world!"

s = " one  s "
print type(s)

for i in range(3, 20, +2):
    print i;

def stripone(s):
    s = s.strip(' ')
    print s
    return;
print(s)
stripone(s)
print s.isdigit()