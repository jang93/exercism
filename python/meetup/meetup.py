import datetime
import calendar


WEEK_TO_FIRST_DATE_OF_WEEK_MAP = {
    '1st': 1,
    '2nd': 8,
    '3rd': 15,
    '4th': 22,
    '5th': 29,
    'last': 25,
    'teenth': 13
}


DAY_OF_WEEK_STRING_TO_NUM_MAP = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}

class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):
    days_in_month = calendar.monthrange(year, month)[1]
    first_date_of_week = WEEK_TO_FIRST_DATE_OF_WEEK_MAP[week]
    given_day_of_week_num = DAY_OF_WEEK_STRING_TO_NUM_MAP[day_of_week]
    if week == 'last':
        first_date_of_week -= (31 - days_in_month)
    if first_date_of_week > days_in_month:
        raise MeetupDayException('Error: No such possible meetup date')
    meetup_date = datetime.date(year, month, first_date_of_week)
    day_num = meetup_date.weekday()
    meetup_date_day = first_date_of_week + (given_day_of_week_num - day_num) % 7
    if meetup_date_day > days_in_month:
        raise MeetupDayException('Error: No such possible meetup date')
    print(meetup_date_day)
    week = meetup_date.replace(day=(meetup_date_day))
    return week


