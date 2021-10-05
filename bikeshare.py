import time
import pandas as pd
import numpy as np

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}


def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hey there! Looks like you're interested in bikeshare data for some American states! \n")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        city = input("What city's data are you interested in; chicago, new york city or washington? \nplease select one - \n"
        ).lower()
        if city == "chicago" or city == "new york city" or city == "washington":
            print("---You have selected {}\n".format(city))
            break
        else:
            print("Wrong Option! Please select one of the three cities only\n")
    while True:
        time = input("Do you want to filter the data? \nYes or No - \n").lower()
        if time == "no":
            month = "all"
            day = "all"
            print("---Alright then, no filters \n")
            break
        elif time == "yes":
            time = input("Do you want to filter by month, day or both - \n").lower()
            if time == "month":
                month = input("What month do you want data for? January, February, March, April, May, or June \nplease select one - \n").lower()
                day = "all"
                print("--- You have filtered by {}\n".format(month))
                break
            elif time == "day":
                month = "all"
                day = input("What day of the week are you interested in? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday \nplease select one - \n").lower()
                print("--- You have filtered by {}\n".format(day))
                break
            elif time == "both":
                month = input(
                    "What month do you want data for? January, February, March, April, May, or June \nplease select one - \n"
                ).lower()
                day = input(
                    "What day of the week are you interested in? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday \nplease select one - \n"
                ).lower()
                print("--- You have  filtered by {} and {}\n".format(month, day))
                break
            else:
                input("Wrong Option! Please select one of the listed options only")
                break
        else:
            time = input(
                "Wrong Option! Please select one of the listed options only \nDo you want to filter the data? \nYes or No - \n"
            ).lower()
            continue
    print("Your option choices are as follows: \nCity - {}, \nMonth - {}, \nDay - {}".format(city, month, day))

    print("-" * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        bikeshare_data - Pandas DataFrame containing city data filtered by month and day
    """
    bikeshare_data = pd.read_csv(CITY_DATA[city])
    bikeshare_data["Start Time"] = pd.to_datetime(bikeshare_data["Start Time"])
    bikeshare_data["month"] = bikeshare_data["Start Time"].dt.month
    bikeshare_data["day_of_week"] = bikeshare_data["Start Time"].dt.day_name()

    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        bikeshare_data = bikeshare_data[bikeshare_data["month"] == month]
    if day != "all":
        bikeshare_data = bikeshare_data[bikeshare_data["day_of_week"] == day.title()]
    return bikeshare_data


def time_stats(bikeshare_data):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # display the most common month
    # display the most common day of week
    # display the most common start hour

    common_month = bikeshare_data["month"].mode()[0]
    print("The most common month is {}".format(common_month))

    common_day_of_week = bikeshare_data["day_of_week"].mode()[0]
    print("The most common day of week is {}".format(common_day_of_week))

    bikeshare_data["hour"] = bikeshare_data["Start Time"].dt.hour
    common_hour = bikeshare_data["hour"].mode()[0]
    print("The most common start hour is {}".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(bikeshare_data):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station
    # display most commonly used end station
    # display most frequent combination of start station and end station trip

    most_popular_start = bikeshare_data["Start Station"].mode()[0]
    print("The most commonly used start station is {}".format(most_popular_start))

    most_popular_end = bikeshare_data["End Station"].mode()[0]
    print("The most commonly used end station is {}".format(most_popular_end))

    bikeshare_data["popular_combination"] = (
        "From "
        + bikeshare_data["Start Station"]
        + " to "
        + bikeshare_data["End Station"]
    )
    most_popular_combination = bikeshare_data["popular_combination"].mode()[0]
    print(
        "The most frequent combination of start and end station is {}".format(
            most_popular_combination
        )
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(bikeshare_data):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time
    # display mean travel time

    total_travel_time = bikeshare_data["Trip Duration"].sum()
    print("The total travel time is {}".format(total_travel_time))

    mean_travel_time = bikeshare_data["Trip Duration"].mean()
    print("Mean travel time is {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(bikeshare_data):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types
    # Display counts of gender
    # Display earliest, most recent, and most common year of birth

    user_types = bikeshare_data["User Type"].value_counts()
    print(user_types)

    if "Gender" in bikeshare_data:
        gender = bikeshare_data["Gender"].value_counts()
        print(gender)
    else:
        print("Sorry, Not Applicable here.")
    if "Birth_Year" in bikeshare_data:
        earliest_birth = bikeshare_data["Birth_Year"].min()
        print(earliest_birth)
        most_recent_birth = bikeshare_data["Birth_Year"].max()
        print(most_recent_birth)
        most_common_birth = bikeshare_data["Birth Year"].mode()[0]
        print(most_common_birth)
    else:
        print("Sorry, Not Applicable here.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def view_raw_data(bikeshare_data):
    """
    Ask if user wants to view raw data
    Returns 5 rows of the table per time
    """

    print(bikeshare_data.head())
    raw_data_loc = 0
    while True:
        user_choice = input(
            "Hello there! Do you want to see the raw data? \nYes or No - "
        ).lower()
        if user_choice == "yes":
            raw_data_loc += 5
            print(bikeshare_data.iloc[raw_data_loc : raw_data_loc + 5])
            follow_up = input(
                "Do you want to see more rows of raw data? Yes or No - "
            ).lower()
            if follow_up == "no":
                break
        elif user_choice == "no":
            return


def main():
    city = ""
    month = ""
    day = ""
    while True:
        city, month, day = get_filters(city, month, day)
        bikeshare_data = load_data(city, month, day)

        time_stats(bikeshare_data)
        station_stats(bikeshare_data)
        trip_duration_stats(bikeshare_data)
        user_stats(bikeshare_data)
        view_raw_data(bikeshare_data)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()
