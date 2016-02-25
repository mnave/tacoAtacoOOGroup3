# -*- coding: utf-8 -*-

# 2015-2016 Programacao 1 (LTI)
# Grupo 25
# 41515 Sílvia Carvalho
# 48392 Mariana Nave



def hourToInt(time):
    """

    """
    t = time.split(":")
    return int(t[0])


def minutesToInt(time):
    t = time.split(":")
    return int(t[1])


def intToTime(hour, minutes):
    """

    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + ":" + m


def add(time1, time2):
    """
    :returns: sum of 2 hours
    """
    t1Hour = hourToInt(time1)
    t1Minutes = minutesToInt(time1)
    t2Hour = hourToInt(time2)
    t2Minutes = minutesToInt(time2)

    hours = (t1Minutes + t2Minutes) / 60
    minutes = (t1Minutes + t2Minutes) % 60

    t1H = t1Hour + t2Hour + hours
    t1M = minutes

    return intToTime(t1H, t1M)


def diff(time1, time2):
    """

    """
    t1Hour = hourToInt(time1)
    t1Minutes = minutesToInt(time1)
    t2Hour = hourToInt(time2)
    t2Minutes = minutesToInt(time2)

    t1H = t1Hour - t2Hour
    minutes = t1Minutes - t2Minutes
    t1M = abs(minutes)

    if minutes < 0:
        t1H = t1H - 1
        t1M = 60 - t1M

    if t1H < 0:
        t1H = 0
        t1M = 0

    return intToTime(t1H, t1M)
