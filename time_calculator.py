DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_day_str(actual_day, day):
    if len(actual_day) == 0: return ''

    index = list(map(lambda d: d.lower(), DAYS)).index(actual_day.lower())
    index = (index+day) % 7

    return ', ' + DAYS[index]

def get_day_later_str(days_nb):
    if days_nb == 0: return ''
    if days_nb == 1: return ' (next day)'
    else: return ' ({} days later)'.format(days_nb)

def hours_format_to_24(hours, meridiem):
    if meridiem == 'AM':
        if hours == 12: return 0
        return hours
    else:
        if hours == 12: return 12
        return hours + 12

def hours_format_to_12(hours):
    if hours in (0, 12): return 12
    return hours%12

def get_meridiem(hours):
    if hours > 11: return 'PM'
    return 'AM'

def add_time(start, duration, actual_day = ''):
    days_nb = 0
    meridiem = start.split(' ')[1]
    hours = hours_format_to_24(int(start.split(':')[0]), meridiem)
    minutes = int(start.split(' ')[0].split(':')[1])

    hours_to_add = int(duration.split(':')[0])
    minutes_to_add = int(duration.split(':')[1])

    minutes += minutes_to_add
    if minutes > 59:
        hours += 1
        minutes -= 60

    hours += hours_to_add
    if hours > 23:
        days_nb = hours//24
        hours = hours%24

    return '{}:{} {}{}{}'.format(
        str(hours_format_to_12(hours)),
        str(minutes).zfill(2),
        get_meridiem(hours),
        get_day_str(actual_day, days_nb),
        get_day_later_str(days_nb)
    )
