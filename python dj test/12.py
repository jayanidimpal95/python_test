import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG, filename='12.log')
logging.info('Started')
list=[ 6, 6, 12, 19, 30]

i=0
f=0
for i in range(len(list)-2):
    f=0
    c=list[i]+list[i+1]
    if(c!=list[i+2]):
        f=1
        logging.info('breaking condition in additive sequence')
        break
if(f==0):
    logging.info('yes additive sequence')
    print "yes additive sequence"
else:
    logging.info('not additive sequence')
    print "not additive sequence"
logging.info('Finished')
