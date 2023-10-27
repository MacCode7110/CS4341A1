Chapter 2 - Exercise 2.3

For each of the following assertions, say whether it is true or false and support your
answer with examples or counterexamples where appropriate.

a. An agent that senses only partial information about the state cannot be perfectly rational.

    False
    If an agent senses only partial information about the state, it can still be perfectly rational.
    Rational agents can operate in a partially observable environment as their percept sequence is based on the content that their sensors percieve.
    In addition, rational agents should be autonomous, which means that they have the capacity to learn and build off of their prior knowledge of the environment and its state regardless of the extent of that knowledge.
    For example, a table-cleaning agent could be perfectly rational in a partially observable environment, and as part of that, be able to learn how to anticipate when and where new germs and bacteria will surface. 
    In the above example, the table-cleaning agent is rational if it selects actions that maximize its performance measure according to the information for each possible percept sequence (dependent on the content that the sensors percieve) and the amount of prior knowledge of the environment. In particular, as long as the agent is selecting actions that maximize its performance measure based on each possible percept sequence, it is rational regardless of whether the sensors provide access to the complete state of the environment at each point in time. 

b. There exist task environments in which no pure reflex agent can behave rationally.

    True
    Yes, there are task environments in which no pure reflex agent can behave rationally.
    A pure reflex agent makes the correct decision based on the current percept. In order for a pure reflex agent to be rational in this case, the environment must be fully observable as this would provide the pure reflex agent with the full state needed to inform the needed percept.
    If there is an environment that is only partially observable, then no pure reflex agent can behave rationally in that environment as the agent cannot access the full state through its sensors.

c. There exists a task environment in which every agent is rational.

    True
    For example, there could be an environment that is both static and only consists of one state. 
    In this task environment, every agent is rational because any action that is taken in response to any percept sequence will result in the same expected value (every action will produce the same state). Every agent will maximize the expected value of the performance measure by default.

d. The input to an agent program is the same as the input to the agent function.

    False
    Agent programs take the current percept as input from the sensors and send an action to the actuators.
    An agent program implements the agent function, which takes in the percept sequence as input and responds by deciding the action that the agent will take.

e. Every agent function is implementable by some program/machine combination.

    False
    As a counterexample based on computer science theory, there could be a goal-based agent with the goal of solving an undecidable problem in an environment containing a Turing Machine and an input tape. 
    For undeciable problems, there is no algorithm that can determine the correct answer on all inputs. 
    Therefore, it is impossible to implement an agent function that fulfills the goal of solving an undecidable problem as there is no way that the agent function can decide the correct action (answer essentially) for all inputs.

f. Suppose an agent selects its action uniformly at random from the set of possible actions.
There exists a deterministic task environment in which this agent is rational.

    True
    For example, in a deterministic environment where there is only one possible resulting state for every action and current state, an agent that selects its actions uniformly at random from the set of possible actions will be rational.
    Based on the logic above, the resulting environment state will be exactly the same as the current state for any action that the agent function specifies.

g. It is possible for a given agent to be perfectly rational in two distinct task environments.

    True
    A task environment consists of the performance measure, the external environment, the actuators, and the sensors. 
    It is indeed possible for a given agent to be perfectly rational in two distinct task environments where certain parts of their respective external environments are different from each other and are not observed by the agents' sensors.
    For example, taking into consideration the table-cleaning agent mentioned in part a, say that the following holds for the table-cleaning agent:
        The performance measure has an expected value of cleaning a new square inch of the given table every second until the entire table is clean.
        Its sensors only consume environment information about which square inches have been cleaned and which square inches are still dirty.
    And say that the following holds about two distinct task environments A and B:
        The difference between A and B that makes each one distinct is that in the external environment for A there is exactly one chair tucked into the table and in the external environment for B there are no chairs tucked into the table.
        Otherwise, the performance measure, actuators, and sensors are exactly the same in both A and B.
    Since the sensors for the table-cleaning agent only detect information about clean and dirty square inches on the table, as long as it maximizes the expected value of the performance measure given the percept sequence, the table-cleaning agent will be perfectly rational in both distinct task environments A and B. The prescence of a tucked-in chair in task environment A has no impact on the performance measure and is not detected by the table-cleaning agent's sensors.

h. Every agent is rational in an unobservable environment.

    False
    As a counterexample, if an agent is acting in an unobservable environment and has prior knowledge of the environment reflected in its initial configuration, it is still possible for the agent to make bad decisions even without any information percieved through sensors. In this case where the expected value of the performance measure is not maximized in the unobservable environment, the agent is not rational.

i. A perfectly rational poker-playing agent never loses.

    False
    If an opposing poker-playing agent that is also perfectly rational has a superior hand in a game of poker, then the former perfectly rational pocker-playing agent can still lose, and could possibly lose multiple times as well.
