def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    acc_no= str(account_number)


    #Start writing your code here
    if acc_no[0]!="1" or len(acc_no)!=4:
        print("Invalid account number")
    elif account_balance < 100000 :
        print("Insufficient account balance")
    else :
        if salary <=25000 :
            print("Invalid loan type or salary")
        elif salary > 25000 and loan_type == "Car" :
            eligible_loan_amount=500000
            bank_emi_expected=36
            if bank_emi_expected<customer_emi_expected or eligible_loan_amount<loan_amount_expected:
                print("The customer is not eligible for the loan")
        elif salary > 50000 and loan_type == "House":
            eligible_loan_amount=6000000
            bank_emi_expected=60
            if bank_emi_expected<customer_emi_expected or eligible_loan_amount<loan_amount_expected:
                print("The customer is not eligible for the loan")
        elif salary > 75000 and loan_type == "Business":
            eligible_loan_amount=7500000
            bank_emi_expected=84
            if bank_emi_expected<customer_emi_expected or eligible_loan_amount<loan_amount_expected:
                print("The customer is not eligible for the loan")
        else:
            print("Invalid loan type or salary")


    if bank_emi_expected >= customer_emi_expected and eligible_loan_amount >= loan_amount_expected:
        print("Account number:", account_number)
        print("The customer can avail the amount of Rs.", eligible_loan_amount)
        print("Eligible EMIs :", bank_emi_expected)
        print("Requested loan amount:", loan_amount_expected)
        print("Requested EMI's:",customer_emi_expected)





    #Populate the variables: eligible_loan_amount and bank_emi_expected

    #Use the below given print statements to display the output, in case of success
    #print("Account number:", account_number)
    #print("The customer can avail the amount of Rs.", eligible_loan_amount)
    #print("Eligible EMIs :", bank_emi_expected)
    #print("Requested loan amount:", loan_amount_expected)
    #print("Requested EMI's:",customer_emi_expected)

    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #rint("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(1005,90000,255000,"Business",7600000,80)