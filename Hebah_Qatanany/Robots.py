##################################################
# Author: Hebah Qatanany
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Professor: Diego Pajarito
# Email: hebah.qatanany@studnets.iaac.net
# Course: MaCT precourse- Programming
##################################################

current_distance_to_object=5
desired_distance_to_object=3

if current_distance_to_object > desired_distance_to_object:
    print('Move 3cm forward')
    print('Faster')
elif current_distance_to_object < desired_distance_to_object:
    print('Move 3cm backward')
    print('Slower')
elif current_distance_to_object>= desired_distance_to_object:
    move=(current_distance_to_object-desired_distance_to_object)/2
    print('move ' + move)

if current_distance_to_object > 10:
    print('Faster')
elif current_distance_to_object> 5:
    print('Same speed')
elif 5>= current_distance_to_object >0:
    print('Slower')
