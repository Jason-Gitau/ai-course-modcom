import joblib

try:
    model=joblib.load('loan_approval.pkl')
    print('model loaded succeessfully')
except FileNotFoundError:
    print('The file was not found')

except Exception as e:
    print(e)

def get_user_details():
    print("Please enter the following details")

    while True:
        try:
            Number_of_Deposits=int(input("how many depos have you made: "))
            Number_of_Withdrawals=int(input("how many withdrawals have you made: "))
            Paid_Previous_Loan=int(input('Did you pay your last loan 1=no,0=yes: '))
            salary=int(input("what is your monthly salary: "))
            age=int(input("How old are you: "))
            account_balance=int(input('what is the account balance account: '))
            Loan_Amount_Requested=int(input('How much money do you need for the loan'))
            Number_of_Late_Payments=int(input('How many late payments have you had: '))
            Years_at_Current_Job=int(input("How many years have you had your current job"))
            Credit_Score =int(input('what is your credit score (0-100)'))
            break

        except:
            print('invalid input, kindly input digits')

        user_input=[[Number_of_Deposits,Number_of_Withdrawals,Paid_Previous_Loan,salary,age,account_balance,Loan_Amount_Requested,Number_of_Late_Payments,Years_at_Current_Job,Credit_Score]]

    return user_input


results= model.predict(get_user_details)
print(results)





            















           
    
    
  
   
    
    
    
    
    