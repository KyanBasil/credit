import json

def evaluate_credit_card_application(applicant):
    # Set credit score threshold for acceptance
    credit_score_threshold = 650
    
    # Set income threshold for acceptance
    income_threshold = 30000
    
    # Set debt-to-income ratio threshold for acceptance
    debt_to_income_threshold = 0.45
    
    # Set age threshold for acceptance
    age_threshold = 18
    
    # Set credit utilization ratio threshold for acceptance
    credit_utilization_threshold = 0.3
    
    # Set number of delinquent accounts threshold for acceptance
    delinquent_accounts_threshold = 1
    
    # Set number of recent credit applications threshold for acceptance
    recent_applications_threshold = 2
    
    points_against = 0
    
    # Check if applicant meets credit score requirement
    if applicant['credit_score'] < credit_score_threshold:
        points_against += 1
    
    # Check if applicant meets income requirement
    if applicant['income'] < income_threshold:
        points_against += 1
    
    # Calculate debt-to-income ratio
    debt_to_income_ratio = applicant['total_debt'] / applicant['income']
    
    # Check if applicant meets debt-to-income ratio requirement
    if debt_to_income_ratio > debt_to_income_threshold:
        points_against += 1
    
    # Check if applicant meets age requirement
    if applicant['age'] < age_threshold:
        points_against += 1
    
    # Check if applicant meets credit utilization requirement
    if applicant['credit_utilization'] > credit_utilization_threshold:
        points_against += 1
    
    # Check if applicant meets delinquent accounts requirement
    if applicant['delinquent_accounts'] > delinquent_accounts_threshold:
        points_against += 1
    
    # Check if applicant meets recent credit applications requirement
    if applicant['recent_applications'] > recent_applications_threshold:
        points_against += 1
    
    recommendation = ""
    new_credit_limit = 0
    
    if points_against >= 3:
        recommendation = "Deny Credit"
    elif points_against == 2:
        recommendation = "Approve with Low Credit Limit"
        new_credit_limit = 1000  # Set a default low credit limit for new customers
    elif points_against == 1:
        recommendation = "Approve with Medium Credit Limit"
        new_credit_limit = 3000  # Set a default medium credit limit for new customers
    else:
        if applicant['credit_score'] >= 800 and applicant['income'] >= 100000:
            recommendation = "Approve with High Credit Limit"
            new_credit_limit = 10000  # Set a default high credit limit for new customers
        else:
            recommendation = "Approve with Standard Credit Limit"
            new_credit_limit = 5000  # Set a default standard credit limit for new customers
    
    return recommendation, new_credit_limit

def manual_review(customers):
    name = input("Enter the customer's name: ")
    for customer in customers:
        if customer['name'].lower() == name.lower():
            print(f"Customer: {customer['name']}")
            print(f"Current Credit Limit: {customer['current_credit_limit']}")
            recommendation, new_credit_limit = evaluate_credit_card_application(customer)
            print(f"Recommendation: {recommendation}")
            print(f"New Credit Limit: {new_credit_limit}")
            
            # Prompt for approval
            approval = input("Do you approve the change? (Y/N): ")
            if approval.lower() == 'y':
                # Update the customer's credit limit in the JSON file
                customer['current_credit_limit'] = new_credit_limit
                with open('customers.json', 'w') as file:
                    json.dump(customers, file, indent=2)
                print("Customer's credit limit has been updated.")
            else:
                print("Change not approved. Customer's credit limit remains unchanged.")
            
            return
    
    print("Customer not found.")

def new_credit_application(customers):
    print("New Credit Application")
    
    # Prompt for customer information
    name = input("Enter the customer's name: ")
    income = float(input("Enter the customer's income: "))
    credit_score = int(input("Enter the customer's credit score: "))
    num_cards = int(input("Enter the number of credit cards the customer has: "))
    age = int(input("Enter the customer's age: "))
    past_history = input("Enter the customer's past credit history (Good/Neutral/Bad): ")
    status = input("Enter the customer's employment status (Employed/Student): ")
    total_debt = float(input("Enter the customer's total debt: "))
    employment_length = int(input("Enter the customer's employment length (in months): "))
    hard_inquiries = int(input("Enter the number of hard inquiries on the customer's credit report: "))
    delinquent_accounts = int(input("Enter the number of delinquent accounts: "))
    years_since_bankruptcy = int(input("Enter the number of years since the customer's last bankruptcy (0 if none): "))
    credit_utilization = float(input("Enter the customer's credit utilization ratio: "))
    credit_history_length = int(input("Enter the length of the customer's credit history (in months): "))
    credit_accounts = int(input("Enter the number of credit accounts the customer has: "))
    recent_applications = int(input("Enter the number of recent credit applications: "))
    savings_balance = float(input("Enter the customer's savings account balance: "))
    requested_credit_limit = float(input("Enter the requested credit limit: "))
    late_payments = int(input("Enter the number of late payments: "))
    collections_accounts = int(input("Enter the number of collections accounts: "))
    public_records = int(input("Enter the number of public records: "))
    credit_card_accounts = int(input("Enter the number of credit card accounts: "))
    installment_loan_accounts = int(input("Enter the number of installment loan accounts: "))
    mortgage_accounts = int(input("Enter the number of mortgage accounts: "))
    
    # Create a new customer dictionary
    new_customer = {
        "name": name,
        "income": income,
        "credit_score": credit_score,
        "num_cards": num_cards,
        "age": age,
        "past_history": past_history,
        "status": status,
        "total_debt": total_debt,
        "employment_length": employment_length,
        "hard_inquiries": hard_inquiries,
        "delinquent_accounts": delinquent_accounts,
        "years_since_bankruptcy": years_since_bankruptcy,
        "credit_utilization": credit_utilization,
        "credit_history_length": credit_history_length,
        "credit_accounts": credit_accounts,
        "recent_applications": recent_applications,
        "savings_balance": savings_balance,
        "requested_credit_limit": requested_credit_limit,
        "late_payments": late_payments,
        "collections_accounts": collections_accounts,
        "public_records": public_records,
        "credit_card_accounts": credit_card_accounts,
        "installment_loan_accounts": installment_loan_accounts,
        "mortgage_accounts": mortgage_accounts,
        "current_credit_limit": 0  # Set initial credit limit to 0
    }
    
    # Evaluate the new credit application
    recommendation, new_credit_limit = evaluate_credit_card_application(new_customer)
    
    print(f"\nNew Credit Application Evaluation:")
    print(f"Customer: {new_customer['name']}")
    print(f"Recommendation: {recommendation}")
    print(f"New Credit Limit: {new_credit_limit}")
    
    # Prompt for approval
    approval = input("Do you approve the new credit application? (Y/N): ")
    if approval.lower() == 'y':
        # Update the new customer's credit limit based on the evaluation
        new_customer['current_credit_limit'] = new_credit_limit
        
        # Add the new customer to the customers list
        customers.append(new_customer)
        
        # Update the customers.json file
        with open('customers.json', 'w') as file:
            json.dump(customers, file, indent=2)
        
        print("New credit application approved and customer added to the database.")
    else:
        print("New credit application not approved.")


def review_all_accounts(customers):
    for customer in customers:
        recommendation, new_credit_limit = evaluate_credit_card_application(customer)
        print(f"Customer: {customer['name']}")
        print(f"Current Credit Limit: {customer['current_credit_limit']}")
        print(f"Recommendation: {recommendation}")
        print(f"New Credit Limit: {new_credit_limit}")
        print()

def manual_action(customers):
    # Placeholder function for manual action against an account
    print("Manual Action")
    # Add logic to handle manual action against an account

def main():
    # Read customer data from customers.json
    with open('customers.json') as file:
        customers = json.load(file)

    while True:
        print("\nAdmin Menu:")
        print("1. Run a manual review on someone's account")
        print("2. Initiate a new Credit Application")
        print("3. Run a review on all accounts")
        print("4. Take manual action against an account")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            manual_review(customers)
        elif choice == '2':
            new_credit_application(customers)
        elif choice == '3':
            review_all_accounts(customers)
        elif choice == '4':
            manual_action(customers)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
