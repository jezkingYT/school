"""
Vytvoření tabulky sinusových hodnot po 30 stupních
sin(000°) = +0.00
sin(030°) = +0.50
sin(060°) = +0.87
sin(090°) = +1.00
sin(120°) = +0.87
sin(150°) = +0.50
sin(180°) = +0.00
sin(210°) = -0.50
sin(240°) = -0.87
sin(270°) = -1.00
sin(300°) = -0.87
sin(330°) = -0.50
sin(360°) = -0.00
"""

import math

for angle in range(0, 361, 30):
    sin_value = math.sin(math.radians(angle))
    print(f"sin({angle:03d}°) = {sin_value:+1.2f}")


import math
for angle  in range(0,361,30):
    radian_angle = math.radians(angle)
    sin_value = math.sin(radian_angle)
    print(f"sin({angle:03d}°) = {sin_value:+1.2f}")