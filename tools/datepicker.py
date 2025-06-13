import datetime

class DateSelector:
    
    def __init__(self):
         pass

    def getTodayDate():
        return datetime.datetime.now()

    def getOneWeekFromToday():
        today = DateSelector.getTodayDate()
        return today + datetime.timedelta(days=7)
    
    def formatDate(dateToFormat):
        return (str(dateToFormat.day) + " " + dateToFormat.strftime("%B") + " " + str(dateToFormat.year) + ", " + dateToFormat.strftime("%A"))
    
    def formatShortDate(dateToFormat):
        return (dateToFormat.strftime("%b") + " " + str(dateToFormat.day))
