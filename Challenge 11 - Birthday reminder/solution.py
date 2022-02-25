import datetime  # USE RELATIVEDELTA
# from dateutil.relativedelta import    relativedelta  # this allows years, months and weeks (weeks as days*7) but is not allowed in the contest
# pandas also has a tool for months, but again pandas is not allowed
import re
from calendar import \
    monthrange  # allows to count the days in a month, which can be useful https://techoverflow.net/2019/05/16/how-to-get-number-of-days-in-month-in-python/


class Calendar:
    def get_repeating_event(self, starting_date, repeat_instruction):
        # Your code goes here
        date = datetime.datetime.strptime(starting_date, "%Y/%m/%d")
        units = "day|week|month|year"
        # pattern = "\s*every\s+\d+\s+"+units+"s?"#may change the pattern if I need to be more strict, to make it end like that end add $
        pattern = "every\s\d+\s(" + units + ")s?$"
        if re.match(pattern, repeat_instruction):
            repeat = repeat_instruction.split()
            amount = int(repeat[1])
            if amount == 0 or amount >= 100:
                return []
            unit = repeat[2]  # if repeat[2][-1]=="s" else repeat[2]+"s"
            if unit.startswith("day"):
                reps = self.add_days(date, amount)
                repetitions = [starting_date] + reps
                return repetitions
            if unit.startswith("week"):
                reps = self.add_days(date, amount * 7)
                repetitions = [starting_date] + reps
                return repetitions
            if unit.startswith("month"):
                # this is the most complicated part without reltivedelta
                # month = int(starting_date[5:7]) #it works even when it starts with 0, but to return it I will probably use the formating tool of datetime
                month = date.month
                day = date.day
                year = date.year
                month1 = (month + amount) % 12 if (month + amount) % 12 != 0 else 12
                addedyear1 = (month + amount) // 12 if (month + amount) % 12 != 0 else ((month + amount) // 12) - 1
                year1 = year + addedyear1
                month2 = (month1 + amount) % 12 if (month1 + amount) % 12 != 0 else 12
                addedyear2 = (month1 + amount) // 12 if (month1 + amount) % 12 != 0 else ((month1 + amount) // 12) - 1
                year2 = year1 + addedyear2
                month3 = (month2 + amount) % 12 if (month2 + amount) % 12 != 0 else 12
                addedyear3 = (month2 + amount) // 12 if (month2 + amount) % 12 != 0 else ((month2 + amount) // 12) - 1
                year3 = year2 + addedyear3
                if any(monthrange(y, m)[1] < day for (y, m) in [(year1, month1), (year2, month2), (year3, month3)]):
                    return []
                else:
                    rep1 = datetime.datetime(year1, month1, day)
                    repetition1 = rep1.strftime('%Y/%m/%d')
                    rep2 = datetime.datetime(year2, month2, day)
                    repetition2 = rep2.strftime('%Y/%m/%d')
                    rep3 = datetime.datetime(year3, month3, day)
                    repetition3 = rep3.strftime('%Y/%m/%d')
                    repetitions = [starting_date, repetition1, repetition2, repetition3]
                    return repetitions

                # depending on the amount of days of the resulting month I may have to modify the day as well
                # I will add the year in the same way as in the year case, so I willl refactor that
            if unit.startswith("year"):
                # for years it's easier just adding the number the year
                # year = date.year
                reps = self.add_years(starting_date, amount)
                return reps

            ''' 
            #find if there is a way to use the string in unit to introduce the keyword argument
            unit = repeat[2] if repeat[2][-1]=="s" else repeat[2]+"s"
            rep1=date+relativedelta(**{unit:amount})
            repetition1=rep1.strftime('%Y/%m/%d')
            rep2=rep1+relativedelta(**{unit:amount})
            repetition2 = rep2.strftime('%Y/%m/%d')
            rep3=rep2+relativedelta(**{unit:amount})
            repetition3 = rep3.strftime('%Y/%m/%d')
            '''



        else:
            return []

    def add_days(self, date, amount):
        days = datetime.timedelta(days=amount)
        rep1 = date + days
        repetition1 = rep1.strftime('%Y/%m/%d')
        rep2 = rep1 + days
        repetition2 = rep2.strftime('%Y/%m/%d')
        rep3 = rep2 + days
        repetition3 = rep3.strftime('%Y/%m/%d')
        repetitions = [repetition1, repetition2, repetition3]
        return repetitions

    def add_years(self, starting_date, amount):
        year = int(starting_date[:4])
        year1 = str(year + amount)
        year2 = str(year + 2 * amount)
        year3 = str(year + 3 * amount)
        repetition1 = year1 + starting_date[4:]
        repetition2 = year2 + starting_date[4:]
        repetition3 = year3 + starting_date[4:]
        repetitions = [starting_date, repetition1, repetition2, repetition3]
        return repetitions


# to get it back to the format date.strftime('%m/%d/%Y')
'''
if __name__ == '__main__':
    solution = Calendar()
    print(solution.get_repeating_event("2701/11/04", "every 1 days"))
'''