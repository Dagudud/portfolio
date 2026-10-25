def define(day, month):
    zodiac = month
    if day >= 1 and day <= 31 and month >= 1 and month <= 12:
        if day >= 22:
            zodiac = zodiac + 1
        if zodiac > 12:
            zodiac = 1
        return zodiac
    else:
        return 0