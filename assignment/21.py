t = [12,24,35,24,88,120,155,88,120,155]
print t
t1=list(set(t))
t1.sort(key=t.index) 
print "After removing duplicate:",t1
