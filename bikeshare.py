import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ["january", "february", "march", "april", "may", "june"]    
days = ["sunday", "monday", "tuesday", "wednsday", "thursday", "friday", "saturday"]          

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
    while True:
        global city
        city = input("Which city would you like to see it's data? Chicago, New York City, Washington?\n").lower()
        if city not in("chicago", "new york city", "washington"):
            print("Please enter a valid city.")
        else:
            break



    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        global month
        month = input("Which month would you like to see it's data or All months? all, Jan., Feb., ...?\n").lower()
        if month not in months and month != "all":
            print("Please enter a valid month.")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        global day
        day = input("Which day would you like to see it's data or All days? all, sun., mon., ...?\n").lower()
        if day not in days and day != "all":
            print("Please enter a valid day.")
        else:
            break


    print('-'*40)
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
    global df
    df = pd.read_csv(CITY_DATA[city])


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    global month
    if month == "all":
        common_month = df['month'].mode()[0]
        print("most common month: ", common_month)
    else: 
        month = month.index(month) + 1
        df = df[df["month"] == month]
        print("the common month: ", month)


    # TO DO: display the most common day of week
    global day
    if day == "all":
        common_day = df['day_of_week'].mode()[0]
        print("most common day: ", common_day)
    else: 
        df = df[df["day_of_week"] == day.title()]
        
        print("the common day of week: ", day.title())


    # TO DO: display the most common start hour

    common_hour = df["hour"].mode()[0]
    print("most common start hour: ", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_common_start_station = df["start station"].mode()[0]
    print("most used start station: ", most_common_start_station)


    # TO DO: display most commonly used end station

    most_used_end_station = df["end station"].mode()[0]
    print("most used end station: ", most_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    most_combination_stations = df.groupby(["start station", "end station"]).size().sort_values().index[0]
    most_combination_start_end_stations = "/ ".join(most_combination_stations)
    print("most combination of start station and end station: ", most_combination_start_end_stations)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df["trip duration"].sum() / (60*60)
    print("the total travel time: ", total_time)


    # TO DO: display mean travel time
    mean_time = df["trip duration"].mean() / 60
    print("mean travel time:", mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("counts of user types: ", user_types)


    # TO DO: Display counts of gender
    if city.lower() == "chicago" or city.lower() == "new york city":
        gender = df["gender"].value_counts()
        print("counts of gender: ", gender)


    # TO DO: Display earliest, most recent, and most common year of birth

    if city.lower() == "chicago" or city.lower == "new york city":
        earliest_birth_year = df["birth year"].min()
        print("earliest year of birth is: ", earliest_birth_year)
        most_recent_birth_year = df["birth year"].max()
        print("most recent year of birth is: ", most_recent_birth_year)
        most_common_birth_year = df["birth year"].mode()[0]
        print("most common year of birth is: ", most_common_birth_year)


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

        count = 0
        raw_data = input("would you like to see more results? Enter yes or no \n")
        while True:
            if raw_data.lower() == "yes":
                count += 1
                print(df.head(5*count))
                raw_data = input("would you like to see more data? yes or no? \n")
            else: 
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
