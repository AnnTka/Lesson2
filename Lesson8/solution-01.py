def search_day():

    goal = int(input("Enter the task(km): "))
    mileage = int(input("Enter the mileage of the 1st day(km): "))
    day = 1

    while goal - mileage > 0:
        # every day the athlete increased the mileage by 10%:
        mileage += mileage/10
        day += 1
    return f"Congratulations! Mission completed. The day the goal was achieved - " + str(day) + "th day."


def main():
    task = search_day()
    print(task)


if __name__ == "__main__":
    main()
