def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    #replace() the dollar sign
    d1 = d.replace("$", " ")
    #d1 became float + return to d1
    return float(d1)

def percent_to_float(p):
    # TODO
    #replace() the percent signt
    p1 = p.replace("%"," ")
    # coverted whithout percent & p1 became float
    p2 = float(p1)/100
    return p2


main()