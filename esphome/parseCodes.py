import csv

with open('remoteCodes.csv', newline='') as csvfile:

    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader)
    print('button:')
    for row in reader:
        print(' - platform: template')
        print('   name: "' + row[0] + '"')
        print('   on_press:')
        print('    - remote_transmitter.transmit_nec:')
        print('        address: ' + row[1])
        print('        command: ' + row[2])
