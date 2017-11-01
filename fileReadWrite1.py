__author__ = 'Arana Fireheart'

lowestLow = 200
lowestLowYear = 0
highestHigh = -200
highestHighYear = 0
try:
    with open('testfile1.txt', 'r') as testFileHandle:
        header = testFileHandle.readline()
        for line in testFileHandle.readlines():
            temperatures = line.strip().split('\t')
            recordLow = temperatures[3]
            recordLowTemp, recordLowYear = recordLow.split()
            recordLowTemp = int(recordLowTemp[:-1])
            recordLowYear = int(recordLowYear[1:-1])
            if recordLowTemp < lowestLow:
                lowestLow = recordLowTemp
                lowestLowYear = recordLowYear
            recordHigh = temperatures[4]
            recordHighTemp, recordHighYear = recordHigh.split()
            recordHighTemp = int(recordHighTemp[:-1])
            recordHighYear = int(recordHighYear[1:-1])
            if recordHighTemp > highestHigh:
                highestHigh = recordHighTemp
                highestHighYear = recordHighYear
        print("Lowest Temp: {0} Year: {1} Highest Temp: {2} Year: {3}".format(lowestLow, lowestLowYear, highestHigh, highestHighYear))
except FileNotFoundError:
    print("ERROR: Filename incorrect")