import datetime

# Represents the amount of seconds that Terrestrial Time is currently ahead of Universal Time
terrestrialTimeOffset = 32.184

def getMarsTime(currentTime):
    print("Test")

def getJulianDate(currentDate):
    dateTimeStamp = currentDate.timestamp()
    julianDate = (dateTimeStamp / 86400) + 2440587.5
    return julianDate

def getMarsDate(currentDate):
    julianDate = getJulianDate(currentDate)
    marsSolDate = (julianDate + terrestrialTimeOffset/86400 - 2405522.0025054) / 1.0274912517
    return marsSolDate

def main():
    # currentDate = datetime.datetime(2020, 9, 17,0,0,0)
    # currentTime = currentDate.time
    # print(currentDate)
    # currentTime
    # print(getMarsDate())
    testDate = datetime.datetime(2020, 12, 23, 22, 8, 27)
    print(testDate.year)
    print("Julian Date: {0}, Mars Date: {1}".format(getJulianDate(testDate), getMarsDate(testDate)))
main()