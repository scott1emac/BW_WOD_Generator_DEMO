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

    a = ""

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

    a += f"\n{t} MINUTE AMRAP OF:\n-------------------\n"

    for i in range(len(amrap_exr)):
        a += f"{reps[0]} {exr[0]}\n"
        exr.pop(0)
        reps.pop(0)

    return amrap_str.set(a)


def emom():
    """Generates EMOM (Every Minute on the Minute) Workout"""

    e = ''

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

    e += f"\n{t} MINUTE EMOM OF:\n-------------------\n"

    for i in range(len(emom_exr)):
        e += f"{reps[0]} {exr[0]}\n"
        exr.pop(0)
        reps.pop(0)

    return emom_str.set(e)


def hero():
    """Generates Hero Workout"""

    text_return = ''

    # Generates random Hero Workout.
    h = hro[rd.randint(0, len(hro) - 1)]

    text_return += f"\nHERO:\n-------------------\n"

    hero_exr = h
    hero_exr = hero_exr.split(',')
    hero_exr = list(hero_exr)

    # Generates Hero Workout text return.
    for i in range(len(hero_exr)):
        text_return += f"{hero_exr[0]}"
        hero_exr.pop(0)

    return hero_str.set(text_return)


def chp():
    """Generates Chipper Workout"""
    text_return = ''

    # Generates random chipper workout.
    c = chip[rd.randint(0, len(chip) - 1)]

    text_return += "\nCHIPPER:\n-------------------\n"

    # Splits the workout for formatting.

    chp_exr = c
    chp_exr = chp_exr.split(',')
    chp_exr = list(chp_exr)

    # Generates Chipper Workout text return.
    for i in range(len(chp_exr)):
        text_return += f"{chp_exr[0]}"
        chp_exr.pop(0)

    return chp_str.set(text_return)


def random():
    """Generates random AMRAP, EMOM, HERO, or CHIPPER workout"""

    rnd = [1, 2, 3, 4]

    r = rnd[rd.randint(0, len(rnd) - 1)]

    if r == 1:
        amrap()
    if r == 2:
        emom()
    if r == 3:
        hero()
    if r == 4:
        chp()

    rnd_exr = r

    return rnd_str.set(str(rnd_exr))


def ext():
    """Closes the Program"""
    exit()


# -------- Main Prg.-------

# Lists of Exercises/times.
ubm = ['Push-ups', 'Diamond Push-ups', 'Chair Dips', 'Decline Push-ups', 'Handstand Push-ups']
lbm = ['Air Squat', 'Jump Squat', 'Lunges', 'Lateral Squat', 'Calf Raise', 'Pistols']
fbm = ['Burpees', 'High Knees', 'Leg Rises', 'V ups']
cor = ['Plank', 'Mountain Climbers']
hro = ['Murph:\n, 1 Mile run\n, 100 Pull-ups\n, 200 Push-Ups\n, 300 Squats\n, 1 Mile run',
       'Monsoor:\n, 20 Sit-ups w/ 8 second contractions\n, 50 Push-Ups\n, Side-Bridge/Plank/Side-Bridge: Hold for 8 '
       'sec.'
       'for a total of 5 mins.\n,50 Push-Ups,100 Mountain Climbers',
       'Tellier:\nFOR TIME:\n, 10 Burpees/25 Push-Ups\n, 10 Burpees/25 Push-Ups/50 Lunges\n, 10 Burpees/25 Push-Ups/50 '
       'Lunges/100 Sit-Ups\n, 10 Burpees/25 Push-Ups/50 Lunges/100 Sit-Ups/ 150 Squats',
       'Whiting:\nAMRAP:\n, 1 Mile Run\n, 5 rounds of:\n27 Squats\n18 Push-Ups, \nIf you finish, Start on the run '
       'again.']
chip = ['10 Handstand Push-ups\n, 20 burpees\n, 40 Jumping Lunges',
        '100 Air Squats\n, 90 Sit-ups\n, 80 Lunges\n, 70 Burpees\n, 60 second plank\n, 50 Mountain Climbers\n, '
        '40 Push-ups\n,'
        '20 Jump Squats',
        '100 Pull-ups\n, 100 Push-ups\n, 100 Sit-ups\n, 100 Squats\n']
tme = ['5', '10', '15', '20', '25', '30']

# ----Tkinter utilities----
# Font and Size for buttons and text response.
exrDisplay = 'Ariel 18'

# ----Welcome Banner----
print("Body Weight WOD Generator v1.0")

# ----Initialize GUI----
root = ttk.Window(themename='darkly')
root.title("BW_WOD_GENERATOR v1.0")
root.geometry('480x720')

# String Var for initialization of Tkinter Buttons
amrap_str = tk.StringVar()
emom_str = tk.StringVar()
hero_str = tk.StringVar()
chp_str = tk.StringVar()
rnd_str = tk.StringVar()

# Title Display//Text, Font, and Size Control of GUI.
title_label = ttk.Label(root, text='BODYWEIGHT WOD GENERATOR v1.0', font='Arial, 16 bold underline')
title_label.pack(padx=20, pady=20)

btn_frame = ttk.Frame(root)
btn_frame.columnconfigure(0, weight=1)
btn_frame.columnconfigure(1, weight=1)
btn_frame.columnconfigure(2, weight=1)

# AMRAP Button.
btn1 = ttk.Button(btn_frame, text='AMRAP', command=amrap, compound='top')
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

# EMOM Button.
btn2 = ttk.Button(btn_frame, text='EMOM', command=emom, compound='top')
btn2.grid(row=0, column=2, sticky=tk.W + tk.E)

# Hero Button.
btn3 = ttk.Button(btn_frame, text='HERO', command=hero, compound='center')
btn3.grid(row=1, column=0, sticky=tk.W + tk.E)

# CHIPPER Button.
btn4 = ttk.Button(btn_frame, text='CHIP', command=chp, compound='left')
btn4.grid(row=1, column=1, sticky=tk.W + tk.E)

# Random Workout Select.
btn5 = ttk.Button(btn_frame, text='RAND', command=random, compound='right')
btn5.grid(row=1, column=2, sticky=tk.W + tk.E)

# Button Frame Pack
btn_frame.pack(fill='x')

# -------- Button Outputs --------

btn_output_frame = tk.Frame(root)

# Button 1 (AMRAP)
btn1_output = tk.Label(btn_output_frame,
                       font=exrDisplay,
                       textvariable=amrap_str,
                       anchor='center')
btn1_output.pack()

# Button 2 (EMOM)
btn2_output = tk.Label(btn_output_frame,
                       font=exrDisplay,
                       textvariable=emom_str,
                       anchor='center')
btn2_output.pack()

# Button 3 (HERO)
btn3_output = tk.Label(btn_output_frame,
                       font=exrDisplay,
                       textvariable=hero_str,
                       anchor='center')
btn3_output.pack()

# Button 4 (CHIPPER)
btn4_output = tk.Label(btn_output_frame,
                       font=exrDisplay,
                       textvariable=chp_str,
                       anchor='center')
btn4_output.pack()

# Button 5 (RANDOM)

btn_output_frame.pack()
# Exit Frame
ext_frame = tk.Frame(root)
ext_frame.columnconfigure(0, weight=1)

# Exit Button
ext_btn = tk.Button(ext_frame, text='CLOSE', command=ext)
ext_btn.grid(row=0, column=0, sticky=tk.W + tk.E)

# Exit Frame Pack
ext_frame.pack(pady=20, side='bottom', fill='x')

# Run GUI
root.mainloop()
