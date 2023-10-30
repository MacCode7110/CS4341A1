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
            2. The robot can only move forward in the direction that it currently faces.
    
        State Space: 
            a. There are n number of square units and in each square unit, the robot faces either north, east, south, or west.
            b. The robot occupies a position that is outside of either the north, east, south, or west borders of the maze (in other words, the robot occupies a position outside of the area of the maze as a result of moving through a maze exit).
            c. The state space has a size that is greater than 4n because for each of the n square units that makes up the area of the maze, the robot faces one of four compass directions (north, east, south, or west). And, it is possible for the robot to occupy a certain number of reasonable positions outside of the maze.
        Initial State: The robot occupies the square unit in the center of the maze and is rotated to face north.
        Goal States: The robot occupies a position that is outside of either the north, east, south, or west borders of the maze (in other words, the robot occupies a position outside of the area of the maze as a result of moving through a maze exit).
        Actions: The robot can rotate to face north, east, south, or west. In addition, the robot can move forward i number of square units in the direction that it faces.
        Transitional Model: 
            a. Rotating the direction of the robot enables it to then move in that same direction (either north, east, south or west), which results in a change in state defined by a new direction.
                I. If the robot enters a state where it stops before hitting a wall, then the robot will need to rotate until it faces a new direction not immediately blocked by a wall. This rotation results in a change in state defined by a new direction.
            b. Moving the robot forward i number of square units in the direction that it faces results in a change in state defined by a new square unit that the robot occupies in the area of the maze. If the robot occupies a position outside of the maze area as a result of moving i number of square units, then it has reached a goal state.
        Action-Cost:
            The cost of an action for the robot is the length of the path it takes to exit the maze, which is equivalent to the total number of square units that it moves through.
            For each square unit that the robot moves through, the numeric cost increments by 1. 

b. In navigating a maze, the only place we need to turn is at the intersection of two or
more corridors. Reformulate this problem using this observation. How large is the state
space now?

        Problem Formulation (includes all key parts of a problem formulation):

        Updated Assumptions: 
            1. The area of the maze is divided into n number of square units.
            2. The robot can only move forward in the direction that it currently faces.
            3. When the robot occupies a square unit at the intersection of two or more corridors, it can rotate and face a new compass direction (either north, east, south, or west).
    
        Updated State Space: 
            a. There are n number of square units. 
            b. At each square unit that does not mark the intersection of two or more corridors, the robot cannot rotate to change the direction it faces. Therefore, there are at most two compass directions the robot can face when moving through a given corridor (moving towards a certain maze border or away from that same maze border).
            c. At each square unit that marks the intersection of two or more corridors, there are four possible compass directions that the robot can face.
            d. The robot occupies a position that is outside of either the north, east, south, or west borders of the maze (in other words, the robot occupies a position outside of the area of the maze as a result of moving through a maze exit).
            e. State space size:
                I. Important consideration: Due to the robot not being able to rotate when moving through a corridor, there may be certain square units in the maze the robot cannot occupy depending on the current corridor and area configurations.
                II. Let x = the number of square units the robot is able to occupy that DO NOT mark the intersection of two or more corridors.
                III. Let y = the number of square units that mark the intersection of two or more corridors.
                IIII. We know that at most (considering that there may be square units that are not possible to occupy), x + y sums to n. For x, there are at most two compass directions the robot can face. For y, there are four possible compass directions the robot can face.
                IV. According to the reasoning listed above, the state space size consists of two parts added together to form an expression: (a maximum of 2x + 4y) + (a certain number of reasonable positions outside of the maze)
        Initial State: The robot occupies the square unit in the center of the maze and is rotated to face north.
        Goal States: The robot occupies a position that is outside of either the north, east, south, or west borders of the maze (in other words, the robot occupies a position outside of the area of the maze as a result of moving through a maze exit).
        Updated Actions: 
            a. When the robot occupies a square unit marking the intersection of two or more corridors, it can rotate to face north, east, south, or west. This rotation at the occupied square unit results in a new state defined by a new direction.
            b. The robot can move forward i number of square units in the direction that it faces.
        Updated Transitional Model: 
            a. When the robot occupies a square unit marking the intersection of two or more corridors, rotating the direction of the robot enables it to then move in that same direction (either north, east, south or west), which results in a change in state defined by a new direction.
                I. If the robot enters a state where it stops before hitting a wall, then the robot will need to rotate until it faces a new direction not immediately blocked by a wall. This rotation results in a change in state defined by a new direction.
            b. Moving the robot forward i number of square units in the direction that it faces results in a change in state defined by a new square unit that the robot occupies in the area of the maze. If the robot occupies a position outside of the maze area as a result of moving i number of square units, then it has reached a goal state.
        Action-Cost:
            The cost of an action for the robot is the length of the path it takes to exit the maze, which is equivalent to the total number of square units that it moves through.
            For each square unit that the robot moves through, the numeric cost increments by 1. 

c. From each point in the maze, we can move in any of the four directions until we reach a
turning point, and this is the only action we need to do. Reformulate the problem using
these actions. Do we need to keep track of the robot’s orientation now?

    Problem Formulation (includes all key parts of a problem formulation):

        Updated Assumptions: 
            1. The area of the maze is divided into n number of square units.
            2. The robot can only move forward in the direction that it currently faces.
            3. Turning points in the maze consist of intersections of two or more corridors, and walls located immediately in front of the square unit the robot occupies.
    
        Updated State Space: 
            a. There are n number of square units. 
            b. State space information:
                I. Each square unit the robot occupies that is either the starting point (during the initial state) or a turning point.
                II. The robot occupies a position that is outside of either the north, east, south, or west borders of the maze (in other words, the robot occupies a position outside of the area of the maze as a result of moving through a maze exit).
        Initial State: The robot occupies the square unit in the center of the maze. This is the starting square unit.
        Goal States: The robot occupies a position that is outside of either the north, east, south, or west borders of the maze (in other words, the robot occupies a position outside of the area of the maze as a result of moving through a maze exit).
        Updated Actions: The robot can rotate in any of the four compass directions. The robot can move forward i number of square units in the direction that it faces until it reaches a turning point.
        Updated Transitional Model: 
            a. When the robot moves forward i number of square units and reaches a turning point, this action results in a change in state as the robot now occupies a turning point.  
            b. If the robot occupies a position outside of the maze area as a result of moving i number of square units, then it has reached a goal state.
        Updated Action-Cost:
            The cost of an action for the robot is the length of the path it takes to exit the maze, which in this case considering the updated state space, is equivalent to the total number of turning points that it moves through.
            For each turning point that the robot moves through, the numeric cost increments by 1. 

        We do not need to keep track of the orientation of the robot as we are only concerned about the starting square unit and each turning point the robot occupies.

d. In our initial description of the problem we already abstracted from the real world,
restricting actions and removing details. List three such simplifications we made.

    1. We simplified the compass direction angles in which the robot can face. In our abstractions, the robot can only face north, east, south, or west, which are all directions that are perpendicular to each other. Furthermore, we removed details such as the possibility of the robot facing a large variety of angles in the northeast, southeast, northwest, and southwest directions.
    2. We excluded details about the terrain of the maze; is the ground rough or smooth? Are there objects, people, or animals present in the maze? Are there are other agents that are moving through the maze? Our abstraction removes these terrain details to simplify the actions and transitional model of the robot.
    3. We excluded details about the width of each corridor, as well as the size of the robot. Do the corridors vary in width? Is the robot able to fit through each corridor? Can the robot adjust its size to make it into each corridor? 