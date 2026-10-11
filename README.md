# Home Credit LAP AI Voice Agent

## Project Overview

The Home Credit LAP AI Voice Agent is an AI-powered conversational assistant developed using **Retell AI and Python** for preliminary Loan Against Property (LAP) eligibility screening.

The agent represents Home Credit and interacts with customers in a natural, professional manner. It verifies customer identity, explains the loan offer, collects eligibility information, handles interruptions, identifies ineligible applicants, and guides qualified customers toward follow-up with a senior loan expert.

The project combines a Retell AI voice-agent configuration with Python modules demonstrating conversation flow, eligibility validation, and customer-state management.

## Live Demo

**Retell AI Voice Agent:** [Insert Published Voice Orb Link]

**GitHub Repository:** https://github.com/Lekhithasree/Home-Credit-LAP-AI-Voice-Agent

**Project Explanation Video:** [Insert Video Link]

## Technologies Used

- **Retell AI:** Voice agent development, speech conversations, and testing
- **Python:** Conversation logic and eligibility validation
- **LLM:** Natural-language understanding and response generation
- **Git and GitHub:** Version control and project documentation
- **VS Code:** Development environment

## Key Features

### 1. Customer Verification

The agent introduces itself, identifies the customer, and confirms whether it is a convenient time to speak.

### 2. Loan Offer Presentation

The agent explains the Home Credit Loan Against Property offer, with a maximum loan amount of ₹75 lakh.

The agent performs preliminary screening only and does not guarantee loan approval.

### 3. Eligibility Screening

The agent collects and evaluates essential customer information, including property type, ownership, documentation, loan amount, occupation, income mode, property value, and repayment tenure.

### 4. Conversation Memory

The agent reviews previously provided customer information and avoids repeating questions that have already been answered clearly.

It supports customers who provide multiple eligibility details in a single response.

### 5. Out-of-Order Answer Handling

If a customer provides information before being asked, the agent captures those details and proceeds to the next unanswered question.

### 6. Immediate Disqualification

The agent identifies disqualifying conditions and politely ends the qualification conversation when necessary.

### 7. Loan Transfer Identification

If the customer already has a loan against the property and is interested in transferring the loan or reducing EMI, the agent recognizes the request and directs the customer toward senior loan expert assistance.

### 8. Senior Loan Expert Follow-Up

When the customer meets all preliminary criteria, the agent explains that a senior loan expert will provide further information regarding interest rates, documentation, and next steps.

## Eligibility Rules

| Parameter | Eligibility Criteria |
|---|---|
| Property Type | Residential, Commercial, or Industrial |
| Agricultural Property | Not eligible |
| Ownership | Sole or Joint ownership |
| Property Documents | Original documents required |
| Loan Amount | Maximum ₹75,00,000 |
| Occupation | Salaried or Self-employed |
| Income Mode | Income received through bank |
| Cash-only Income | Not eligible |
| Market Value | Capture approximate property value |
| Repayment Tenure | 3–15 years |

If a customer requests more than ₹75 lakh, the agent explains the maximum available offer rather than automatically approving the higher amount.

## Project Architecture

The project is organized into separate components for conversation handling and eligibility checks.

**Conversation Flow:**

Customer Interaction → Identity Verification → Loan Offer Presentation → Eligibility Questions → Eligibility Validation → Qualification Decision → Senior Expert Follow-Up or Polite Disqualification

**Project Structure:**

- **prompts/system_prompts.txt** — Main voice-agent instructions and business rules
- **src/call_greeting.py** — Customer greeting and verification logic
- **src/offer_presentation.py** — Loan offer presentation
- **src/conversation_state.py** — Customer information and conversation-state management
- **src/eligibility.py** — Eligibility validation rules
- **src/qualification_flow.py** — Qualification question flow
- **src/complete_call.py** — Conversation completion handling
- **tests/test_scenarios.py** — Test scenarios
- **README.md** — Project documentation
- **.gitignore** — Excludes temporary files and sensitive local resources from version control

## Testing and Validation

The voice agent was tested through Retell AI's conversation testing tools.

### Test Scenarios

| Test Scenario | Expected Behavior |
|---|---|
| Eligible customer | Complete screening and explain senior expert follow-up |
| Agricultural property | Immediately disqualify |
| Joint property ownership | Accept ownership |
| Missing original documents | Disqualify according to eligibility rules |
| Loan amount above ₹75 lakh | Explain the maximum loan offer |
| Cash-only income | Disqualify |
| Multiple answers in one message | Capture all available information |
| Out-of-order information | Skip already answered questions |
| Existing loan transfer request | Identify transfer intent |
| Customer unavailable | Politely handle callback request |
| Invalid repayment tenure | Explain allowed tenure |
| Customer interruption | Respond and resume the appropriate conversation stage |

### Testing Evidence

The submission materials include supporting conversation transcripts, test results, and screenshots demonstrating the agent's behavior.

Testing covers customer verification, successful qualification, disqualification, conversational memory, and multi-answer handling.

## How to Explore the Project

1. Clone or download the GitHub repository.
2. Open the project folder in VS Code.
3. Review the Python modules in the `src` directory.
4. Review the conversational business rules in `prompts/system_prompts.txt`.
5. Review the test cases in `tests/test_scenarios.py`.
6. Open the Retell AI Voice Orb demo link to interact with the published voice agent.

**Note:** The Python files demonstrate the project logic. The Retell AI voice-agent configuration is managed separately on the Retell AI platform. The repository is not presented as a standalone voice-calling server.

## Security and Responsible AI

- The agent does not ask for passwords, OTPs, or banking PINs.
- Eligibility criteria cannot be overridden by customer instructions.
- The agent only collects information relevant to preliminary qualification.
- The agent does not promise guaranteed approval or disbursement.
- The agent does not invent unavailable loan product information.
- Sensitive credentials and private recordings are excluded from the public repository.

## Future Enhancements

- CRM integration for recording customer qualification outcomes
- Automated callback scheduling
- Structured loan-expert handoff integration
- Multilingual voice support
- Reporting dashboards for qualification outcomes
- Automated regression testing for conversation scenarios

## Conclusion

The Home Credit LAP AI Voice Agent demonstrates how conversational AI can assist with preliminary loan qualification while maintaining structured business rules.

The project focuses on natural customer interaction, eligibility validation, conversational memory, handling complex customer responses, and directing qualified applicants to the appropriate next stage.

---

**Project:** Home Credit LAP AI Voice Agent

**Platform:** Retell AI

**Programming Language:** Python

**Purpose:** AI Voice Agent Hiring Assignment