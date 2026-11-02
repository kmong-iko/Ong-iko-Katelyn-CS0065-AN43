# PART 1: KNOWLEDGE REPRESENTATION (KR)

# Knowledge Base: Stores current weather information
facts = {
    "temperature": 32,
    "is_raining": False,
    "humidity": 85,
    "wind_speed": 15,
    "cloudy": True
}

# Display the Knowledge Base
print("=== WEATHER KNOWLEDGE BASE ===")
for category, value in facts.items():
    print(f"{category}: {value}")


# PART 2: RULE-BASED REASONING (RBR)

# Rule 1: Check if the temperature is hot
def rule_hot(facts):
    if facts["temperature"] > 30:
        return "Turn on the air conditioner."

# Rule 2: Check if it is raining
def rule_rain(facts):
    if facts["is_raining"]:
        return "Bring an umbrella."

# Rule 3: Check if humidity is high
def rule_humidity(facts):
    if facts["humidity"] > 80:
        return "Use a dehumidifier."

# Rule 4: Check if it is cloudy
def rule_cloudy(facts):
    if facts["cloudy"]:
        return "Expect possible rain."

# List of available rules
rules = [
    rule_hot,
    rule_rain,
    rule_humidity,
    rule_cloudy
]

# Task 2B: Inference Engine
def inference_engine(facts, rules):
    actions = []

    # Check every rule against the knowledge base
    for rule in rules:
        result = rule(facts)

        if result:
            actions.append(result)

    return actions

# Task 2C: Display Output
print("\n=== RULE-BASED REASONING ACTIONS ===")

actions = inference_engine(facts, rules)

for action in actions:
    print("-", action)


# PART 3: CASE-BASED REASONING (CBR)

# Task 3A: Store previous weather cases
case_base = [
    {
        "problem": {
            "temperature": 35,
            "is_raining": False,
            "humidity": 90
        },
        "solution": "Turn on the air conditioner and use a dehumidifier."
    },
    {
        "problem": {
            "temperature": 25,
            "is_raining": True,
            "humidity": 75
        },
        "solution": "Bring an umbrella and stay indoors."
    },
    {
        "problem": {
            "temperature": 20,
            "is_raining": False,
            "humidity": 60
        },
        "solution": "Enjoy the cool weather outdoors."
    }
]


# Task 3B: Retrieve the most similar case
def retrieve_case(new_problem, case_base):
    best_case = None
    highest_similarity = -1

    for case in case_base:
        similarity = 0

        # Compare the weather features
        for feature in new_problem:
            if new_problem[feature] == case["problem"][feature]:
                similarity += 1

        if similarity > highest_similarity:
            highest_similarity = similarity
            best_case = case

    return best_case


# Task 3C: Reuse the solution
print("\n=== CASE-BASED REASONING ===")

# Use the current weather facts as the new problem
new_problem = {
    "temperature": facts["temperature"],
    "is_raining": facts["is_raining"],
    "humidity": facts["humidity"]
}

retrieved_case = retrieve_case(new_problem, case_base)

print("Most Similar Past Case:")
print(retrieved_case["problem"])

solution = retrieved_case["solution"]

print("\nReused Solution:")
print(solution)


# Task 3D: Revise the solution
print("\n=== REVISE SOLUTION ===")

choice = input("Do you want to modify the solution? (yes/no): ")

if choice.lower() == "yes":
    solution = input("Enter your revised solution: ")

print("Final Solution:", solution)


# Task 3E: Retain the new case
new_case = {
    "problem": new_problem,
    "solution": solution
}

case_base.append(new_case)

print("\n=== RETAINED NEW CASE ===")
print("New case successfully added to the case base!")
print("Total number of cases:", len(case_base))
