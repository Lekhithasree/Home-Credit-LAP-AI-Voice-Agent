
# Home Credit AI Voice Agent
# Step 12: Connect memory and eligibility

from conversation_state import (
    create_customer_state,
    update_state,
    get_next_question
)

from eligibility import (
    check_property_type,
    check_ownership,
    check_documents,
    check_loan_amount,
    check_income,
    check_market_value,
    check_tenure
)


def evaluate_customer(state):

    
    # Check if customer needs loan transfer support
    if state["existing_property_loan"]:
        return "Transfer Required - Loan specialist follow-up. End call"

    # Check if customer wants to reduce existing EMI
    if state["emi_reduction_request"]:
        return "Transfer Required - Loan specialist follow-up. End call"

    
    # Check if the customer is busy
    if state["is_busy"]:

        # Customer is busy but has not given a callback time
        if state["callback_time"] is None:
            return "What time would be convenient for a callback?"

        # Customer has provided a callback time
        else:
            return "Callback time recorded - End the call"



    results = []

    # Check each available answer
    rules = [
        ("property_type", check_property_type),
        ("ownership", check_ownership),
        ("documents", check_documents),
        ("loan_amount", check_loan_amount),
        ("market_value", check_market_value),
        ("tenure", check_tenure)
    ]

    for field, check_function in rules:
        if state[field] is not None:
            result = check_function(state[field])
            results.append(result)

    # Check occupation and income together
    occupation = state["occupation"]
    income_mode = state["income_mode"]

    if occupation is not None or income_mode is not None:
        result = check_income(
            occupation or "",
            income_mode or ""
        )
        results.append(result)

    # Priority 1: Immediately reject ineligible customers
    for result in results:
        if result.startswith("Not Eligible"):
            return result

    
    # Priority 2: Handle loan amounts above 75 lakh

    maximum_amount = 7500000

    if state["loan_amount"] is not None:

        if state["loan_amount"] > maximum_amount:

            response = state["loan_limit_response"]

            # Customer accepts the 75 lakh offer
            if response == "accepted":
                state["loan_amount"] = maximum_amount

            # Customer declines the offer
            elif response == "declined":
                return "Customer declined 75 lakh - End the call"

            # Customer has not decided yet
            else:
                return "Our maximum offer is 75 lakh. Would you like to proceed with 75 lakh?"


    # Priority 3: Clarify unclear answers
    for result in results:
        if result.startswith("Please"):
            return result

    # Priority 4: Ask the next unanswered question
    next_question = get_next_question(state)

    if next_question == "All seven eligibility items answered":
        return "Qualified - Senior loan expert follow-up"

    return next_question
if __name__ == "__main__":
    # Test 1: Customer provides multiple answers
    customer = create_customer_state()

    update_state(customer, {
        "property_type": "Residential",
        "ownership": "Joint",
        "market_value": 8000000
    })

    print("\nTest 1 - Next Question:")
    print(evaluate_customer(customer))


    # Test 2: Customer mentions cash income
    update_state(customer, {
        "occupation": "Self-employed",
        "income_mode": "Cash"
    })

    print("\nTest 2 - Cash Income:")
    print(evaluate_customer(customer))


    # Test 3: Customer already has a property loan

    customer3 = create_customer_state()

    update_state(customer3, {
        "existing_property_loan": True
    })

    print("\nTest 3 - Existing Property Loan:")
    print(evaluate_customer(customer3))


    # Test 4: Customer wants to reduce existing EMI

    customer4 = create_customer_state()

    update_state(customer4, {
        "emi_reduction_request": True
    })

    print("\nTest 4 - EMI Reduction:")
    print(evaluate_customer(customer4))


    # Test 5: Customer is busy

    customer5 = create_customer_state()

    update_state(customer5, {
        "is_busy": True
    })

    print("\nTest 5 - Busy Customer:")
    print(evaluate_customer(customer5))


    # Test 6: Customer provides callback time

    update_state(customer5, {
        "callback_time": "Tomorrow at 3 PM"
    })

    print("\nTest 6 - Callback Time:")
    print(evaluate_customer(customer5))

    print("Saved Callback Time:", customer5["callback_time"])


    # Test 7: Customer requests 90 lakh

    customer7 = create_customer_state()

    update_state(customer7, {
        "loan_amount": 9000000
    })

    print("\nTest 7 - Loan Amount Above Limit:")
    print(evaluate_customer(customer7))


    # Test 8: Customer accepts 75 lakh

    update_state(customer7, {
        "loan_limit_response": "accepted"
    })

    print("\nTest 8 - Customer Accepts:")
    print(evaluate_customer(customer7))

    print("Saved Loan Amount:", customer7["loan_amount"])


    # Test 9: Customer declines 75 lakh

    customer9 = create_customer_state()

    update_state(customer9, {
        "loan_amount": 9000000,
        "loan_limit_response": "declined"
    })

    print("\nTest 9 - Customer Declines:")
    print(evaluate_customer(customer9))