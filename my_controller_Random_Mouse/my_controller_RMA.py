"""my_controller_random_Mouse controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, DistanceSensor, Motor, PositionSensor, GPS, Compass 
import random, math, time

def run_robot(robot):
    
    
    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28 #angular velocity
    
    #enable motors
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    gps = robot.getDevice('gps')
    gps.enable(timestep)
    startX = 23
    startZ = 0
    
    compass = robot.getDevice('compass')
    compass.enable(timestep)
    startHeading = 90

    
    #enable proximity sensors 
    prox_sensors = []
    for ind in range (8): #8 sensors on EPuck Robot
        sensor_name = 'ps' + str(ind)
        prox_sensors.append(robot.getDevice(sensor_name))
        prox_sensors[ind].enable(timestep)


    def go_straight():
           left_motor.setVelocity(max_speed)
           right_motor.setVelocity(max_speed)

    def turn_left():
        target_heading = current_heading + 90
        if target_heading > 360:
           target_heading = 90
            
        if current_heading < target_heading:
            left_motor.setVelocity(-0.1 * max_speed)
            right_motor.setVelocity(0.1 * max_speed)

    def turn_right():                  
        right_motor.setVelocity(-max_speed)
        left_motor.setVelocity(max_speed)
        robot.step(timestep)
        right_motor.setVelocity(0)
        left_motor.setVelocity(0)
        startX = posX
        
        
                
                                
    def turn_around():
        left_motor.setVelocity(0.6 * max_speed)
        right_motor.setVelocity(-0.6 * max_speed)
     
        
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
        left_wall = prox_sensors[5].getValue() > 80
        right_wall = prox_sensors[2].getValue() > 80
        front_wall = prox_sensors[7].getValue() > 80
   
        
        current_time = robot.getTime()
    
        left_speed = max_speed
        right_speed = max_speed
        
        
        if (posX < (startX - 15)):
            turn_right()
      
            
        
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
        
        
       # if posX == (startX + 12) or posX == (startX - 12):
        #    left_motor.setVelocity(0)
         #   right_motor.setVelocity(0)
            #turn_right()
            #startX = posX
            #startZ = posZ
    

# Enter here exit cleanup code.

if __name__ == "__main__":
#Create robot instance
    my_robot = Robot()
    run_robot(my_robot) 