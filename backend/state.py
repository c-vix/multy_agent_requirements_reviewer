from typing import TypedDict


class RequirementState(TypedDict):
    requirement: str
    quality_result : str
    ambiguity_result : str
    security_result : str
    review_result : str
    rewritten_requirement : str