#eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00

def main():
    t = input(
        "What time is it?"
        ).strip(" ")
    time = convert(t)
    if 7 <= time <= 8:
        print("breakfast time")

    if 12 <= time <= 13:
        print("lunch time")

    if 18 <= time <= 19:
        print("dinner time")


def convert(time):
    h = float(time.split(":")[0])
    m = float(time.split(":")[1])
    return h + (m/60.0)


if __name__ == "__main__":
    main()
