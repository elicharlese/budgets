# ====================================================================================
'''
Getting the correct month based on the current datetime and the preferred forecast or history.
month_bug: string, this describes the current datetime right now in mm/dd/yyyy hh:mm:ss format
'''
# import datetime

# month_bug = datetime.datetime.now()

# print('This is the fixed version: {get_month(int(month.strftime("%m")))}')

# https://www.w3schools.com/python/trypython.asp?filename=demo_datetime_strftime_m
# https://www.w3schools.com/python/trypython.asp?filename=demo_datetime_strftime_b2
# ====================================================================================

months = 12
weeks_per_month = 4

def get_month(month):
    month += 1
    months_dict = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    if month <= 12:
        return months_dict[month]
    else:
        print("FIXME: Fix get_month function")

def print_corporate_budget_report(months):
    print('================================== Corporate Budget Report =====================================')
    # Categories
    corporations = 0
    reinvestments = 0
    generation = 0
    duplication = 0
    interests = 0
    storage = 0
    taxes = 0
    earnings = 0
    expenses = 0
    for month in range(months):
        for week in range(weeks_per_month):
            ##### Corporate Earnings #####
            earnings += 1000000 # Cleanfolio
            earnings += 10000000 # Majors & Minors
            earnings += 550000000 # GSL
            earnings += 100000000000 # DASH
        ##### Corporate Expenses #####
        # Taxes
        taxes = earnings * 0.1
        expenses += taxes
        # Interest (40% APY)
        interests += 500000
        storage -= 500000
        interests *= 1.0333
        # Taxes (Estimate)
        taxes = storage * 0.1
        storage -= taxes
        # Reinvestments (On Hand)
        reinvestments += 500000
        reinvestments *= 0.1
        storage -= 500000
        print(f'Interests for {get_month(month)}: ${"{:,}".format(int(interests))}')
        print(f'Expenses for {get_month(month)}: ${"{:,}".format(int(expenses))}')
        print(f'Taxes for {get_month(month)}: ${"{:,}".format(int(taxes))}')
        print(f'Cash for {get_month(month)}: ${"{:,}".format(int(corporations))}')
        print("------------")
        print(f'Savings after {get_month(month)}: ${"{:,}".format(int(earnings))}')
        print()
    print("========================================================")
    print()
    print(f'Total interests {month + 1} months from now: ${"{:,}".format(int(interests))}')
    print(f'Total expenses {month + 1} months from now: ${"{:,}".format(int(expenses))}')
    print(f'Total taxes {month + 1} months from now: ${"{:,}".format(int(taxes))}')
    print(f'Total cash {month + 1} months from now: ${"{:,}".format(int(corporations))}')
    print("------------")
    print(f'Total savings {month + 1} months from now: ${"{:,}".format(int(earnings))}')
    print()
    print('================================== End of Corporate Budget Report =====================================')
    print()

def print_family_budget_report(months):
    print('================================== Family Budget Report =====================================')
    # Categories
    members = 30
    income = 0
    expenses = 0
    interest = 0
    for month in range(months):
        for week in range(weeks_per_month):
            ##### Full-Power Bitcell #####
            income += 5000000
            ##### Half-Power Bitcell #####
            # income += 2500000
            ##### No-Power Bitcell #####
            # income += 0
        ##### Member Expenses #####
        # taxes
        taxes = income * 0.1
        #cash
        cash = income * 0.1
        expenses += cash
        cash *= 0.1
        # interest
        interest += 500000
        expenses += 500000
        interest *= 1.0333
        #expenses
        expenses += 100000
        # savings
        savings = income - expenses
        print(f'Interests for {get_month(month)}: ${"{:,}".format(int(interest))}')
        print(f'Expenses for {get_month(month)}: ${"{:,}".format(int(expenses))}')
        print(f'Taxes for {get_month(month)}: ${"{:,}".format(int(taxes))}')
        print(f'Cash for {get_month(month)}: ${"{:,}".format(int(cash))}')
        print("------------")
        print(f'Savings after {get_month(month)}: ${"{:,}".format(int(savings))}')
        print()
    print("========================================================")
    print()
    print(f'Total interests for all members: ${"{:,}".format(int(interest * members))}')
    print(f'Total expenses for all members: ${"{:,}".format(int(expenses * members))}')
    print(f'Total taxes for all members: ${"{:,}".format(int(taxes * members))}')
    print(f'Total cash for all members: ${"{:,}".format(int(cash * members))}')
    print("------------")
    print(f'Total savings for all members: ${"{:,}".format(int(savings * members))}')
    print()
    print('================================== End of Family Budget Report =====================================')
    print()

def print_personal_budget_report(months):
    print('================================== Personal Budget Report =====================================')
    #Categories
    interest = 0
    expenses = 0
    savings = 0
    cash = 0
    for month in range(months):
        for week in range(weeks_per_month):
            ##### Developer Job #####
            if 9 > month:
                savings += 2500
                # Developer (Part-Time)
                savings += 0
                savings += 0
                # Financer (Part-Time)
                savings += 0
                savings += 0
                # Trader (Part-Time)
                savings += 5000
                savings *= 1.1
            ##### Pipeline Finished #####
            else:
                # Developer (Part-Time)
                savings += 1000000
                savings += 10000000
                # Financer (Part-Time)
                savings += 550000000
                savings += 100000000000
                # Trader (Part-Time)
                savings += 5000000
                savings *= 1.1
        ##### Project Expenses #####
        if month == 4: # DASH & GSL
            savings -= 14000
            expenses += 14000
        if month == 5: # Majors
            savings -= 21000
            expenses += 21000
        if month == 6: # Minors
            savings -= 42000
            expenses += 42000
        ##### Big Expenses #####
        if month == 4: # Model S Downpayment
            savings -= 15000
            expenses += 10000
        if month == 7: # Summer Security Deposit
            savings -= 5000
            expenses += 5000
        if month == 9: # NY Security Deposit
            savings -= 30000
            expenses += 30000
        if month == 12: # Past Back Rent
            savings -= 18000
            expenses -= 18000
        ##### Personal Expenses #####
        if 9 > month:
            expenses += 10000
            savings -= 10000
            # Interest (40% APY)
            interest += 1000
            savings -= 1000
            interest *= 1.0333
            # Taxes (Estimate)
            taxes = savings * 0.1
            savings -= taxes
            # Cash (On Hand)
            cash += 1000
            cash *= 0.1
            savings -= 1000
        else:
            expenses += 10000000
            savings -= 10000000
            # Interest (40% APY)
            interest += 500000
            savings -= 500000
            interest *= 1.0333
            # Taxes (Estimate)
            taxes = savings * 0.1
            savings -= taxes
            # Cash (On Hand)
            cash += 500000
            cash *= 0.1
            savings -= 500000
            personal_budget_report = {
                "interest": interest,
                "expenses": expenses,
                "taxes": taxes,
                "cash": cash,
                "savings": savings
            }
        print(f'Interests for {get_month(month)}: ${"{:,}".format(int(interest))}')
        print(f'Expenses for {get_month(month)}: ${"{:,}".format(int(expenses))}')
        print(f'Taxes for {get_month(month)}: ${"{:,}".format(int(taxes))}')
        print(f'Cash for {get_month(month)}: ${"{:,}".format(int(cash))}')
        print("------------")
        print(f'Savings after {get_month(month)}: ${"{:,}".format(int(savings))}')
        print()
    print("========================================================")
    print()
    print(f'Total interests {month + 1} months from now: ${"{:,}".format(int(interest))}')
    print(f'Total expenses {month + 1} months from now: ${"{:,}".format(int(expenses))}')
    print(f'Total taxes {month + 1} months from now: ${"{:,}".format(int(taxes))}')
    print(f'Total cash {month + 1} months from now: ${"{:,}".format(int(cash))}')
    print("------------")
    print(f'Total savings {month + 1} months from now: ${"{:,}".format(int(savings))}')
    print()
    print('================================== End of Personal Budget Report =====================================')
    print()
    print(personal_budget_report)

print_corporate_budget_report(months)
print_family_budget_report(months)
print_personal_budget_report(months)

# ====================================================================================
'''
Building out the class and objects that will be used to distinguish members, corporations and personal budget
resources from eachother.
'''

# class budget:
#     # https://www.w3schools.com/python/python_classes.asp
#     budget = 0
#     init.__self__ = self
