__author__ = 'vnellore'


def calculateCreditCardBalance(balance, annualInterestRate, monthlyPaymentRate):

    print 'balance = ' + str(balance)
    print 'annualInterestRate = ' + str(annualInterestRate)
    print 'monthlyPaymentRate = ' + str(monthlyPaymentRate)
    minimumMonthlyPayment = 0
    totalPaid = 0
    for i in range(1, 13):
       minimumMonthlyPayment = monthlyPaymentRate * balance
       interest = (annualInterestRate/12.0) * (balance - minimumMonthlyPayment)
       balance += (round(interest, 2) - round(minimumMonthlyPayment, 2))
       totalPaid += minimumMonthlyPayment

       print 'Month: ' + str(i)
       print 'Minimum monthly payment : ' + str(round(minimumMonthlyPayment,2))
       print 'Remaining balance : ' + str(balance)

    print 'Total paid: ' + str(round(totalPaid,2))


def calculateFixedPayoffAmount(balance, annualInterestRate):

    print 'balance = ' + str(balance)
    print 'annualInterestRate = ' + str(annualInterestRate)
    minimumMonthlyPayment = 100.0

    original_balance = balance

    while balance > 0:
        balance = original_balance
        for i in range(1, 13):
            interest = (annualInterestRate/12.0) * (balance - minimumMonthlyPayment)
            balance += (round(interest, 2) - round(minimumMonthlyPayment, 2))

        print 'monthly payment : ' + str(minimumMonthlyPayment) + ' balance : ' + str(balance)
        if balance > 0:
            minimumMonthlyPayment += 10
        else:
            break

    print('Lowest Payment : ' + str(minimumMonthlyPayment))

calculateFixedPayoffAmount(3926, 0.2)