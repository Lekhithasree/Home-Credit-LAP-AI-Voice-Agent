
# Home Credit AI Voice Agent
# Step 18A: Connect the conversation

from conversation_state import create_customer_state, update_state
from call_greeting import greet_customer, verify_customer
from offer_presentation import present_offer


# Create a new customer record
customer = create_customer_state()

customer_name = "Rahul"
agent_name = "Priya"
company_name = "Home Credit"


# Step 1: AI greets the customer
print("\nAgent:")
print(greet_customer(customer_name, agent_name, company_name))


# Step 2: Customer confirms identity
print("\nCustomer: Yes, speaking")

response = verify_customer(
    customer,
    "Yes, speaking",
    customer_name
)

print("\nAgent:")
print(response)


# Step 3: Customer confirms availability
print("\nCustomer: Yes, go ahead")

update_state(customer, {
    "available_to_talk": True
})


# Step 4: AI presents the loan offer
print("\nAgent:")
print(present_offer(customer, company_name))


# Step 18B: Connect all eligibility questions

from qualification_flow import evaluate_customer

# Customer agrees to answer questions
print("\nCustomer: Yes, that's fine.")

print("\nAgent:")
print(evaluate_customer(customer))


# Simulated customer answers
answers = [
    ("Residential house",
     {"property_type": "Residential"}),

    ("Jointly owned with my wife",
     {"ownership": "Joint"}),

    ("Yes, I have original documents",
     {"documents": "yes"}),

    ("I need 50 lakh",
     {"loan_amount": 5000000}),

    ("I'm salaried and receive income in my bank",
     {"occupation": "Salaried", "income_mode": "Bank"}),

    ("My property is worth 1 crore",
     {"market_value": 10000000}),

    ("I want 10 years",
     {"tenure": 10})
]


# Process each customer answer
for customer_reply, new_information in answers:

    print("\nCustomer:", customer_reply)

    # Save customer information
    update_state(customer, new_information)

    # Check eligibility and get next question
    result = evaluate_customer(customer)

    print("Agent:", result)


# Step 19: Test an ineligible customer

print("\n--- Test: Ineligible Customer ---")

# Create a separate customer
customer2 = create_customer_state()

# Simulated customer responses
test_answers = [
    (
        "I own a residential house",
        {"property_type": "Residential"}
    ),
    (
        "I am self-employed and receive income in cash",
        {
            "occupation": "Self-employed",
            "income_mode": "Cash"
        }
    ),
    (
        "My property is jointly owned",
        {"ownership": "Joint"}
    )
]

# Process customer answers
for customer_reply, information in test_answers:

    print("\nCustomer:", customer_reply)

    # Save the customer's information
    update_state(customer2, information)

    # Check eligibility
    result = evaluate_customer(customer2)

    print("Agent:", result)

    # Stop immediately if the customer is ineligible
    if result.startswith("Not Eligible"):
        print("Call ended: No more questions.")
        break
