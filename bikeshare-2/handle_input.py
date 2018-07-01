CITY_LIST = ['chicago', 'new york city', 'washington']
FILTER_LIST = ['month', 'day', 'both', 'none']
MONTH_LIST = ['january', 'february', 'march', 'april', 'may', 'june']
DAY_LIST = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']


def handle_city_input():
    """
    Asks user to specify a city to analyze.

    Returns:
         (str) city - name of the city to analyze
    """
    city = input('Would you like to see data for Chicago, New York City or Washington?\n')
    city = city.strip()

    if check_valid_city(city):
        print('Awesome! You have chosen {}\n'.format(city))
    else:
        while True:
            city = input('\nOops! Please choose valid city Chicago, New York City or Washington\n')

            if check_valid_city(city):
                print('Awesome! You have chosen {}\n'.format(city))
                break

    return city.lower()


def handle_filter_input():
    """
    Asks user to filter by month, day, both or not at all. Type 'none' for no time filter.

    Returns:
         (str) filter_input - name of the filter
    """
    filter_input = input('Would you like to filter the data by month, day, both or not at all. '
                         'Type \'none\' for no time filter.?\n')
    filter_input = filter_input.strip()

    if check_valid_filter(filter_input):
        print('Awesome! You have chosen to filter by {}\n'.format(filter_input))
    else:
        while True:
            filter_input = input('\nOops! Please choose valid filter month, day, both or none\n')

            if check_valid_filter(filter_input):
                print('Awesome! You have chosen to filter by {}\n'.format(filter_input))
                break

    return filter_input.lower()


def handle_month_input():
    """
    Asks user to specify a month to analyze.

    Returns:
         (str) month - name of the month to analyze
    """
    month = input('Which month? January, February, March, April, May or June? Please fill out full month name\n')
    month = month.strip()

    if check_valid_month(month):
        print('Awesome! You have chosen {}\n'.format(month))
    else:
        while True:
            month = input('\nOops! Please choose valid month January, February, March, April, May or June?'
                          ' Please fill out full month name\n')

            if check_valid_month(month):
                print('Awesome! You have chosen {}\n'.format(month))
                break

    return month.lower()


def handle_day_input():
    """
    Asks user to specify a day to analyze.

    Returns:
         (str) day - name of the day to analyze
    """
    day = input('Which Day? Sunday, Monday, Tuesday, Wednesday, '
                'Thursday, Friday or Saturday? Please fill out full day name\n')
    day = day.strip()

    if check_valid_day(day):
        print('Awesome! You have chosen {}\n'.format(day))
    else:
        while True:
            day = input('\nOops! Please choose valid day Sunday, Monday, Tuesday, '
                        'Wednesday, Thursday, Friday or Saturday. Please fill out full day name\n')

            if check_valid_day(day):
                print('Awesome! You have chosen {}\n'.format(day))
                break

    return day.lower()


def check_valid_city(city):
    """
    Check for valid city input

    Args:
        (str) city - name of the city to analyze

    Returns:
        (bool) - True/False
    """
    if city == '':
        return False
    else:
        city = city.lower()

        if CITY_LIST.__contains__(city):
            return True
        else:
            return False


def check_valid_filter(filter_input):
    """
    Check for valid filter input

    Args:
        (str) filter_input - name of the filter to analyze

    Returns:
        (bool) - True/False
    """
    if filter_input == '':
        return False
    else:
        filter_input = filter_input.lower()

        if FILTER_LIST.__contains__(filter_input):
            return True
        else:
            return False


def check_valid_month(month):
    """
    Check for valid month input

    Args:
        (str) month - name of the month to analyze

    Returns:
        (bool) - True/False
    """
    if month == '':
        return False
    else:
        month = month.lower()

        if MONTH_LIST.__contains__(month):
            return True
        else:
            return False


def check_valid_day(day):
    """
    Check for valid day input

    Args:
        (str) day - name of the day to analyze

    Returns:
        (bool) - True/False
    """
    if day == '':
        return False
    else:
        day = day.lower()

        if DAY_LIST.__contains__(day):
            return True
        else:
            return False
