## Jenna Salmi practical assingment spring 2023
# Currency conversion program

import csv

# app selection


def app():
    filename = None
    while True:
        print("ACME(tm) US DOLLAR EXCHANGE RATE APP\n"
          "1) LOAD currency exchange rate data from a file\n"
          "2) USE AVERAGE exchange rate\n"
          "3) USE HIGHEST exchange rate\n"
          "4) USE LOWEST exchange rate\n"
          "5) CONVERT USD TO EUR\n"
          "6) CONVERT USD TO AUD\n"
          "7) CONVERT USD TO GBP\n"
          "0) QUIT program")
    
        choice = input("Choose what to do: ")

        if choice == "0":
            break
        elif choice == "1":
            filename = get_filename()
            currency(filename)
        elif choice == "2":
            option2(filename)
        elif choice == "3":
            option3(filename)
        elif choice == "4":
            option4(filename)
        elif choice == "5":
            convert_EUR_average(filename)
        elif choice == "6":
            convert_AUD_average(filename)
        elif choice == "7":
            convert_GBP_average(filename)
        else:
            print("Input a number between 0-7 to use exchange rate app.")

def get_filename():
    filename = input("Give name of the data file: ")
    return filename

# 1. option loading data
        
def currency (filename):
    with open(filename, "r") as currencydays:
            currencydays.readline()
            rows = []
            for line in currencydays:
                row = line.strip().split(";")
                rows.append(row)
                days_sum = len(rows)
                day1 = rows[0]
                last_day = rows[-1]
    print("Data loaded successfully!")
    print("Currency exchange data is from", days_sum, "days between",day1[0], "and", last_day[0]+".")
    print()

# Option AVERAGE for calculating exchange rates

def option2 (filename):
    print("Using the average currency exchange rate.")
    print()
    print("ACME(tm) US DOLLAR EXCHANGE RATE APP\n"
          "1) LOAD currency exchange rate data from a file\n"
          "2) USE AVERAGE exchange rate\n"
          "3) USE HIGHEST exchange rate\n"
          "4) USE LOWEST exchange rate\n"
          "5) CONVERT USD TO EUR\n"
          "6) CONVERT USD TO AUD\n"
          "7) CONVERT USD TO GBP\n"
          "0) QUIT program")
    
    choise = input("Choose what to do: ")

    if choise == "0":
        print()
    elif choise == "1":
            currency(filename)

    elif choise == "2":
            option2 (filename)

    elif choise == "3":
            option3 (filename)

    elif choise == "4":
            option4(filename)

    elif choise == "5":
        convert_EUR_average(filename)

    elif choise == "6":
        convert_AUD_average(filename)

    elif choise == "7":
        convert_GBP_average(filename)
    else:
        print("Input a number between 0-7 to use exchange rate app.")
        print()

#option HIGHEST for calculating exchange rates

def option3 (filename):
    print("Using the highest currency exchange rate.")
    print()
    print("ACME(tm) US DOLLAR EXCHANGE RATE APP\n"
          "1) LOAD currency exchange rate data from a file\n"
          "2) USE AVERAGE exchange rate\n"
          "3) USE HIGHEST exchange rate\n"
          "4) USE LOWEST exchange rate\n"
          "5) CONVERT USD TO EUR\n"
          "6) CONVERT USD TO AUD\n"
          "7) CONVERT USD TO GBP\n"
          "0) QUIT program")
    
    choise = input("Choose what to do: ")

    if choise == "0":
        print()
    elif choise == "1":
            currency(filename)
    elif choise == "2":
            option2 (filename)
    elif choise == "3":
            option3 (filename)
    elif choise == "4":
            option4(filename)
    elif choise == "5":
        convert_EUR_highest(filename)
    elif choise == "6":
        convert_AUD_highest(filename)
    elif choise == "7":
        convert_GBP_highest(filename)
    else:
        print("Input a number between 0-7 to use exchange rate app.")
        print()
        
#option LOWEST for calculating exchange rates
def option4 (filename):
    print("Using the lowest currency exchange rate.")
    print()
    print("ACME(tm) US DOLLAR EXCHANGE RATE APP\n"
          "1) LOAD currency exchange rate data from a file\n"
          "2) USE AVERAGE exchange rate\n"
          "3) USE HIGHEST exchange rate\n"
          "4) USE LOWEST exchange rate\n"
          "5) CONVERT USD TO EUR\n"
          "6) CONVERT USD TO AUD\n"
          "7) CONVERT USD TO GBP\n"
          "0) QUIT program")
    
    choise = input("Choose what to do: ")

    if choise == "0":
        print()
    elif choise == "1":
            currency(filename)
    elif choise == "2":
            option2 (filename)
    elif choise == "3":
            option3 (filename)
    elif choise == "4":
            option4(filename)
    elif choise == "5":
        convert_EUR_lowest(filename)
    elif choise == "6":
        convert_AUD_lowest(filename)
    elif choise == "7":
        convert_GBP_lowest(filename)
    else:
        print("Input a number between 0-7 to use exchange rate app.")
        print()
        
# Converting USD to EUR using average

def convert_EUR_average (filename):
    data = filename
    with open(filename, "r") as convertEur:
            convertEur.readline()
            eur = []
            for line in convertEur:
                row = line.strip().split(";")
                if row[1] != '':
                    eur1 = float(row[1])
                    eur.append(eur1)
    average = sum(eur) / len(eur)

    usd = float(input("Give USD to convert: "))
    converted = usd * average
    print(usd, "USD in EUR is", round(converted,2), "EUR")
    print()
    
# Converting USD to EUR using highest rate
def convert_EUR_highest (filename):
    data = filename
    with open(filename, "r") as convertEur:
            convertEur.readline()
            eur = []
            for line in convertEur:
                row = line.strip().split(";")
                if row[1] != '':
                    eur1 = float(row[1])
                    eur.append(eur1)
    highest = max(eur) 
    usd = float(input("Give USD to convert: "))
    converted = usd * highest
    print(usd, "USD in EUR is", round(converted,2), "EUR")
    print()
    
# Converting USD to EUR using lowest rate
def convert_EUR_lowest (filename):
    data = filename
    with open(filename, "r") as convertEur:
            convertEur.readline()
            eur = []
            for line in convertEur:
                row = line.strip().split(";")
                if row[1] != '':
                    eur1 = float(row[1])
                    eur.append(eur1)
    lowest = min(eur) 
    usd = float(input("Give USD to convert: "))
    converted = usd * lowest
    print(usd, "USD in EUR is", round(converted,2), "EUR")
    print()
    
# Converting USD to AUD using average

def convert_AUD_average (filename):
    data = filename
    with open(filename, "r") as convertAud:
            convertAud.readline()
            aud = []
            for line in convertAud:
                row = line.strip().split(";")
                if row[2] != '':
                    aud1 = float(row[2])
                    aud.append(aud1)
    average = sum(aud) / len(aud)

    usd = float(input("Give USD to convert: "))
    converted = usd * average
    print(usd, "USD in AUD is", round(converted,2), "AUD")
    print()
    
# Converting USD to AUD using highest

def convert_AUD_highest (filename):
    data = filename
    with open(filename, "r") as convertAud:
            convertAud.readline()
            aud = []
            for line in convertAud:
                row = line.strip().split(";")
                if row[2] != '':
                    aud1 = float(row[2])
                    aud.append(aud1)
    highest = max(aud) 
    usd = float(input("Give USD to convert: "))
    converted = usd * highest
    print(usd, "USD in AUD is", round(converted,2), "AUD")
    print()
    
# Converting USD to AUD using lowest
def convert_AUD_lowest (filename):
    data = filename
    with open(filename, "r") as convertAud:
            convertAud.readline()
            aud = []
            for line in convertAud:
                row = line.strip().split(";")
                if row[2] != '':
                    aud1 = float(row[2])
                    aud.append(aud1)
    lowest = min(aud) 
    usd = float(input("Give USD to convert: "))
    converted = usd * lowest
    print(usd, "USD in AUD is", round(converted,2), "AUD")
    print()
    
#Converting USD to GBP using average
    
def convert_GBP_average (filename):
    data = filename
    with open(filename, "r") as convertGBP:
        convertGBP.readline()
        gbp = []
        for line in convertGBP:
            row = line.strip().split(";")
            if row[3] != '':
                gbp1 = float(row[3])
                gbp.append(gbp1)
    average = sum(gbp) / len(gbp)

    usd = float(input("Give USD to convert: "))
    converted = usd * average
    print(usd, "USD in GBP is", round(converted,2), "GBP")
    print()
    
#Converting USD to GBP using highest
def convert_GBP_highest (filename):
    data = filename
    with open(filename,"r") as convertGBP:
        convertGBP.readline()
        gbp = []
        for line in convertGBP:
            row = line.strip().split(";")
            if row[3] != '':
                gbp1 = float(row[3])
                gbp.append(gbp1)
    highest = max(gbp) 
    usd = float(input("Give USD to convert: "))
    converted = usd * highest
    print(usd, "USD in GBP is", round(converted,2), "GBP")
    print()
    
# Converting USD to GBP using lowest
def convert_GBP_lowest (filename):
    data = filename
    with open(filename, "r") as convertGBP:
        convertGBP.readline()
        gbp = []
        for line in convertGBP:
            row = line.strip().split(";")
            if row[3] != '':
                gbp1 = float(row[3])
                gbp.append(gbp1)
    lowest = min(gbp) 
    usd = float(input("Give USD to convert: "))
    converted = usd * lowest
    print(usd, "USD in GBP is", round(converted,2), "GBP")
    print()

app()
