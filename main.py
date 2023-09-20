# BW WOD GENERATOR v1.0
import random as rd


# -------- Functions -------
def exr_base(a, b):
    """Returns a list of placeholders generated from a random range of numbers."""

    # Generates random number of exercises.
    num_exr = rd.randint(a, b)

    # List of randomly generated exercises.
    exr = []

    # Creates empty placeholders in base_exr.
    for i in range(num_exr):
        exr.append('_')

    # Returns list of placeholders.
    return exr


def exr_cycle(phl):
    """Replaces exr_base placeholders in list(l) from other functions with appropriate exercises."""

    # Number of cycles function will perform.
    c = len(phl)

    # Replaces empty placeholders in amrap_ex with exercises from upper body, lower body, and full body lists.
    while c > 0:
        phl[c - 1] = ubm[rd.randint(0, (len(ubm) - 1))]
        if c > 0:
            c -= 1
        phl[c - 1] = lbm[rd.randint(0, (len(lbm) - 1))]
        if c > 0:
            c -= 1
        phl[c - 1] = fbm[rd.randint(0, (len(fbm) - 1))]
        if c > 0:
            c -= 1

    return phl


def exr_reps(reps, a, b):
    """Generates exercise repetitions based on list(reps). """

    r = len(reps)
    r_num = []
    for i in range(r):
        r_num.append(rd.randint(a, b))

    return r_num


def amrap():
    """Generates AMRAP (As Many Rounds As Possible) Workout"""

    # Generates random number of exercises in range(a, b).
    amrap_num = (exr_base(2, 5))

    # Replaces placeholders in list.
    amrap_exr = (exr_cycle(amrap_num))

    # Generates number of reps per exercise.
    amrap_reps = exr_reps(amrap_exr, 8, 12)

    # Generates Time.
    t = tme[rd.randint(2, 5)]

    # Generates AMRAP Text Return
    exr = amrap_exr
    reps = amrap_reps

    print(f"\n{t} MINUTE AMRAP OF:\n-------------------\n")

    for i in range(len(amrap_exr)):
        print(f"{reps[0]} {exr[0]}\n")
        exr.pop(0)
        reps.pop(0)

    return ''


def emom():
    """Generates EMOM (Every Minute on the Minute) Workout"""

    # Generates random number of exercises in range(a, b).
    emom_num = (exr_base(2, 3))

    # Replaces placeholders in list.
    emom_exr = (exr_cycle(emom_num))

    # Generates number of reps per exercise.
    emom_reps = exr_reps(emom_exr, 8, 10)

    # Generates Time from index in list tme.
    t = tme[rd.randint(1, 4)]

    # Generates EMOM Text Return
    exr = emom_exr
    reps = emom_reps

    print(f"\n{t} MINUTE EMOM OF:\n-------------------\n")

    for i in range(len(emom_exr)):
        print(f"{reps[0]} {exr[0]}\n")
        exr.pop(0)
        reps.pop(0)

    return ''


def chp(c):
    pass


# -------- Main Prg.-------


# Lists of Exercises/times.
ubm = ['Push-ups', 'Diamond Push-ups', 'Chair Dips', 'Decline Push-ups', 'Handstand Push-ups']
lbm = ['Air Squat', 'Jump Squat', 'Lunges', 'Lateral Squat', 'Calf Raise', 'Pistols']
fbm = ['Burpees', 'High Knees', 'Leg Rises', 'V ups']
cor = ['Plank', 'Mountain Climbers']
hro = []
chip = ['10 Handstand Push-ups, 20 burpees, 40 Jumping Lunges',
        '100 Air Squats, 90 Sit-ups, 80 Lunges, 70 Burpees, 60 second plank, 50 Mountain Climbers, 40 Push-ups, '
        '20 Jump Squats',
        '100 Pull-ups, 100 Push-ups, 100 Sit-ups, 100 Squats']
tme = ['5', '10', '15', '20', '25', '30']
rnd = ['Hero', 'AMRAP', 'EMOM', 'Chipper', 'RFT']

# test1 = amrap()
# print(test1)
# test2 = emom()
# print(test2)
test3 = chp()
print(test3)
