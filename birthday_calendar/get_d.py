from birthday_calendar import Gsheets


d = Gsheets("1UNJKsafMjayXP4UfxFYWjq6Tgsn0USHR-bWpuFL9CYI")

s = d.get_data_from_sheet("LIST OF EMPLOYEES", "A1:K")

ids_and_dates = []
if s[0][10] == "Date of birth":
    for n in s:
        try:
            ids_and_dates.append([n[1], n[10]])
        except IndexError as e:
            print(e)

    print(ids_and_dates)

