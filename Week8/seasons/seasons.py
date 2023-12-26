from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    try:
        year,month,day=input('Date of Birth: ').split('-')
    except ValueError:
        sys.exit("Invalid Date")
    print(checkBirthDay(year,month,day))


def  checkBirthDay(year,month, day):
    variance = date.today() - date(int(year),int(month),int(day))
    minutes = int(variance.total_seconds() /60)
    try:
        result = p.number_to_words(minutes , andword="") + " minutes"
        return result.capitalize()
    except ValueError:
        sys.exit("Invalid Date")


if __name__ == "__main__":
    main()