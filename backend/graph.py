from langgraph.graph import StateGraph, START, END
from state import RequirementState
from agents import (quality_agent, ambiguity_agent, security_agent, reviewer_agent, rewriter_agent)

def route_after_review(state: RequirementState):
    review = state["review_result"]

    if "STATUS: GOOD" in review:
        return "end"

    return "rewrite"

builder = StateGraph(RequirementState)

# add agents as nodes
builder.add_node("quality", quality_agent)
builder.add_node("ambiguity", ambiguity_agent)
builder.add_node("security", security_agent)
builder.add_node("reviewer", reviewer_agent)
builder.add_node("rewriter", rewriter_agent)

# starting point
builder.add_edge(START, "quality")

# normal flow
builder.add_edge("quality", "ambiguity")
builder.add_edge("ambiguity", "security")
builder.add_edge("security", "reviewer")

builder.add_conditional_edges(
    "reviewer",
    route_after_review,
    {
        "end": END,
        "rewrite": "rewriter",
    },
)

builder.add_edge("rewriter", END)

graph = builder.compile()
