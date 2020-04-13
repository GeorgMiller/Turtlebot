# Turtlebot

okay to execute everything do the following:


1. open terminal
run : 

export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo empty_world.launch.py


gazebo should show up


2. open Terminal in dqn_ws

run: 

colcon build

and:

. install/setup.bash

then run 

export TURTLEBOT3_MODEL=burger
ros2 run dqn turtlebot

to edit the file go to 

dqn_ws/src/dqn/dqn/turtlebot.py

if you have any questions, write me. It's not to much, but i guess it's a starting point. Tomorrow I will look how to integrate the dqn_turtlebot file into this structure. I now know how the setup.py and package.xml of colcon works.

