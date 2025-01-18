def main():
    string = input("Time: ").strip()

    main_time = convert(string)

    if main_time >= 7.0 and main_time <= 8.0:
        print("Breakfast time")
    elif main_time >= 12.0 and main_time <= 13.0:
        print("Lunch time")
    elif main_time >= 18.0 and main_time <= 19.0:
        print("Dinner time")



def convert(time):
    hour, minute = map(int, time.split(":"))
    
    if 0 <= hour < 24 and 0 <= minute < 60:
        return hour + minute / 60
    else:
        return None

if __name__ == "__main__":
    main()
