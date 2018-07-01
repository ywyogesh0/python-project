import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

CITY_LIST = ['chicago', 'new york city', 'washington']
FILTER_LIST = ['month', 'day', 'both', 'none']
MONTH_LIST = ['january', 'february', 'march', 'april', 'may', 'june']
DAY_LIST = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "None" to apply no month filter
        (str) day - name of the day of week to filter by, or "None" to apply no day filter
    """
    print(
        '\nHello! Let\'s explore some US bikeshare data!\n\n--- All inputs will be considered as case in-sensitive!\n')

    # get user input for city (chicago, new york city, washington)
    city = handle_city_input()

    # get user input to filter by month, day, both or not at all. Type 'none' for no time filter
    filter_input = handle_filter_input()

    if filter_input == 'both':
        month, day = handle_month_input(), handle_day_input()
    elif filter_input == 'month':
        month, day = handle_month_input(), None
    elif filter_input == 'day':
        day, month = handle_day_input(), None
    elif filter_input == 'none':
        month, day = None, None

    print('-' * 40)
    return city, month, day


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


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "None" to apply no month filter
        (str) day - name of the day of week to filter by, or "None" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    create_month_hour_and_day_of_week_columns(df)

    if month is None and day is None:
        return df

    elif month is not None and day is None:
        return filter_df_by_month(df, month)

    elif day is not None and month is None:
        return filter_df_by_day(df, day)

    else:
        return filter_df_by_month_and_day(df, month, day)


def create_month_hour_and_day_of_week_columns(df):
    """Create month, hour and day_of_week columns to analyze.

    Args:
        df - Pandas DataFrame containing city data
    """
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    return df


def filter_df_by_month(df, month):
    """Filter by month.

    Args:
        (str) month - month by which Pandas DataFrame will be filtered
        df - Pandas DataFrame containing city data
    """
    return df[df['month'] == MONTH_LIST.index(month) + 1]


def filter_df_by_day(df, day):
    """Filter by day.

    Args:
        (str) day - day by which Pandas DataFrame will be filtered
        df - Pandas DataFrame containing city data
    """
    return df[df['day_of_week'] == day.title()]


def filter_df_by_month_and_day(df, month, day):
    """Filter by month and day both.

    Args:
        (str) month - month by which Pandas DataFrame will be filtered
        (str) day - day by which Pandas DataFrame will be filtered
        df - Pandas DataFrame containing city data
    """
    df = df[df['month'] == MONTH_LIST.index(month) + 1]
    df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('What is the most popular month for travelling?')
    popular_month_number = df['month'].mode()[0]
    print(MONTH_LIST[popular_month_number - 1].title())

    # display the most common day of week
    print('\nWhat is the most popular day for travelling?')
    print(df['day_of_week'].mode()[0])

    # display the most common start hour
    print('\nWhat is the most popular hour of the day to start your travels?')
    print(df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('What is the most popular start station for travelling?')
    print(df.groupby(['Start Station']).size().nlargest(1))

    # display most commonly used end station
    print('\nWhat is the most popular end station for travelling?')
    print(df.groupby(['End Station']).size().nlargest(1))

    # display most frequent combination of start station and end station trip
    print('\nWhat is the most popular start and end station trip for travelling?')
    print(df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('What was the total travelling done for 2017 through June?')
    print('Timedelta(\'{}\')'.format(pd.Timedelta(seconds=np.sum(df['Trip Duration']))))

    # display mean travel time
    print('\nWhat was the average time spent on each trip?')
    print('Timedelta(\'{}\')'.format(pd.Timedelta(seconds=np.mean(df['Trip Duration']))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("What is the breakdown of users?\n")
    print(df['User Type'].value_counts())
    print('\n')

    if 'Gender' in df.columns:
        # Display counts of gender
        print("What is the breakdown of gender?\n")
        print(df['Gender'].value_counts())
        print('\n')
    else:
        print('No breakdown of gender...')

    if 'Birth Year' in df.columns:
        # Display oldest, latest, and most common year of birth
        print("What is the oldest, latest and most common year of birth, respectively?\n")
        oldest = np.min(df['Birth Year'])
        latest = np.max(df['Birth Year'])
        common = df['Birth Year'].mode()[0]
        print('({}, {}, {})'.format(oldest, latest, common))
    else:
        print('\nNo stats of birth year...')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()

        print('\nPlease wait. Loading Data...\n')
        print('Applying Filters...')
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter \'yes\' or any other character for \'no\'.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
