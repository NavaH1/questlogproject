import calendar #

year = int((input)("Please type in the year you would like to check: "))
month = ((input)("Please type in the month you would like to check: ")).lower() # the lower is so we can make any
# input in lower case letters.

month_cal= {'december': 12,
'november': 11,
'october': 10,
'september': 9,
'august': 8,
'july': 7,
'june': 6,
'may': 5,
'april': 4,
'march': 3,
'february': 2,
'january': 1}

if month.isdigit():# I use the command .isdigit to check if the input is a number
   int_month_imp = int(month) # is use this command to change the input from str to int
   print(calendar.month(year, int_month_imp))
else:
   print(calendar.month(year, month_cal.get(month)))# we use the dictionary to assign str (months ) to number
