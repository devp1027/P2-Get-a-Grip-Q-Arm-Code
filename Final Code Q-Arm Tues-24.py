ip_address = 'localhost' # Enter your IP Address here
project_identifier = 'P2B' # Enter the project identifier i.e. P2A or P2B
#--------------------------------------------------------------------------------
import sys
sys.path.append('../')
from Common.simulation_project_library import *

hardware = False
QLabs = configure_environment(project_identifier, ip_address, hardware).QLabs
arm = qarm(project_identifier,ip_address,QLabs,hardware)
potentiometer = potentiometer_interface()
#--------------------------------------------------------------------------------
# STUDENT CODE BEGINS
#---------------------------------------------------------------------------------

import random

def spawn_container(cage_num):
    arm.spawn_cage(cage_num) #spawns the cage with the given number input

def cage_pickup():
    time.sleep(2) #Rests between commands so the movements are visible and not instantaneous
    arm.move_arm(0.594, 0.031, 0.017) #moves arm to pickup location
    time.sleep(2)
    arm.control_gripper(40)#closes gripper around cage
    time.sleep(2)
    arm.move_arm(0.406, 0.0, 0.483) #moves arm to home without dropping object
    time.sleep(2)

def drop_off(cage_num):
    while True:
        if cage_num == 1 and 0.5 < potentiometer.left() <1: #cage is small and red, control of potentiometer to position 1 on autoclave
            time.sleep(2)
            arm.move_arm(0.0, -0.7, 0.3) #arm moves to position 1 of red autoclave
            time.sleep(2)
            arm.control_gripper(-40) #opens gripper to drop cage
            time.sleep(2)
            arm.home() #arm moves home to prepare for picking up the next cage
            break
        if cage_num == 4 and potentiometer.left()== 1: #cage is large and red, control of potentiometer to position 2 on autoclave
            time.sleep(2)
            arm.move_arm(0.0, -0.406, 0.24) #arm moves to position 2 of red autoclave
            time.sleep(2)
            arm.control_gripper(-40)
            time.sleep(2)
            arm.home()
            arm.open_autoclave('red',False) #closes drawer of red autoclave
            break
        if cage_num == 2 and 0.5 < potentiometer.left() <1: #cage is small and green
            time.sleep(2)
            arm.move_arm(0.0, 0.7, 0.3) #arm moves to position 1 of green autoclave
            time.sleep(2)
            arm.control_gripper(-40)
            time.sleep(2)
            arm.home()
            break
        if cage_num == 5 and potentiometer.left()== 1: #cage is large and green
            time.sleep(2)
            arm.move_arm(0.0, 0.406, 0.24) #arm moves to position 2 of green autoclave
            time.sleep(2)
            arm.control_gripper(-40)
            time.sleep(2)
            arm.home()
            arm.open_autoclave("green",False)
            break
        if cage_num == 3 and 0.5< potentiometer.left() <1: #cage is small and blue
            time.sleep(2)
            arm.move_arm(-0.62, 0.23, 0.3) #arm moves to position 1 of blue autoclave
            time.sleep(2)
            arm.control_gripper(-40)
            time.sleep(2)
            arm.home()
            break
        if cage_num == 6 and potentiometer.left()== 1: #cage is large and blue
            time.sleep(2)
            arm.move_arm(-0.382, 0.2, 0.3) #arm moves to position 2 of blue autoclave
            time.sleep(2)
            arm.control_gripper(-40)
            time.sleep(2)
            arm.open_autoclave('blue',False)
            arm.home()
            break
    
def rotate_base(cage_num):
    while True:
        arm.rotate_base(potentiometer.right()-0.5) #rotates base according to potentiometer reading
        if cage_num == 1:
            if arm.check_autoclave('red'):
                break #breaks if the correct cage number is at the correct autoclave so the drop function can begin
        if cage_num == 4:
            if arm.check_autoclave('red'):
                break
        if cage_num == 2:
            if arm.check_autoclave('green'):
                break
        if cage_num == 5:
            if arm.check_autoclave('green'):
                break
        if cage_num == 3:
            if arm.check_autoclave('blue'):
                break
        if cage_num == 6:
            if arm.check_autoclave('blue'):
                break
        
def open_autoclave(cage_num):
    if cage_num == 4: #checks if the cage is large and red
        arm.open_autoclave('red') #opens the red autoclave drawer
    if cage_num == 5:
        arm.open_autoclave('green')
    if cage_num == 6:
        arm.open_autoclave('blue')



arm.activate_autoclaves() #activates all autoclaves before arm moves
previous_containers = [1,2,3,4,5,6] #list of possible container identifiers
cage_num = random.sample(previous_containers,6) #assigns a random cage number between 1-6 but does not repeat within previous_containers list
for i in cage_num: #calls each function for each of the 6 cages
    arm.spawn_cage(i)
    cage_pickup()
    rotate_base(i)
    open_autoclave(i)
    drop_off(i)

#---------------------------------------------------------------------------------
# STUDENT CODE ENDS
#---------------------------------------------------------------------------------
    

    

