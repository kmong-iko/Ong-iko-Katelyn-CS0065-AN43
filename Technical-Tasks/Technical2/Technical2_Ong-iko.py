# TASK 1: SET UP THE ENVIRONMENT

# Ask the user for the initial state of each room
rooms = {}

for room in ["A", "B"]:
    while True:
        state = input(f"Is Room {room} dirty or clean? ").strip().lower()

        if state in ["dirty", "clean"]:
            rooms[room] = state
            break
        else:
            print("Please enter only 'dirty' or 'clean'.")

# Function to check if a room is dirty
def is_dirty(room):
    return rooms[room] == "dirty"

# Function to clean a room
def clean_room(room):
    rooms[room] = "clean"

print("\nInitial Environment:", rooms)

# TASK 2: IMPLEMENT THE RULE-BASED AGENT

class VacuumAgent:
    def __init__(self, location="A"):
        self.location = location

    # Move to the other room
    def move(self):
        if self.location == "A":
            self.location = "B"
        else:
            self.location = "A"

    # Decide what action to take
    def perceive_and_act(self):
        if is_dirty(self.location):
            clean_room(self.location)
            action = "Cleaned Room " + self.location
        else:
            self.move()
            action = "Moved to Room " + self.location

        return action

# Create the agent starting in Room A
agent = VacuumAgent("A")

print("Agent created at Room", agent.location)

# TASK 3: RUN THE SIMULATION

while True:
    try:
        steps = int(input("Enter the number of simulation steps: "))
        if steps > 0:
            break
        print("Please enter a number greater than zero.")
    except ValueError:
        print("Please enter a valid whole number.")

print("\n--- SIMULATION START ---")

for step in range(1, steps + 1):
    action = agent.perceive_and_act()

    print(f"\nStep {step}")
    print("Agent Location:", agent.location)
    print("Action Taken:", action)
    print("Room Conditions:", rooms)

print("\n--- SIMULATION COMPLETE ---")
print("Final Environment:", rooms)
