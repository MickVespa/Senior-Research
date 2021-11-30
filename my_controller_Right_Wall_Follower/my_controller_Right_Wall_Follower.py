"""Right Wall Follower controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, DistanceSensor, Motor, PositionSensor
import math

def run_robot(robot):
    #wall following function#
    
    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28
    
    #enable motors
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    
    gps = robot.getDevice('gps')
    gps.enable(timestep)
    startX = 7
    startZ = 103
    
    compass = robot.getDevice('compass')
    compass.enable(timestep)
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    #Enable proximity sensors
    prox_sensors = []
    for ind in range (8): #8 sensors on EPuck Robot
        sensor_name = 'ps' + str(ind)
        prox_sensors.append(robot.getDevice(sensor_name))
        prox_sensors[ind].enable(timestep)
        
    #Main Loop
    #perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
    # Read the sensors:
        for ind in range (8):
            print("ind: {}, val: {}".format(ind, prox_sensors[ind].getValue()))
        
        #read GPS sensor       
        posX = int(gps.getValues()[0] * 100) # Convert from cm to m
        posZ = int(gps.getValues()[2] * 100)
        
        print("--------------------------")
        print("X Corrdinate = {}, Z Coordinate = {}".format(posX, posZ))
        
        heading_vector = compass.getValues() #gets compass heading in vectors
        current_heading2 = math.degrees(math.atan2(heading_vector[2],heading_vector[0]))
        current_heading = abs((current_heading2-360)%360)
        
        print("--------------------------")
        print("Compass Heading = {} ".format(current_heading))
        print("--------------------------")
    
    # Process sensor data here.
        right_wall = prox_sensors[2].getValue() > 80
        right_corner = prox_sensors[1].getValue() > 80
        front_wall = prox_sensors[0].getValue() > 80
    
        left_speed = max_speed
        right_speed = max_speed
    
        if front_wall:
            print("Turn left in place")
            left_speed = -max_speed
            right_speed = max_speed
    
        else: 
        
            if right_wall:
                print("Drive forward")
                left_speed = max_speed
                right_speed = max_speed
            
            else:
                print("Turn right in place")
                left_speed = max_speed
                right_speed = max_speed/6
                
            if right_corner:
                print("came too close, turning left")
                left_speed = max_speed/6
                right_speed = max_speed
                
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)


    

# Enter here exit cleanup code.

if __name__ == "__main__":
#Create robot instance
    my_robot = Robot()
    run_robot(my_robot) 
