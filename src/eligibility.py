
# Home Credit AI Voice Agent
# Loan Against Property - Eligibility Rules


# Rule 1: Property Type
def check_property_type(property_type):
    property_type = property_type.strip().lower()

    eligible_types = ["residential", "commercial", "industrial"]

    if property_type in eligible_types:
        return "Eligible - Continue to next question"

    elif property_type == "agricultural":
        return "Not Eligible - End the call"

    else:
        return "Please clarify the property type"


# Rule 2: Ownership
def check_ownership(ownership):
    ownership = ownership.strip().lower()

    if ownership in ["sole", "joint"]:
        return "Eligible - Continue to next question"

    return "Please clarify the ownership status"


# Rule 3: Original Documents
def check_documents(documents_available):
    documents_available = documents_available.strip().lower()

    if documents_available == "yes":
        return "Eligible - Continue to next question"

    elif documents_available == "no":
        return "Not Eligible - End the call"

    return "Please clarify document availability"


# Rule 4: Loan Amount
def check_loan_amount(amount):
    maximum_amount = 7500000

    if amount <= 0:
        return "Please enter a valid loan amount"

    elif amount <= maximum_amount:
        return "Eligible - Continue to next question"

    return "Offer maximum loan amount of 75 lakh"


# Rule 5: Occupation and Income
def check_income(occupation, income_mode):
    occupation = occupation.strip().lower()
    income_mode = income_mode.strip().lower()

    eligible_occupations = ["salaried", "self-employed"]

    if income_mode == "cash":
        return "Not Eligible - End the call"

    if income_mode != "bank":
        return "Please clarify the income mode"

    if occupation in eligible_occupations:
        return "Eligible - Continue to next question"

    return "Please clarify the occupation"


# Rule 6: Property Market Value
def check_market_value(market_value):

    if market_value > 0:
        return "Property value recorded - Continue to next question"

    return "Please provide a valid property value"


# Rule 7: Loan Tenure
def check_tenure(tenure):

    if 3 <= tenure <= 15:
        return "Eligible - Continue to next question"

    return "Not Eligible - End the call"


# Check a complete customer application
def check_customer_eligibility(customer):

    checks = [
        check_property_type(customer["property_type"]),
        check_ownership(customer["ownership"]),
        check_documents(customer["documents"]),
        check_loan_amount(customer["loan_amount"]),
        check_income(
            customer["occupation"],
            customer["income_mode"]
        ),
        check_market_value(customer["market_value"]),
        check_tenure(customer["tenure"])
    ]

    for result in checks:
        if result != "Eligible - Continue to next question" \
                and result != "Property value recorded - Continue to next question":
            return result

    return "Qualified - Senior loan expert follow-up"


# Run tests only when this file is executed directly
if __name__ == "__main__":

    print("Test 1 - Residential Property:")
    print(check_property_type("Residential"))

    print("\nTest 2 - Agricultural Property:")
    print(check_property_type("Agricultural"))

    print("\nTest 3 - Cash Income:")
    print(check_income("Salaried", "Cash"))

    print("\nTest 4 - Loan Amount Above Limit:")
    print(check_loan_amount(9000000))

    print("\nTest 5 - Valid Tenure:")
    print(check_tenure(10))

    # Complete customer test
    customer = {
        "property_type": "Residential",
        "ownership": "Joint",
        "documents": "yes",
        "loan_amount": 5000000,
        "occupation": "Salaried",
        "income_mode": "Bank",
        "market_value": 10000000,
        "tenure": 10
    }

    print("\nComplete Customer Eligibility Result:")
    print(check_customer_eligibility(customer))
