print('Опреденение знака зодиака v0.1')
print('date format: day month')
print('Дата в формате: день месяц')
date = str(input()).lower()
day = 0
month = 0
ind = 0

for i in range(len(date)):
    if date[i].isalpha() or date[i - 1] == ' ':
        ind = i
        break

dictEN = ['', 'january', 'febraury', 'march', 'april', 'may', 'jun', 'july', 'august', 'september', 'october',
          'november', 'december']
dictRU = ['', 'январ', 'феврал', 'март', 'апрел', 'ма', 'июн', 'июл', 'август', 'сентябр', 'октябр', 'ноябр', 'декабр']
maxDaysInMonth = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dictCirill = 'яфмаисонд'

rusLang = True

if date[ind:len(date)].isnumeric():
    month = int(date[ind:len(date)])
else:
    month = date[ind:len(date)]
    if month[0] in dictCirill:
        try:
            month = dictRU.index(month[0:-1])
        except ValueError:
            print('Некорректоно указан месяц')
            month = -1
    else:
        rusLang = False
        try:
            month = dictEN.index(month)
        except ValueError:
            print('The month is incorrect')
            month = -1

if date[0:ind - 1].isnumeric():
    day = int(date[0:ind - 1])

if not ((1 <= month <= 12) and (1 <= day <= maxDaysInMonth[month])):
    print('Некорректные данные')

zodiac = ''

if (month == 3 and 21 <= day) or (month == 4 and 19 >= day):
    if rusLang:
        zodiac = 'Овен'
    else:
        zodiac = 'Aries'

if (month == 4 and 20 <= day) or (month == 5 and 20 >= day):
    if rusLang:
        zodiac = 'Телец'
    else:
        zodiac = 'Taurus'

if (month == 5 and 21 <= day) or (month == 6 and 20 >= day):
    if rusLang:
        zodiac = 'Близнецы'
    else:
        zodiac = 'Gemini'

if (month == 6 and 21 <= day) or (month == 7 and 22 >= day):
    if rusLang:
        zodiac = 'Рак'
    else:
        zodiac = 'Cancer'

if (month == 7 and 23 <= day) or (month == 8 and 22 >= day):
    if rusLang:
        zodiac = 'Лев'
    else:
        zodiac = 'Leo'

if (month == 8 and 23 <= day) or (month == 9 and 22 >= day):
    if rusLang:
        zodiac = 'Дева'
    else:
        zodiac = 'Virgo'

if (month == 9 and 23 <= day) or (month == 10 and 22 >= day):
    if rusLang:
        zodiac = 'Весы'
    else:
        zodiac = 'Libra'

if (month == 10 and 23 <= day) or (month == 11 and 21 >= day):
    if rusLang:
        zodiac = 'Скорпион'
    else:
        zodiac = 'Scorpio'

if (month == 11 and 22 <= day) or (month == 12 and 21 >= day):
    if rusLang:
        zodiac = 'Стрелец'
    else:
        zodiac = 'Sagittarius'

if (month == 12 and 22 <= day) or (month == 1 and 19 >= day):
    if rusLang:
        zodiac = 'Козерог'
    else:
        zodiac = 'Capricorn'

if (month == 1 and 20 <= day) or (month == 2 and 18 >= day):
    if rusLang:
        zodiac = 'Водолей'
    else:
        zodiac = 'Aquarius'

if (month == 2 and 19 <= day) or (month == 3 and 20 >= day):
    if rusLang:
        zodiac = 'Рыбы'
    else:
        zodiac = 'Pisces'

if rusLang:
    print('Твой знак ' + zodiac)
else:
    print('Your sign ' + zodiac)


