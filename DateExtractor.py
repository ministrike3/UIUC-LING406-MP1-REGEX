import re
import os

#This function is simple; simply read in the article as one big string so that I can then work with it in other functions
def import_testing_article():
    article_link = os.getcwd() + "/Test_Inputs/testarticle"
    print(article_link)
    article_content = open(article_link, "r")
    article_content = article_content.read()
    return article_content

#I actually wrote a function for this regex because I also needed to do several things
#essentially this function is to find all the "2009" styled years;
#However, alot of the 'year' numbers are already taken by bigger regexs so I had to sort and decide which ones to keep
def dealing_with_standalone_years(content, mainlist):
    years = re.compile(
        r'[1-3][0-9]{3}')
    #y will have all the years in them
    y = []
    for i in years.finditer(content):
        y.append([i.start(), i.end(), i.group()])
    #What to remove will store the years that are already used by another term
    what_to_remove = []
    for i in range(0, len(y)):
        checking_start = y[i][0]
        checking_end = y[i][1]
        for current_order in mainlist:
            #If the year's position in the string is within the position markers of a bigger term it needs to be removed
            if checking_start >= current_order[0] and checking_end <= current_order[1]:
                what_to_remove.append(i)
    what_to_remove.reverse()
    for i in what_to_remove:
        del y[i]
    for i in y:
        mainlist.append([i[0], i[1], i[2]])
    return mainlist


if __name__ == "__main__":
    #import the article to test on
    article_inputted = import_testing_article()
    thing_to_order = []
    #This regex finds the big dates like "January 17th, 2017', but can also find 'January 2017'
    proper_dates = re.compile(
        r'(\b\d{1,2}\s{0,3})?\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?).?\s?(\d{1,2}(st|nd|rd|th)?)?(([,.\-\/]?)\D?)?((19[7-9]\d|20\d{2})|\d{2})*')
    for i in proper_dates.finditer(article_inputted):
        #This prevents little matches like . and D from activiating because the group(3) is the date group
        if i.group(3):
            thing_to_order.append([i.start(), i.end(), i.group()])
    #This regex find things like 'the 12th of December'
    blah_of_blahs = re.compile(
        r'\b(the)\D(\d{1,2}(st|nd|rd|th))\D(of)\D(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember))')
    for i in blah_of_blahs.finditer(article_inputted):
        thing_to_order.append([i.start(), i.end(), i.group()])
    #This finds things like 'Monday the 3rd'
    day_of_week = re.compile(
        r'\b((Mon|Tues|Wed(nes)?|Thur(s)?|Fri|Sat(ur)?|Sun)(day)?)\b\D(the)\D(\d{1,2}(st|nd|rd|th)?)')
    for i in day_of_week.finditer(article_inputted):
        thing_to_order.append([i.start(), i.end(), i.group()])
    #This finds all the holidays
    holiday_search = re.compile(
        r'\b(New Year\'s Day|New Year\'s Eve|Martin Luther King Jr. Day|Martin Luther King Day|Groundhog Day|Ash Wednesday|Valentine\'s Day|Presidents\' Day|St. Patrick\'s Day|Easter Sunday|Cinco de Mayo|Memorial Day|Independence Day|Columbus Day|Presidents\' Day|Christmas Eve|Christmas Day|Thanksgiving)')
    for i in holiday_search.finditer(article_inputted):
        thing_to_order.append([i.start(), i.end(), i.group()])
    #This finds dates of all forms xx/xx/xx
    date = re.compile(
        r'(\d{2}|\d)[\/\-](\d{2}|\d{1})([\/\-](\d{4}|\d{2}|\b)|\b)')
    for i in date.finditer(article_inputted):
        thing_to_order.append([i.start(), i.end(), i.group()])
    #This adds the standalone years by calling my function from above
    thing_to_order = dealing_with_standalone_years(article_inputted, thing_to_order)
    #This sorts the big list by appearance order
    thing_to_order = sorted(thing_to_order, key=lambda s: s[0])
    #This removes extra whitespaces or parantheses and stuff at the end
    for i in thing_to_order:
        if i[2][-1] == ' ':
            i[2] = i[2][:-1]
        if i[2][-1] == ',':
            i[2] = i[2][:-1]
        if i[2][-1] == ')':
            i[2] = i[2][:-1]
        print(i[2])
