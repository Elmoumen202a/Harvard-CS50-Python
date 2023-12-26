def main():
    while True:
        try:
            fraction = str(input("Fraction: ").strip())
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError, UnboundLocalError):
            continue

def convert(fraction):

    if "/" in fraction:
        x, y = fraction.split("/", 1)
    else:
        raise UnboundLocalError("Not a valid fraction.")

    if x.isdigit() and y.isdigit():
        if int(x) <= int(y) and int(y) != 0:
            percentage = (int(x) / int(y)) * 100
            return percentage
        else:
            raise ZeroDivisionError("X is larger than Y")
    else:
        raise ValueError("Not an integer")

def gauge(percentage):
    if int(percentage) >= 99:
        return "F"
    elif int(percentage) < 99 and int(percentage) > 1:
        return f"{percentage:.0f}%"
    else:
        return "E"

if __name__ == "__main__":
    main()