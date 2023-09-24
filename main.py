# BW WOD GENERATOR v1.0
import random as rd


# -------- Functions -------
def user():
    """Validates User Input and Error Handling. """

    user_sel = input("Select workout type: AMRAP/EMOM/Chipper/Hero ..or exit\n")
    user_sel.capitalize()

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


def chp():
    """Generates EMOM (Every Minute on the Minute) Workout"""

    c = chip[rd.randint(0, len(chip) - 1)]

    print("\nCHIPPER:\n-------------------\n")

    c = c.split(',')

    for i in c:
        print(i.lstrip())

    return ''


def hero():
    """Generates EMOM (Every Minute on the Minute) Workout"""

    h = hro[rd.randint(0, len(hro) - 1)]

    print("\nHERO:\n-------------------\n")

    h = h.split(',')

    for i in h:
        print(i.lstrip())

    return ''


# -------- Main Prg.-------


# Lists of Exercises/times.
ubm = ['Push-ups', 'Diamond Push-ups', 'Chair Dips', 'Decline Push-ups', 'Handstand Push-ups']
lbm = ['Air Squat', 'Jump Squat', 'Lunges', 'Lateral Squat', 'Calf Raise', 'Pistols']
fbm = ['Burpees', 'High Knees', 'Leg Rises', 'V ups']
cor = ['Plank', 'Mountain Climbers']
hro = ['Murph:, 1 Mile run, 100 Pull-ups, 200 Push-Ups, 300 Squats, 1 Mile run',
       'Monsoor:, 20 Sit-ups w/ 8 second contractions, 50 Push-Ups, Side-Bridge/Plank/Side-Bridge: Hold for 8 sec. '
       'for a total of 5 mins.,50 Push-Ups,100 Mountain Climbers',
       'Tellier:\n\nFOR TIME:, 10 Burpees/25 Push-Ups, 10 Burpees/25 Push-Ups/50 Lunges, 10 Burpees/25 Push-Ups/50 '
       'Lunges/100 Sit-Ups, 10 Burpees/25 Push-Ups/50 Lunges/100 Sit-Ups/ 150 Squats',
       'Whiting:\n\nAMRAP:, 1 Mile Run, 5 rounds of:\n27 Squats\n18 Push-Ups, \nIf you finish, Start on the run again.']
chip = ['10 Handstand Push-ups, 20 burpees, 40 Jumping Lunges',
        '100 Air Squats, 90 Sit-ups, 80 Lunges, 70 Burpees, 60 second plank, 50 Mountain Climbers, 40 Push-ups, '
        '20 Jump Squats',
        '100 Pull-ups, 100 Push-ups, 100 Sit-ups, 100 Squats']
tme = ['5', '10', '15', '20', '25', '30']
rnd = ['HERO', 'AMRAP', 'EMOM', 'CHIPPER', 'RFT']

# test1 = amrap()
# print(test1)
# test2 = emom()
# print(test2)
# test3 = chp()
# print(test3)
# test4 = hero()
# print(test4)

# Welcome Banner
print("Body Weight WOD Generator v1.0")

# User input
u = user()

if user_sel == 'AMRAP':
    print(amrap())
if user_sel == 'EMOM':
    print(emom())
if user_sel == 'HERO':
    print(hero())
if user_sel == 'CHIPPER':
    print(chp())
if user_sel == 'EXIT':
    exit()



