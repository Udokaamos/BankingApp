import random
import time
with open('bank.txt','r') as file:
    doc = file.read()
    user = eval(doc)

print('Welcom to City Bank')

while True:

  
    time.sleep(1)
    print('Do you have an accont with us, yes or no? :')
    time.sleep(1)
    account_number = random.randrange(3000000000, 3999999999)
    login_user = input('>').lower()
    if login_user == 'yes':
        login_details = print(input('\nEnter your Account Number : '))
        new_password =  print(input('\nEnter your Password : '))
        print('You have successfully logged in to your account')
        account_balance = 0

        for i in range(5):
            print("\nDo you wish to perfom any other transaction like: \nDeposit, Withdraw or Transfer funds, or do you wish to Edit your detail?")

            time.sleep(1)
            print("\nT0 Deposit money, Press D, \nTo withdraw, Press W, \nTo Transfer to another Costumer, Press T, \nTo Edit your Details, Press E")
        
            
            user_inputs = input('>').lower()
            
            
            if user_inputs == 'd':
                deposit_money = int(input('Please deposit funds by inputting deposit amount here :\n>'))
                deposit = deposit_money
                account_balance = account_balance + deposit
                print(f'Your account balance is {account_balance}')
                # balance = account_balance
            elif user_inputs == 'w':
                withdraw_money = int(input('Input the amount you wish to withdraw : \n'))
                withdrawal_amount = withdraw_money
                if withdrawal_amount > account_balance:
                    print('insufficient funds.\r\nSorry, your transaction cannot be completed!')
                else:
                    print(f'Transaction completed \r\nYou have successfully withdrawn the sum of {withdrawal_amount}')
            elif user_inputs == 't':
                recipent_name = input('Enter the name of recipent :\n')
                recipent_account_number = int(input('Account number of recipent :\n'))
                transfer_amount = int(input('Transfer Amount :'))
                if transfer_amount > account_balance:
                    print('insufficient funds.\r\nSorry, your transaction cannot be completed!')
                else:
                    print(f'Transaction completed \r\nYou have successfully transfered the sum of {transfer_amount} to {recipent_name}')
            elif user_inputs == 'e':
                edit_details = print('Welcome to First BANK, you can edit your details here!!')
                Fullname = input('Please enter your fullname :\n> ')
                password = input('Edit password :\n> ')
                pin = input('Create new transaction pin :\n> ')
                Submit = print('To submit your edits, press S :')
                Submit_input = input('>').lower()
                Submit_edits = """
                You have successfully updated your details.
                """
                if Submit_input == 's':
                    print(Submit_edits)
            else:
                print('Your option does not exist. Goodbye!!!')
                
            
    else:
        print('Please input your details to signup')
        time.sleep(1)
        Fullname = input('\nEnter your fullname :\n> ')
        password = input('\nPlease create a password :\n> ')
        transaction_pin = input('\nCreate a transaction pin :\n> ')
        account_balance = 0

        print(f'\nYour current accout balance is {account_balance}')
        time.sleep(2)

        print('\nYour account have been successfully created')
        time.sleep(2)

        print(f'\nYour account number is: {account_number}')
        time.sleep(2)

        print('\nDo you wish to perform any transaction on your account, Yes or No? ')
        login_details = account_number
        new_password = password
        user_input = input('>').lower()
        
        if user_input == 'yes':
            print('\nPlease enter your Account Number and Password to login')
          

            login_details = int(input('\nEnter your Account Number : '))
            new_password =  input('\nEnter your Password : ')
            time.sleep(2)
            for i in range(2):
                if account_number == login_details and password == new_password:
                    print('Login Complete')

                    for i in range(5):
                        question = print(input("\nDo you wish to perfom any other transaction like: \nDeposit, Withdraw or Transfer funds, or do you wish to Edit your detail? \nYes or No!").lower())
                        if question == 'yes':
                            time.sleep(2)
                            request = print(input("\nT0 Deposit money, Press D, \nTo withdraw, Press W, \nTo Transfer to another Costumer, Press T, \nTo Edit your Details, Press E : ").lower())
                            
                            if request == 'd':
                                deposit_money = int(input('Please deposit funds by inputting deposit amount here :\n>'))
                                deposit = deposit_money
                                account_balance = account_balance + deposit
                                print(f'Your account balance is {account_balance}')
                            elif request == 'w':
                                withdraw_money = int(input('Input the amount you wish to withdraw : \n'))
                                withdrawal_amount = withdraw_money
                                if withdrawal_amount > account_balance :
                                    print('insufficient funds.\r\nSorry, your transaction cannot be completed!')
                                else:
                                    print(f'Transaction completed \r\nYou have successfully withdrawn the sum of {withdrawal_amount}')
                                    time.sleep(2)
                            elif request == 't':
                                recipent_name = input('Enter the name of recipent :\n')
                                recipent_account_number = int(input('Account number of recipent :\n'))
                                transfer_amount = int(input('Transfer Amount :'))
                                transfer = transfer_amount
                                if transfer > account_balance:
                                    print('insufficient funds.\r\nSorry, your transaction cannot be completed!')
                                else:
                                    print(f'Transaction completed \r\nYou have successfully transfered the sum of {transfer_amount} to {recipent_name}')
                            elif request == 'e':
                                edit_details = print('Welcome to First BANK, you can edit your details here!!')
                                Fullname = input('Please enter your fullname :\n> ')
                                password = input('Edit password :\n> ')
                                pin = input('Create new transaction pin :\n> ')
                                Submit = print('To submit your edits, press S :')
                                Submit_input = input('>').lower()
                                Submit_edits = """
                                You have successfully updated your details.
                                """
                                if Submit_input == 's':
                                    print(Submit_edits)
                            else:
                                print('Your option does not exist. Goodbye!!!')
                         

                                user['account_number'] = account_number
                                user['name'] = Fullname
                                user['password'] = password
                                user['pin'] = transaction_pin
                                user['balance'] = account_balance
                            
                        else:
                            print('\nThank you, Goodbye')    
                else:
                    print('Invalid input, Try again')
                    login_details = int(input('\nEnter your Account Number : '))
                    new_password =  input('\nEnter your Password : ')
                    time.sleep(2)
                if login_details != account_number and password != new_password:
                  print('\ninvalid user, please contact the customer care line on 09876784 for help!!!')
                  break
        else:
            print('\nThank you, Goodbye')
        with open('bank.txt', 'w') as file:
            file.write(f'{user}')
            # file.write(f'\nYour deposit is {deposit}')
            # file.write(f'\nYou withdrew the sum of {withdraw_money}')
            # file.write(f'\nThe sum of {transfer} has been transfered to {recipent_name}')

           