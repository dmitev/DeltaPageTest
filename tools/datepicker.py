import datetime

class DateSelector:

    def get_today_date():
        """Get today's date"""
        return datetime.datetime.now()

    def get_one_week_from_today():
        """Get a day a week from today"""
        today = DateSelector.get_today_date()
        return today + datetime.timedelta(days=7)
    
    def format_date(date_to_format: datetime):
        """
        Formats a date for the seach of a round trip flight
        Paremeters
        date_to_format : datetime
            date to be formatted
        """ 
        return (str(date_to_format.day) + " " + date_to_format.strftime("%B") + " " + str(date_to_format.year) + ", " + date_to_format.strftime("%A"))
    
    def format_short_date(date_to_format: datetime):
        """
        Closes the GDPR screen
        Paremeters
        date_to_format : datetime
            date to be formatted
        """ 
        return (date_to_format.strftime("%b") + " " + str(date_to_format.day))
