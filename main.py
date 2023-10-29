# Exercise 2.9

# Implement a simple reflex agent for the vacuum environment in Exercise 2.8.
# Run the environment with this agent for all possible initial dirt configurations and agent locations.
# Record the performance score for each configuration and the overall average score.
# Output the sequence of actions for the environment and initial locations described in Figure 2.2

# 1X2 vacuum cleaner space according to Figure 2.2
# Initial dirt configurations and vacuum cleaner locations are:
# [(A, Clean), (B, Clean)], initial vacuum cleaner location = A
# [(A, Clean), (B, Dirty)], initial vacuum cleaner location = A
# [(A, Dirty), (B, Clean)], initial vacuum cleaner location = A
# [(A, Dirty), (B, Dirty)], initial vacuum cleaner location = A
# [(A, Clean), (B, Clean)], initial vacuum cleaner location = B
# [(A, Clean), (B, Dirty)], initial vacuum cleaner location = B
# [(A, Dirty), (B, Clean)], initial vacuum cleaner location = B
# [(A, Dirty), (B, Dirty)], initial vacuum cleaner location = B

# Task Environment and Key Assumptions:

# Task Environment:

# Environment class is the external environment
# with the WorldPosition class used to help construct that environment.

# Performance measure/score calculated in the
# SimpleReflexVacuumAgent's update_performance_score function.
# The performance score is an integer that is incremented each time the agent performs the sucking action
# on a dirty square. The reasoning for calculating the performance score in this manner goes as follows; the
# the primary intention of the SimpleReflexVacuumAgent (and a vacuum cleaner in general) is arguably to
# clean dirty squares through sucking in all the dirt. Therefore, the performance measure should evaluate
# the agent's ability to carry out this primary intention. The agent is programmed such that it will clean dirty squares
# through the sucking action as frequently as possible; that is, the agent will perform the sucking action
# for every dirty square that it perceives. Thus, for each action that the agent executes,
# it is expected that the performance measure (how many times the agent
# successfully carries out its primary intention of cleaning dirty squares) will be maximized given the
# initial environment configuration and agent location.

# Sensors feed information to the SimpleReflexVacuumAgent's specify_agent_action function.

# Actuator for cleaning dirty squares and moving between locations
# in the environment is defined in the SimpleReflexVacuumAgent's execute_action function.

# The SimpleReflexVacuumAgent has a run_agent_actions function that triggers a loop of actions that the agent executes.

# SimpleReflexVacuumAgent has a clean_square_counter variable that keeps track of
# how many squares the agent has visited and confirmed a status of clean.
# The clean_square_counter variable is part of a condition
# in the run_agent_actions function used to regulate the loop of executed actions.

# Key Assumptions:

# After the vacuum cleaning agent has sucked dirt from a square (and that square then becomes clean), the square
# CANNOT become dirty again.
# If a square begins with a status of clean, it cannot become dirty
# following the instantiation of the initial configuration.
# The Vacuum Cleaning Agent only finishes executing actions in its run_agent_actions function when the agent
# has checked upon visiting that both squares A and B have a status of clean.
# That is, the loop of executed actions in the run_agent_actions function
# only finishes when the clean_square_counter is equal to 2.

class Environment:

    def __init__(self, world_position_list):
        self.world = world_position_list


class WorldPosition:

    def __init__(self, location, status):
        self.location = location
        self.status = status


class SimpleReflexVacuumCleaningAgent:

    def __init__(self, env, current_vacuum_world_position_index):
        self.env = env
        self.current_vacuum_world_position_index = current_vacuum_world_position_index
        self.clean_square_counter = 0
        self.performance_score = 0
        print("Initial location of the Vacuum Cleaning agent is " +
              self.env.world[self.current_vacuum_world_position_index].location)

    # Agent function, which specifies the action the agent should take.
    # Agent function has pre-built knowledge of which squares and statuses it is checking for in
    # the environment as demonstrated in the pseudocode for the textbook Figure 2.8.
    def specify_agent_action(self):
        if self.env.world[self.current_vacuum_world_position_index].status == "Dirty":
            return "Suck"
        elif self.env.world[self.current_vacuum_world_position_index].location == "A":
            return "Right"
        elif self.env.world[self.current_vacuum_world_position_index].location == "B":
            return "Left"

    def execute_action(self, action):
        if action == "Suck":
            self.env.world[self.current_vacuum_world_position_index].status = "Clean"
            self.update_performance_score()
            print("Action: Suck" + " -> Same Location: " +
                  self.env.world[self.current_vacuum_world_position_index].location)
        elif action == "Right":
            self.current_vacuum_world_position_index += 1
            self.clean_square_counter += 1
            print("Action: Right" + " -> New Location: " +
                  self.env.world[self.current_vacuum_world_position_index].location)
        elif action == "Left":
            self.current_vacuum_world_position_index -= 1
            self.clean_square_counter += 1
            print("Action: Left" + " -> New Location: " +
                  self.env.world[self.current_vacuum_world_position_index].location)

    def update_performance_score(self):
        self.performance_score += 1

    def get_performance_score(self):
        return self.performance_score

    def run_agent_actions(self):
        while self.clean_square_counter < 2:
            self.execute_action(self.specify_agent_action())
        print("The Vacuum Cleaning Agent has finished running and locations A and B both have a status of Clean.")


# Run each of the four configurations and initial locations. Record the performance scores for each configuration and
# then calculate the overall average performance score for all configurations:

# [(A, Clean), (B, Clean)], initial vacuum cleaner location = A
# [(A, Clean), (B, Dirty)], initial vacuum cleaner location = A
# [(A, Dirty), (B, Clean)], initial vacuum cleaner location = A
# [(A, Dirty), (B, Dirty)], initial vacuum cleaner location = A
# [(A, Clean), (B, Clean)], initial vacuum cleaner location = B
# [(A, Clean), (B, Dirty)], initial vacuum cleaner location = B
# [(A, Dirty), (B, Clean)], initial vacuum cleaner location = B
# [(A, Dirty), (B, Dirty)], initial vacuum cleaner location = B

configuration_list = [Environment([WorldPosition("A", "Clean"), WorldPosition("B", "Clean")]),
                      Environment([WorldPosition("A", "Clean"), WorldPosition("B", "Dirty")]),
                      Environment([WorldPosition("A", "Dirty"), WorldPosition("B", "Clean")]),
                      Environment([WorldPosition("A", "Dirty"), WorldPosition("B", "Dirty")]),
                      Environment([WorldPosition("A", "Clean"), WorldPosition("B", "Clean")]),
                      Environment([WorldPosition("A", "Clean"), WorldPosition("B", "Dirty")]),
                      Environment([WorldPosition("A", "Dirty"), WorldPosition("B", "Clean")]),
                      Environment([WorldPosition("A", "Dirty"), WorldPosition("B", "Dirty")])]

initial_world_position_index_list = [0, 0, 0, 0, 1, 1, 1, 1]

performance_score_list = []

for index, c in enumerate(configuration_list):
    print("--")
    vacuum_cleaning_agent = SimpleReflexVacuumCleaningAgent(c, initial_world_position_index_list[index])
    print("Running Vacuum Cleaning Agent for configuration at index " + str(index) + "\n")
    vacuum_cleaning_agent.run_agent_actions()
    print("")
    performance_score_list.append(vacuum_cleaning_agent.get_performance_score())
    print("Performance Score for Vacuum Cleaning Agent: " +
          str(performance_score_list[index]))
    print("--\n")


def calculate_average_performance_score():
    average_performance_score = sum(performance_score_list) / len(configuration_list)
    return average_performance_score


print("The overall average performance score for the agent running against all configurations is " +
      str(calculate_average_performance_score()))
