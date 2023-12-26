def main():
    # Ask the user for time and call for the convert function
    time_ = input("What time is it? ")
    time = convert(time_)
    # breakfast from 7:00 to 8:00
    if time >= 7 and time <= 8:
        print("breakfast time")
    #lunch from 12:00 to 13:00
    elif time >= 12 and time <= 13:
        print("lunch time")
    #dinner from 18:00 to 19:00
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    # hours & minutes
    hours, minutes = time.split(":")
    # float number
    minutes_ = float(minutes)/60
    hours_ = float(hours)
    # result to main func
    return hours_ + minutes_

if __name__ == "__main__":
    main()