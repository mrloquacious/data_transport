
bc = '['
for i in range(1,1000):
    if i != 999:
        #bc += '{ ' + str(i) + ' : "' + str(i) + '" },'
        bc += '"' + str(i) + '",'
    else:
        bc += '"' + str(i) + '"]'

f = open('bcsample.json', 'w+')
f.write(bc)
f.close()


