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

calculateCreditCardBalance(4213, 0.2, 0.04)