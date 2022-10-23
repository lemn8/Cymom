# Cymom
main.py filename will autorun when powered on. 
I made everything like this so it can be controlled by Openhab2.5 and also minimum standby-power is used. 
Its for Servo2040 with Circuitpython. 
I only used three headers i dont know which one was which (arm/head/moving umbilical cord by fish wire). 
The crying baby sample is me when i was little which i found on a casette somewhere. The iron sounds are pizza stands moving around in the kitchen closet which is also available for download. 

For audio playback i used the DY-SV5W. The filename has to be 00001.mp3 then it will be played automatically if you solder a wire between 12 and 4 (see attached pic). Problem is it will loop so you need to time when to turn off the item when it got triggered. I will also include a example Halloweenprop.rules for openhab.

You fould trigger it by making a habpanel for your phone or movement-sensors. For me a habpanel worked best because i was guiding the guests around.

i never did this before so i hope it will be of any help...