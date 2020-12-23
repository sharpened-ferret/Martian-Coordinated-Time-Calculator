import datetime

# Represents the amount of seconds that Terrestrial Time is currently ahead of Universal Time
terrestrialTimeOffset = 32.184 + 8

def getMarsTime(currentTime):
    solTimestamp = (getMarsDate(currentTime) * 24) % 24
    return datetime.timedelta(0,0,0,0,0,solTimestamp)
    return solTimestamp

def getJulianDateUT(currentDate):
    dateTimeStamp = currentDate.timestamp()
    julianDate = (dateTimeStamp / 86400) + 2440587.5
    return julianDate

def getJulianDateTT(currentDate):
    return getJulianDateUT(currentDate) + terrestrialTimeOffset/86400
    
def getMarsDate(currentDate):
    julianDateTT = getJulianDateTT(currentDate)
    marsSolDate = (julianDateTT - 2405522.0025054) / 1.0274912517
    return marsSolDate

def main():
    # testDate = datetime.datetime(2020, 12, 23, 22, 8, 27)
    testDate = datetime.datetime.now()
    print(testDate.year)
    print("Julian Date: {0}, Mars Date: {1}".format(getJulianDateTT(testDate), getMarsDate(testDate)))
    print("Current MTC: {0}".format(getMarsTime(testDate)))

main()