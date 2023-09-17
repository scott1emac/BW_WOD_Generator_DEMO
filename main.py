# BW WOD GENERATOR v1.0
import random as rd


# -------- Functions -------
def amrap():
    """Generates AMRAP (As Many Rounds As Possible) Workout"""

    # Generates random number of exercises.
    num_exercise = rd.randint(2, 5)

    # List of randomly generated exercises.
    amrap_ex = []

    # Creates empty placeholders in amrap_ex for cycle count.
    for i in range(num_exercise):
        amrap_ex.append('_')

    # uses count from amrap_ex for cycle int.
    cycles = len(amrap_ex)

    # Replaces empty placeholders in amrap_ex with exercises from upper body, lower body, and full body lists.
    while cycles > 0:
        amrap_ex[cycles - 1] = ubm[rd.randint(0, (len(ubm) - 1))]
        if cycles > 0:
            cycles -= 1
        amrap_ex[cycles - 1] = lbm[rd.randint(0, (len(lbm) - 1))]
        if cycles > 0:
            cycles -= 1
        amrap_ex[cycles - 1] = fbm[rd.randint(0, (len(fbm) - 1))]
        if cycles > 0:
            cycles -= 1

    # Generates number of reps per exercise.
    r = len(amrap_ex)
    r_num = []
    for i in range(r):
        r_num.append(rd.randint(8, 12))

    # Generates Time.
    t = tme[rd.randint(2, 5)]

    # Generates Text return
    exr = amrap_ex
    reps = r_num

    print(f"\n{t} MINUTE AMRAP OF:\n-------------------\n")

    for i in range(len(amrap_ex)):
        print(f"{reps[0]} {exr[0]}\n")
        exr.pop(0)
        reps.pop(0)

    return ''


def emom():
    """Generates EMOM (Every Minute on the Minute) Workout"""

    return ''


# -------- Main Prg.-------


# Lists of Exercises/times.
ubm = ['Push-ups', 'Diamond Push-ups', 'Chair Dips', 'Decline Push-ups', 'Handstand Push-ups']
lbm = ['Air Squat', 'Jump Squat', 'Lunges', 'Lateral Squat', 'Calf Raise', 'Pistols']
fbm = ['Burpees', 'High Knees', 'Leg Rises', 'V ups']
cor = ['Plank', 'Mountain Climbers']
tme = ['5', '10', '15', '20', '25', '30']

test1 = amrap()
print(test1)
test2 = emom()
print(test2)
