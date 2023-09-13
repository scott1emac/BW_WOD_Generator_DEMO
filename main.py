# BW WOD GENERATOR v1.0
import random as rd


# -------- Functions -------
def amrap():
    """Generates AMRAP (As Many Rounds As Possible) Workout"""

    num_exercise = rd.randint(2, 5)



    amrap_ex = []

    for i in range(num_exercise):
        amrap_ex.append('_')

    cycles = len(amrap_ex)
    print(cycles-1)

    while cycles > 0:
        amrap_ex[cycles-1] = ubm[rd.randint(0,(len(ubm)-1))]
        cycles = - 1
        amrap_ex[cycles - 1] = lbm[rd.randint(0, (len(lbm) - 1))]
        cycles = - 1
        amrap_ex[cycles - 1] = fbm[rd.randint(0, (len(fbm) - 1))]
        cycles = - 1


    return amrap_ex


# -------- Main Prg.-------


# Lists of Exercises.
ubm = ['Push-ups', 'Diamond Push-ups', 'Chair Dips', 'Decline Push-ups', 'Handstand Push-ups']
lbm = ['Air Squat', 'Jump Squat', 'Lunges', 'Lateral Squat', 'Calf Raise', 'Pistols']
fbm = ['Burpees', 'Mountain Climbers', 'High Knees', 'Leg Rises', 'V ups', 'Plank']

test = amrap()
print(test)
