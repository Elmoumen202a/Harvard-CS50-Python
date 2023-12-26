# creat list
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# creat main function
def main():
    #loop forever
    while True:
        # ask the users
        user_input = input('Date: ')
        try:
            #month = m , day= d, year= y
            # split the date
            m,d,y = user_input.split('/')
           # m = int(m)
            #d = int(d)
            # check the months and days
            y = int(y)
            if (int (m) > 0 and int(m) < 13) and (int(d) > 0 and int(d) < 32):
                if y >= 1000 and y <= 9999:
                    # print output
                    print(f"{y}-{int(m):02}-{int(d):02}")
                    break
        except:
            try:
                # check comma in input
                if "," in user_input:
                    # split
                    m,d,y = user_input.split(' ')
                    # replace comma with space
                    d = d.replace(',','')
                    #d = int(d)
                    y = int(y)
                    # check
                    if m in months and (int(d) > 0 and int(d) < 32):
                        if y >= 1000 and y <= 9999:
                            m= (months.index (m)+1)
                            #print outot
                            print(f"{y}-{int(m):02}-{int(d):02}")
                            break
            except:
                pass

main()