
# Home Credit AI Voice Agent
# Step 16: Customer Greeting and Verification

from conversation_state import create_customer_state


# Step 1: Greet the customer
def greet_customer(customer_name, agent_name, company_name):

    return (
        f"Hello, may I speak with {customer_name}? "
        f"I'm {agent_name}, an AI voice assistant "
        f"calling from {company_name}."
    )


# Step 2: Verify the customer's identity
def verify_customer(state, response, customer_name):

    response = response.strip().lower()

    # Customer confirms their identity
    if response in ["yes", "yes, speaking", "speaking",
                    f"this is {customer_name.lower()}",
                    f"yes, this is {customer_name.lower()}"]:

        state["customer_verified"] = True

        return "Thank you for confirming. Is this a convenient time to talk?"

    # Customer says it is the wrong person
    elif response in ["no", "wrong number",
                      "not me", "you have the wrong number"]:

        state["customer_verified"] = False
        state["call_ended"] = True

        return "Sorry for the inconvenience. Thank you for your time."

    # Customer asks who is calling
    elif "who is calling" in response or "who's calling" in response:

        return f"I'm calling from Home Credit. May I confirm I'm speaking with {customer_name}?"

    # Any unclear response
    else:
        return f"Sorry, just to confirm, am I speaking with {customer_name}?"



# Run tests only when this file is executed directly
if __name__ == "__main__":

    # Test 1: Correct customer
    customer1 = create_customer_state()

    print("\nTest 1 - Correct Customer:")
    print(greet_customer("Rahul", "Priya", "Home Credit"))
    print(verify_customer(customer1, "Yes, speaking", "Rahul"))
    print("Verified:", customer1["customer_verified"])

    # Test 2: Customer asks who is calling
    customer2 = create_customer_state()

    print("\nTest 2 - Who Is Calling:")
    print(verify_customer(customer2, "Who is calling?", "Rahul"))

    # Test 3: Wrong number
    customer3 = create_customer_state()

    print("\nTest 3 - Wrong Number:")
    print(verify_customer(customer3, "Wrong number", "Rahul"))
    print("Call Ended:", customer3["call_ended"])

