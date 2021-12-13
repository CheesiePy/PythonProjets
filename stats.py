"""
Student: May Lindenberg
ID: 203132949
Assignment no. 3
Program: stats.py
"""
import math

def isfloat(str):
    """this func checks for valid input for isfloat func"""
    ls = [i if i.isdecimal() or i == "." or i == "+" or i == "-" or i == " " else None for i in str]
    if None in ls:
        return False
    else:
        flag = True
        for i in range(len(ls)):
            if ls[i] == ' ' and ls[i+1] == '0':
                if ls[i+2] != ".":
                    flag = False
                else:
                    continue
            elif ls[i] == " " and ls[i+1] == ".":
                flag = False
            else:
                continue
        return flag


def string_to_list(str):
    """this func turn a str of numbers to a list of floats"""
    ls = str.split(" ")
    numlist = [float(i) for i in ls if (i != "" and i != " ")]
    return numlist


def mean(list1):
    """this func takes a list of nums and return the average of them """
    size = len(list1)
    addvalue = 0
    for i in list1:
        addvalue += float(i)
    return round(addvalue/size, 2)

def sd(list1):
    """this func takes a list of numbers and returns the standard deviation"""
    addvalue = 0
    avrg = (mean(list1))
    for i in list1:
            addvalue += (abs(avrg - (i))**2) / len(list1)
    return round(math.sqrt(addvalue), 2)

def median(list1):
    """this func takes a list of numbers and returns the median"""
    x = sorted(list1)
    l = len(list1)
    m = (l//2)
    if l % 2 == 0:
        return round((x[m-1] + x[m])/2, 2)
    else:
        return round(x[m], 2)

def main():
    file_input = open("numbers1.txt", "r")
    file_read = file_input.read()
    if isfloat(file_read):
        main_list = string_to_list(file_read)
        main_mean = mean(main_list)
        main_sd = sd(main_list)
        main_median = median(main_list)
        file_out = open("stats.txt", "w")
        text = ("mean: {:>21}\nstandard deviation: {:>7}\nmedian: {:>19}".format(main_mean, main_sd, main_median))
        file_out.write(text)
    else:
        print("illegal input!")
main()