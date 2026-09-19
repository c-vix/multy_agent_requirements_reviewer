from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from state import RequirementState

load_dotenv()


model = ChatOpenAI(
    model="gpt-5-mini",
    temperature=0
)


def quality_agent(state: RequirementState):
    requirement = state["requirement"]

    prompt = f"""
You are a Software Requirement Quality Agent.

Your responsibility is to evaluate the quality of a
software requirement.

Evaluate the requirement using these criteria:

1. Specific
2. Measurable
3. Clear
4. Testable

Requirement:
{requirement}

For each criterion:
- Say PASS or FAIL
- Give a short explanation

Do not rewrite the requirement.
Only analyze its quality.
short response is preferred.
"""

    response = model.invoke(prompt)

    return {
        "quality_result": response.content
    }

def ambiguity_agent(state: RequirementState):
    requirement = state["requirement"]

    prompt = f"""
You are a Software Requirement Ambiguity Agent.

Your responsibility is to identify ambiguous or vague
parts of a software requirement.

Look for:
- vague words
- subjective terms
- missing information
- unclear actors
- unclear actions
- unclear conditions

Requirement:
{requirement}

List each ambiguity and briefly explain why it is ambiguous.

Do not rewrite the requirement.
short response is preferred.
"""

    response = model.invoke(prompt)

    return {
        "ambiguity_result": response.content
    }

def security_agent(state: RequirementState):
    requirement = state["requirement"]

    prompt = f"""
You are a Software Security Requirement Agent.

Analyze the following requirement from a security perspective.

Look for missing considerations related to:
- authentication
- authorization
- passwords
- sensitive data
- access control
- security constraints

Requirement:
{requirement}

Identify relevant security concerns.

If there are no obvious security concerns, say so.

Do not rewrite the requirement.
short response is preferred.
"""

    response = model.invoke(prompt)

    return {
        "security_result": response.content
    }

def reviewer_agent(state: RequirementState):
    requirement = state["requirement"]

    quality = state["quality_result"]
    ambiguity = state["ambiguity_result"]
    security = state["security_result"]

    prompt = f"""
You are the Lead Software Requirement Reviewer.

Review the requirement using the analyses provided
by three specialist agents.

ORIGINAL REQUIREMENT:
{requirement}

QUALITY ANALYSIS:
{quality}

AMBIGUITY ANALYSIS:
{ambiguity}

SECURITY ANALYSIS:
{security}

Determine whether the requirement needs improvement.

Return your response in exactly this structure:

STATUS: GOOD

or

STATUS: NEEDS_IMPROVEMENT

Then provide a short explanation.

Do not rewrite the requirement yet.
short response is preferred.
"""

    response = model.invoke(prompt)

    return {
        "review_result": response.content
    }

def rewriter_agent(state: RequirementState):
    requirement = state["requirement"]

    quality = state["quality_result"]
    ambiguity = state["ambiguity_result"]
    security = state["security_result"]
    review = state["review_result"]

    prompt = f"""
You are a Software Requirement Rewriting Agent.

Rewrite the requirement to address the problems identified
by the specialist agents.

ORIGINAL REQUIREMENT:
{requirement}

QUALITY ANALYSIS:
{quality}

AMBIGUITY ANALYSIS:
{ambiguity}

SECURITY ANALYSIS:
{security}

REVIEW:
{review}

Create one improved software requirement.

The rewritten requirement should be:
- specific
- clear
- measurable where possible
- testable
- free from vague language

Return ONLY the rewritten requirement.
short response is preferred.
"""

    response = model.invoke(prompt)

    return {
        "rewritten_requirement": response.content
    }