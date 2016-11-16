'''
This code is not useful but will get the handles to vibrate.
It starts with the one with black tape, goes on with the one with yellow tape,
and finally it vibrates both. Going from speed 1 to speed 1+2
'''

from psychopy import core
from psychopy import parallel as pp

# Activate different pins;

# "Black" handle
# Activate pin 2 (Speed 1)
black_one = int("00000001", 2)
# Activate pin 3 (Speed 2)
black_two = int("00000010", 2)
# Activate pin 2 & 3 (Speed 1+2)
black_three = int("00000011", 2)

black = [black_one, black_two, black_three]
# "Yellow" handle
# Activate pin 4 (Speed 1)
yellow_one = int("00000100", 2)
# Activate pin 5 (Speed 2)
yellow_two = int("00001000", 2)
# Activate pin 4 & 5 (Speed 1+2)
yellow_three = int("00001100", 2)

yellow = [yellow_one, yellow_two, yellow_three]

# Both Handles
# Activate pin 2 + 4 (Speed 1)
both_one = int("00000101", 2)
# Activate pin 5 + 3 (Speed 2)
both_two = int("00001010", 2)
# Activate pin 2, 3, 4 & 5 (Speed 1+2)
both_three = int("00001111", 2)

both = [both_one, both_two, both_three]

# Vibrations

vibs = {'black': black, 'yellow': yellow, 'both': both}

#output = pp.ParallelPort(adress=0x3FF8)


# In the loop we go from the 'black' to the 'yellow' and the both handles
for key in vibs:
    for speed in vibs[key]:

        # Activate and start vibration
        port.setData(speed)

        # Vibrate for 400ms.
        core.wait(.4)

        # Stop vibration
        port.setData(0)
