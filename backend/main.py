from graph import graph


def main():

    print("=" * 60)
    print("AI REQUIREMENT REVIEWER")
    print("=" * 60)

    requirement = input("\nEnter a software requirement:\n> ")

    if not requirement.strip():
        print("\nNo requirement entered. Please run the program again and enter a requirement.")
        return

    initial_state = {
        "requirement": requirement,
        "quality_result": "",
        "ambiguity_result": "",
        "security_result": "",
        "review_result": "",
        "rewritten_requirement": "",
    }

    print("\nReviewing requirement... this may take a moment.")
    result = graph.invoke(initial_state)

    print("\n" + "=" * 60)
    print("RESULT")
    print("=" * 60)

    print("\nOriginal Requirement:")
    print(result["requirement"])

    print("\n--- Quality Agent ---")
    print(result["quality_result"])

    print("\n--- Ambiguity Agent ---")
    print(result["ambiguity_result"])

    print("\n--- Security Agent ---")
    print(result["security_result"])

    print("\n--- Reviewer Agent ---")
    print(result["review_result"])

    print("\n--- Rewritten Requirement ---")
    print(result["rewritten_requirement"])


if __name__ == "__main__":
    main()
