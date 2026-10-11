
# Home Credit AI Voice Agent
# Step 17: Present the Loan Offer

from conversation_state import (
    create_customer_state,
    update_state
)


def present_offer(state, company_name):

    # Do not continue an ended call
    if state["call_ended"]:
        return "Call already ended"

    # Verify the customer first
    if state["customer_verified"] is not True:
        return "Please verify the customer first"

    # Check whether the customer is busy
    if state["is_busy"] or state["available_to_talk"] is False:
        return "What time would be convenient for a callback?"

    # Confirm availability before explaining the offer
    if state["available_to_talk"] is not True:
        return "Is this a convenient time to talk?"

    # Present the special loan offer
    return (
        f"As one of our valued customers at {company_name}, "
        "you have a special pre-approved Loan Against Property "
        "offer of up to 75 lakh rupees. "
        "I'd like to ask a few questions to check your "
        "preliminary eligibility. Would that be okay?"
    )


# Run tests only when this file is executed directly
if __name__ == "__main__":

    # Test 1: Verified and available customer
    customer1 = create_customer_state()

    update_state(customer1, {
        "customer_verified": True,
        "available_to_talk": True
    })

    print("\nTest 1 - Present Offer:")
    print(present_offer(customer1, "Home Credit"))

    # Test 2: Busy customer
    customer2 = create_customer_state()

    update_state(customer2, {
        "customer_verified": True,
        "is_busy": True
    })

    print("\nTest 2 - Busy Customer:")
    print(present_offer(customer2, "Home Credit"))

    # Test 3: Unverified customer
    customer3 = create_customer_state()

    print("\nTest 3 - Unverified Customer:")
    print(present_offer(customer3, "Home Credit"))

    # Test 4: Availability not confirmed
    customer4 = create_customer_state()

    update_state(customer4, {
        "customer_verified": True
    })

    print("\nTest 4 - Confirm Availability:")
    print(present_offer(customer4, "Home Credit"))
