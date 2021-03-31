import random
import matplotlib.pyplot as plt
import sys
import subprocess
import pkg_resources

required = {'matplotlib'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

x = 0
y = 0

vx = []
vy = []

def randomwalk(x, y, steps):
    """Random walk function"""
    def step_choice(min, max):
        """Magnitude of the step"""
        return random.randint(min, max)
    
    is_magnitude = input("Do you want to enter custom magnitude? (y/n) Default magnitude is (-2, 2): ")
    if (is_magnitude.lower() == "y"):
        print("Now you have to enter the magnitude of the step. Magnitude is a range in which steps can deviate. For example (-2, 2). In this range steps can change from -2 upto +2.")
        min = int(input("Enter the MINIMUNM magnitude: "))
        max = int(input("Enter the MAXIMUM magnitude: "))
    else:
        min = -5
        max = 5

    for i in range(steps):
        magnitude = step_choice(min, max)
        x = x + (magnitude*random.randrange(-1, 2, 2))
        vx.append(x)
        y = y + (magnitude*random.randrange(-1, 2, 2))
        vy.append(y)


steps = int(input("How many steps you want to take? Steps between 1000 and 50000 work better: "))
randomwalk(0,0,steps)
# print(vx)
# print(vy)

points = list(range(steps))
plt.figure(figsize=(10, 6))
plt.scatter(vx, vy, c = points, cmap=plt.cm.Greens, s=5)

plt.scatter(0, 0, c="blue", edgecolor="none", s=100)
plt.scatter(vx[-1], vy[-1], s=100, c="red", edgecolor="none")
plt.show()