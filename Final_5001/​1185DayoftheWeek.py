'''
(Leetcode ​​1185) ​Day of the Week
给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
输入为三个整数：day、month 和 year，分别表示日、月、年。
您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。


示例 1：
输入：day = 31, month = 8, year = 2019
输出："Saturday"

示例 2：
输入：day = 18, month = 7, year = 1999
输出："Sunday"

示例 3：
输入：day = 15, month = 8, year = 1993
输出："Sunday"
 
提示：
给出的日期一定是在 1971 到 2100 年之间的有效日期。
'''


class Solution:
    # use list instead of calendar method
    # 1971-1-1 is Friday
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # def a function to define whether the year is a leapyear
        def isLeapYear(year):
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                return True
            else:
                return False

        # assign two list, the first is calendar, second is month_days
        calendar = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday']
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # if the year is a leapyear, the days of Feburary is 29
        if isLeapYear(year):
            month_days[1] = 29

        # initialize the days to be 0, and add days by year by month and by day
        days = 0
        # add by year
        for i in range(1971, year):
            if isLeapYear(i):
                days += 366
            else:
                days += 365

        # add by month
        for i in range(0, month-1):
            days += month_days[i]

        # add by day, add 4 because 1971-1-1 days=1 is Friday
        # the index of calendar is 5, so to get the right index
        # the days should add (5-1)=4
        days += day + 4

        # return the day of the calendar list
        return calendar[days%7]
