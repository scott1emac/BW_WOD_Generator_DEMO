# --BW WOD GENERATOR v1.0--
import random as rd
import tkinter as tk
import ttkbootstrap as ttk


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

    # length of input list(reps).
    r = len(reps)

    # Generates and appends rep range for exercise to r_num for return.
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

    a = ''

    a += f"\n{t} MINUTE AMRAP OF:\n-------------------\n"

    for i in range(len(amrap_exr)):
        a += f"{reps[0]} {exr[0]}\n"
        exr.pop(0)
        reps.pop(0)

    return a


def click():
    am = amrap()
    amrap_str.set(am)


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
rnd = ['HERO', 'AMRAP', 'EMOM', 'CHIPPER']

# ----Tkinter utilities----
# Font and Size for buttons and response.
f = 'Ariel 10'

# ----Welcome Banner----
print("Body Weight WOD Generator v1.0")

# ----Initialize GUI----
window = ttk.Window(themename='darkly')
window.title("BW_WOD_GENERATOR v1.0")
window.geometry('500x500')

# Title Display//Text, Font, and Size Control of GUI.
title_label = ttk.Label(master=window, text='BODYWEIGHT WOD GENERATOR v1.0', font='Arial, 12 bold')
title_label.pack(padx=20, pady=20)

# Input Field Button(s)f
input_frame = ttk.Frame(master=window)
input_frame.columnconfigure(0, weight=3)
input_frame.columnconfigure(1, weight=1)
input_frame.columnconfigure(2, weight=1)
input_frame.columnconfigure(3, weight=1)

# btn1 (Exit Button)
btn1 = ttk.Button(master=input_frame, text='amrap', command=amrap)
btn1.pack()

input_frame.pack()

# Output btn1 (Exit Button).
amrap_str = tk.StringVar()
output_label = ttk.Label(
    master=window,
    textvariable=amrap_str,
    font=f)

output_label.pack()

# Run GUI
window.mainloop()
