import tkinter
from tkinter import *
from tkinter import messagebox

background = "#F0EB8D"

window = Tk()
window.title("Workout_Trakcer")
window.minsize(height=300, width=600)
window.config(padx=100,pady=50, background=background)

#-----------------BACKEND------------------

try:
    def save():
        listbox_text = listbox.get(listbox.curselection())
        spinbox_text = reps.get()
        day_text = day_input.get()
        weight_text = weight_input.get()

        if day_text == "" or weight_text == "":
            messagebox.showinfo(title="warning", message="Hey you have left some fields empty!")
        else:
            is_ok = messagebox.askokcancel(title="confirmation", message="Is it ok to save the details?")
            if is_ok:
                f = open("workout_track.txt", "a")
                f.write(f" Day: {day_text} | Workout: {listbox_text} | Weight: {weight_text} | Reps: {spinbox_text}\n")
                weight_input.delete(0, END)
except "_tkinter.TclError: bad listbox index "": must be active, anchor, end, @x,y, or a number":
    pass

#labels
select_day = Label(text="Add Day:")
select_day.grid(column=1, row=1)
select_day.config(pady=10)
select_day.configure(background=background)

select_workout = Label(text="Select workout:")
select_workout.grid(column=1, row=3)
select_workout.config(pady=10)
select_workout.configure(background=background)

select_reps = Label(text="Reps:")
select_reps.grid(column=1, row=5)
select_reps.config(pady=10)
select_reps.configure(background=background)

select_weight = Label(text="Weight:")
select_weight.grid(column=1, row=7)
select_weight.config(pady=10)
select_weight.configure(background=background)

#Inputs
day_input = Entry(width=22)
day_input.grid(column=2, row=1)


weight_input = Entry(width=22)
weight_input.grid(column=2, row=7)



#list_box

listbox = Listbox(height=3)
workouts = ["Pushups", "Chest_press", "Chest_machine_fly", "Decline_dumbels_press",
          "shoulder_press", "lateral_raise", "reverse_machine_fly", "shoulder_shrugs", "triceps_pushdown", "Dumbbel_over_headExtension", "Rope_pushdown"]
for workout in workouts:
    listbox.insert(workouts.index(workout), workout)
listbox.bind("<<ListboxSelect>>")
listbox.grid(column=2, row=3)

#spin_box
reps = Spinbox(from_=1,to=50)
reps.grid(column=2, row=5)

#buttons
confirm_button = Button(text="SAVE", command=save)
confirm_button.grid(column=2, row=9)
confirm_button.configure(activebackground="blue")




window.mainloop()
