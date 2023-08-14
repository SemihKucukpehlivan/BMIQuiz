import tkinter

#window
window = tkinter.Tk()
window.minsize(width=300, height=150)
window.title("BMI CALCULATOR")

# kg_label
kg_label = tkinter.Label(text="Enter Your Weight(kg)")
kg_label.config(fg="black")
kg_label.grid(padx=141,pady=3)

# kg_entry
kg_entry = tkinter.Entry(width=18)
kg_entry.grid(padx=141,pady=3)

# cm_label
cm_label = tkinter.Label(text="Enter Your Height(cm)")
cm_label.config(fg="black")
cm_label.grid(padx=141,pady=3)

# cm_entry
cm_entry = tkinter.Entry(width=15)
cm_entry.grid(padx=141,pady=3)


# calculateButton
def calculateButton():

    if not kg_entry.get() or not cm_entry:
        result_label.config(text="Please enter both weight and height.")
    else:
        try:
            weight = float(kg_entry.get())
            height = float(cm_entry.get())
        except ValueError:
            print("Please enter valid number")
        else:
            check_entry(weight, height)

#check entry
def check_entry(weight, height):
    try:
        weight = float(weight)
        height = float(height)
    except ValueError:
        print("Please enter valid number")
    else:
        bmi = calculateBMI(weight, height)


#calculate BMI
def calculateBMI(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    if bmi < 18.5:
        result_label.config(text="Underweight")
    elif 18.5 <= bmi < 24.9:
        result_label.config(text="Normal")
    elif 25 <= bmi < 29.9:
        result_label.config(text="Overweight")
    elif 30 <= bmi < 34.9:
        result_label.config(text="1st degree obese")
    elif 35 <= bmi < 39.9:
        result_label.config(text="2nd degree obese.")
    else:
        result_label.config(text="3rd degree obese")

    return bmi

#calculate_button
calculate_button = tkinter.Button(text="Calculate", command=calculateButton)
calculate_button.grid(padx=141,pady=3)

#resutl label
result_label = tkinter.Label(text="", fg="black")
result_label.grid(pady=3)


window.mainloop()
