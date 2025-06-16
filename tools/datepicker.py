import datetime

class DateSelector:
    
    def __init__(self):
         pass

    def getTodayDate():
        """Get today's date"""
        return datetime.datetime.now()

    def getOneWeekFromToday():
        """Get a day a week from today"""
        today = DateSelector.getTodayDate()
        return today + datetime.timedelta(days=7)
    
    def formatDate(dateToFormat: datetime):
        """
        Formats a date for the seach of a round trip flight
        Paremeters
        dateToFormat : datetime
            date to be formatted
        """ 
        return (str(dateToFormat.day) + " " + dateToFormat.strftime("%B") + " " + str(dateToFormat.year) + ", " + dateToFormat.strftime("%A"))
    
    def formatShortDate(dateToFormat: datetime):
        """
        Closes the GDPR screen
        Paremeters
        dateToFormat : datetime
            date to be formatted
        """ 
        return (dateToFormat.strftime("%b") + " " + str(dateToFormat.day))
