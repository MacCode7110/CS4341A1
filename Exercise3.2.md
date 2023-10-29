Chapter 3 - Exercise 3.2

Your goal is to navigate a robot out of a maze. The robot starts in the center of the maze
facing north. You can turn the robot to face north, east, south, or west. You can direct the
robot to move forward a certain distance, although it will stop before hitting a wall.

a. Formulate this problem. How large is the state space?

    Diagram of the starting problem:

               North
                 ^
                 |
    West       Robot        East


               South

    Problem Formulation (includes all key parts of a problem formulation):

        Assumptions: 
            1. The area of the maze is divided into n number of square units.
            2. The robot can only move forward in the direction that it faces.
            3. If a robot stops before hitting a wall, it will rotate clockwise until it faces the first new compass direction (north, east, south, or west) that is not immediately blocked by a wall. The robot will then move forward in that new direction.
    
        State Space: There are n number of square units and in each square unit, the robot faces either north, east, south, or west.
        Initial State: The robot occupies the square unit in the center of the maze and is rotated to face north.
        Goal State(s): The robot has finished moving i number of square units past a square unit marking either the north, east, south, or west borders of the maze.
        Actions: The robot can rotate to face north, east, south, or west. In addition, the robot can move forward i number of square units in the direction that it faces.
        Transitional Model:
        Action-Cost Function:
        

b. In navigating a maze, the only place we need to turn is at the intersection of two or
more corridors. Reformulate this problem using this observation. How large is the state
space now?



c. From each point in the maze, we can move in any of the four directions until we reach a
turning point, and this is the only action we need to do. Reformulate the problem using
these actions. Do we need to keep track of the robot’s orientation now?



d. In our initial description of the problem we already abstracted from the real world,
restricting actions and removing details. List three such simplifications we made.