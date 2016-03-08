# -*- coding: utf-8 -*-

# 2015-2016 Complementos de Programacao
# Grupo 3
# 43134 Luís Filipe Leal Campos
# 48392 Mariana Vieira De Almeida Nave

def changeFormatTime(period):
    """Change format of a period from 'HHHH' into 'HH:MM - HH:MM'.

    Requires:
    period is a string with the format 'HHHH'.
    Ensures:
    string with format 'HH:MM - HH:MM'.
    """

    H1 = period[0:2]
    H2 = period[2:4]

    return H1 + ":00 - " + H2 + ":00"


def getPreviousPeriod(period):
    """Gets the time of the previous 2 hour period.

    Requires:
    period is a string with the format 'HHHH'
    corresponding to a 2 hour period.
    Ensures:
    A string in the same format as the input, corresponding
    to the previous 2 hour period.
    """

    H1 = period[0:2]

    newH1 = str(int(H1) - 2)

    if len(newH1) == 1:
        newH1 = '0' + newH1

    newH2 = H1

    return newH1 + newH2
