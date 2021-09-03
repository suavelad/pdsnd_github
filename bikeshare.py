import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = str(input("Enter your city: ")).lower()
    while city not in ['chicago','new york city','washington']:
        print('selected city not in the list, try again please :' )
        city = str(input("Enter your city: ")).lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input ( "Enter month of the year: ")).lower()
    while month not in ['all','january','february','march', 'april', 'may','june', 'july','august','september','october','november','december','all']:
        print('selected month is not valid, try again please :' )
        month = str(input ( "Enter month of the year: ")).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day= str(input ("Enter the day of the week :")).lower()
    while day not in ['all','monday','tuesday','wednesday', 'thursday', 'friday','saturday', 'sunday','all']:
        print('selected day is  not valid, try again please  :' )
        day= str(input ("Enter the day of the week :")).lower()


    print('-'*40)
    print (city, month, day)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    try:
        if month !=day !='all':
            count = 0
            df = pd.read_csv(CITY_DATA[city])
            response = str(input('Do you want to see the next 5 raw data ')).lower()
            while response != 'yes':
                response = str(input('Do you want to see the next 5 raw data ')).lower()
            df.head(5)    

            df['Start Time'] = pd.to_datetime(df['Start Time'])
            df['month'] = df['Start Time'].dt.month
            df['day'] = df['Start Time'].dt.day
            return df
        else:
            return 'you need to select a specific day of the week  and month '
    except:
        return 'It seems a column you are trying to access is not available on this dataframe'


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    try:
        # TO DO: display the most common month
        most_common_month = df['month'].mode()[0]
        print('most common month: ', most_common_month)



        # TO DO: display the most common day of week
        most_common_day  = df['day'].mode()[0]
        print('most common day', most_common_day)

        # TO DO: display the most common start hour
        most_hour = df['Start Time'].dt.hour.mode()[0]
        print('most_hour: ', most_hour)


    except:
        return 'It seems a column you are trying to access is not available on this dataframe'

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    try:
        # TO DO: display most commonly used start station
        most_used_start_station = df['Start Station'].mode()[0]
        print('most used start station: ', most_used_start_station)

        # TO DO: display most commonly used end station
        most_used_end_station = df['End Station'].mode()[0]
        print('most used end station: ', most_used_end_station)

        # TO DO: display most frequent combination of start station and end station trip
        most_used_start_end_station = (df['Start Station'] +df['End Station']).mode()[0]
        print ('most used start and end station combined: ', most_used_start_end_station)

    except:
      return 'It seems a column you are trying to access is not available on this dataframe'      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    try:
        # TO DO: display total travel time
        total_trip_time = df['Trip Duration'].sum()
        print('total_trips: ',total_trip_time )

        # TO DO: display mean travel time
        mean_trip_time = df['Trip Duration'].mean()
        print('the mean: ', mean_trip_time)
    
    except:
        return 'It seems a column you are trying to access is not available on this dataframe'
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        # TO DO: Display counts of user types
        user_type_count = df['User Type'].value_counts()
        print ('user type count: ', user_type_count)

        # TO DO: Display counts of gender
        user_gender = df['Gender'].value_counts()
        print ('user gender: ', user_gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        df = df.sort_values('Birth Year', axis=0, ascending=True, inplace=False).dropna()
        earliest = df['Birth Year'].iloc[0]
        recent = df['Birth Year'].iloc[-1]
        most_common_year = df['Birth Year'].mode()[0]
        print ('early: ', earliest)
        print ('recent: ',recent)
        print ('common', most_common_year)

    except:
        return 'It seems a column you are trying to access is not available on this dataframe'    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()