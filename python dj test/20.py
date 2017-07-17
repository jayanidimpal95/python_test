import collections
str1 = raw_input("Enter the string:")
list=str1.split(" ")
dict = {}
for n in list:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
od=collections.OrderedDict(sorted(dict.items()))

for k, v in od.iteritems():
    print k,":", v
