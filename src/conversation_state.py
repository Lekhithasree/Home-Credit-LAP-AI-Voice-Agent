
# Home Credit AI Voice Agent
# Step 11: Customer Memory

# Create an empty customer record
def create_customer_state():
    return {
        "property_type": None,
        "ownership": None,
        "documents": None,
        "loan_amount": None,
        "loan_limit_response":None,
        "occupation": None,
        "income_mode": None,
        "market_value": None,
        "tenure": None,
        "existing_property_loan":False,
        "emi_reduction_request":False,
        "is_busy":False,
        "callback_time":None,
        "available_to_talk":None,
        "customer_verified": None,
        "call_ended":False
        
    }


# Save information provided by the customer
def update_state(state, new_answers):
    for key, value in new_answers.items():
        if key in state and value is not None:
            state[key] = value

    return state


# Find the next unanswered question
def get_next_question(state):

    if state["property_type"] is None:
        return "What type of property do you own?"

    if state["ownership"] is None:
        return "Is the property solely or jointly owned?"

    if state["documents"] is None:
        return "Do you have original property documents?"

    if state["loan_amount"] is None:
        return "How much would you like to borrow?"

    if state["occupation"] is None and state["income_mode"] is None:
        return "Are you salaried or self-employed, and is your income received through a bank or in cash?"

    if state["occupation"] is None:
        return "Are you salaried or self-employed?"

    if state["income_mode"] is None:
        return "Is your income received through a bank or in cash?"

    if state["market_value"] is None:
        return "What is the approximate market value of your property?"

    if state["tenure"] is None:
        return "How many years would you like to repay the loan?"

    return "All seven eligibility items answered"



# Run these tests only when this file is executed directly
if __name__ == "__main__":

    # Create a customer
    customer = create_customer_state()

    # Save multiple answers
    update_state(customer, {
        "property_type": "Residential",
        "ownership": "Joint",
        "market_value": 8000000
    })

    print("Property:", customer["property_type"])
    print("Ownership:", customer["ownership"])
    print("Market Value:", customer["market_value"])

    print("Next Question:", get_next_question(customer))
