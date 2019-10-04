import numpy as np
angle = [0,30,45,60,90]
angle = [i*np.pi/180 for i in angle]
print("sin:", np.sin(angle))
print("cos:", np.cos(angle))
print("tan:", np.tan(angle))