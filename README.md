#  CSC-450 Senior Research 
##  Analysis of Maze Solving Algorithms using a Micro Mouse Robot

### Objective
- Conduct an experiment using the software Webots to emulate the GCTronic' e-puck robot attempt to solve various mazes, comparing the average time of maze completion between the wall follower and random maze algorithms

### Software
- Webots Software can be downloaded from [here](https://cyberbotics.com/)


Webots website contains all the required documentation required to be able to create and implement robots in it's virtual world. Their [tutorial series](https://cyberbotics.com/doc/guide/tutorial-1-your-first-simulation-in-webots) gives a user the proper tools and resources to familiarize themselfs with the UI.

All mazes were randomly generated from [mazegenerator.net](https://www.mazegenerator.net/) and implemented in webotsw using solid wall nodes.

The source code included in this repository includes the controllers for each algorithm written in python, and the world files (.wbt) that are opened with Webots.
