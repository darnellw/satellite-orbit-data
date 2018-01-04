'''
Widget to calculate orbiting body information given planet mass, satellite mass,
and orbit radius. Assumes circular orbits.

Script by darnellw
github.com/darnellw

References:
Physics and equations: www.physicsclassroom.com
Physics and equations: hyperphysics.phy-astr.gsu.edu
International Space Station data: https://www.space.com/16748-international-space-station.html
'''

import sys
import math
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Global constants
GRAV_CONST = 6.673e-11
PI = 3.14159265

# Closes the program
def quit_app():
    root.quit()

# Clears the fields
def clear_fields():
    txt_plan_mass.delete(0, "end")
    txt_sat_mass.delete(0, "end")
    txt_radius.delete(0, "end")
    list_output.delete(0, "end")

# Show "Help" window
def show_help():
    message = "This program accepts planet mass, satellite mass, and orbit "
    message += "radius as input. It then calculates and displays data about "
    message += "the orbiting satellite. This program assumes circular orbits."
    message += "\n\n"
    message += "Planet mass: the mass of the planet in which the satellite "
    message += "orbits, in kilograms.\n"
    message += "Satellite mass: the mass of the satellite, in kilograms.\n"
    message += "Orbit radius: the distance from the center of the planet to "
    message += "the center of the satellite, in meters.\n\n"
    message += "All fields accept scientific notation (ex.: 5.972e24)"
    messagebox.showinfo("About", message)

# Show "About" window
def show_about():
    message = "Version 0.1.0\n"
    message += "github.com/darnellw\n\n"
    message += "References:\n"
    message += "www.physicsclassroom.com\n"
    message += "hyperphysics.phy-astr.gsu.edu"
    message += "https://www.space.com/16748-international-space-station.html"
    messagebox.showinfo("About", message)

# Calculate and display data
def calc():
    try:
        plan_mass = float(txt_plan_mass.get())
        sat_mass = float(txt_sat_mass.get())
        radius = float(txt_radius.get())

        clear_fields()

        sat_velocity = math.sqrt(GRAV_CONST * plan_mass / radius)
        sat_velocity = format(sat_velocity, '.4E')

        sat_period = math.sqrt((4 * radius**3 * PI**2)/(GRAV_CONST * plan_mass)) / 3600
        sat_period = format(sat_period, '.4E')

        sat_acc = GRAV_CONST * plan_mass / radius**2
        sat_acc = format(sat_acc, '.4E')

        plan_mass = format(plan_mass, '.4E')
        sat_mass = format(sat_mass, '.4E')
        radius = format(radius, '.4E')

        list_output.insert(END,
            "Planet Mass: " + plan_mass + " kg",
            "Satellite Mass: " + sat_mass + " kg",
            "Orbit Radius: " + radius + " m",
            "Sat. Velocity: " + sat_velocity + " m/s",
            "Sat. Period: " + sat_period + " hours",
            "Sat. Acceleration: " + sat_acc + (u" m/s\u00B2")
        )

    except:
        message = "Error performing calculations."
        messagebox.showwarning("Error", message)
        clear_fields()

root = Tk()
root.title("Orbit Data")
root.resizable(width=False, height=False)

# Menu
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Clear", command=clear_fields)
menu_file.add_command(label="Quit", command=quit_app)
menu.add_cascade(label="File", menu=menu_file)

menu_help = Menu(menu, tearoff=0)
menu_help.add_command(label="Help", command=show_help)
menu_help.add_command(label="About", command=show_about)
menu.add_cascade(label="Help", menu=menu_help)

root.config(menu=menu)

# Frame structure
frame_left = LabelFrame(root, text="Input Data")
frame_left.grid(row=0, column=0, padx=4, pady=4)
frame_right = LabelFrame(root, text="Output")
frame_right.grid(row=0, column=1, rowspan=2, padx=4, pady=4)
frame_bottom = Frame(root)
frame_bottom.grid(row=1, column=0, padx=4, pady=8)

# Left frame contents
# Label and textbox for planet mass
Label(frame_left, text="Planet Mass").grid(row=0, column=0, padx=4, pady=2, sticky=E)
txt_plan_mass = Entry(frame_left)
txt_plan_mass.grid(row=0, column=1, padx=4, pady=2)
Label(frame_left, text="kg").grid(row=0, column=2, padx=4, pady=2, sticky=W)

# Label and textbox for satellite mass
Label(frame_left, text="Satellite Mass").grid(row=1, column=0, padx=4, pady=2, sticky=E)
txt_sat_mass = Entry(frame_left)
txt_sat_mass.grid(row=1, column=1, padx=4, pady=2)
Label(frame_left, text="kg").grid(row=1, column=2, padx=4, pady=2, sticky=W)

# Label and textbox for orbit radius
Label(frame_left, text="Orbit Radius").grid(row=2, column=0, padx=4, pady=2, sticky=E)
txt_radius = Entry(frame_left)
txt_radius.grid(row=2, column=1, padx=4, pady=2)
Label(frame_left, text="m").grid(row=2, column=2, padx=4, pady=2, sticky=W)

# Right frame contents
# Listbox and scrollbar for output
list_output = Listbox(frame_right, activestyle="none", width=35, height=8, takefocus=0)
list_output.grid(row=0, column=0, padx=4, pady=4, sticky=N+S)
scroll = Scrollbar(frame_right, orient=VERTICAL, takefocus=0)
scroll.grid(row=0, column=0, sticky=N+S+E)

# Attach scrollbar to listbox
list_output['yscrollcommand'] = scroll.set
scroll['command'] = list_output.yview

# Buttons
btn_calc = Button(frame_bottom, text="Calculate", command=calc)
btn_calc.grid(row=0, column=0, padx=4)
btn_clear = Button(frame_bottom, text="Clear", command=clear_fields)
btn_clear.grid(row=0, column=1, padx=4)
btn_exit = Button(frame_bottom, text="Exit", command=quit_app)
btn_exit.grid(row=0, column=2, padx=4)

# International Space Station default data
txt_plan_mass.insert(0, "5.972e24")
txt_sat_mass.insert(0, "391000")
txt_radius.insert(0, "6770000")

# Main loop to keep window open
root.mainloop()
