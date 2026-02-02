def main():
    date()


def date():
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
    while True:
        date = input("Date: ").strip()
        try:
            if "/" in date:
                month, day, year = date.split("/")
                if int(day) <= 31 and int(month) <= 12:
                    print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
                    break
                else:
                    raise Exception()
            elif "," in date:
                parts = date.replace(",", "").split(" ")
                month_name, day, year = parts
                if month_name in months:
                    month = months.index(month_name) + 1
                    if int(day) <= 31:
                        print(f"{year}-{str(month).zfill(2)}-{day.zfill(2)}")
                        break
                    else:
                        raise Exception()
                else:
                    raise Exception()
        except:
            pass



main()    