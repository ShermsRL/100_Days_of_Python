import tkinter


def calculate():
    miles = float(mile_input.get())
    km = miles * 1.609344
    dp_km = round(km, 2)
    converted_km.config(text=dp_km)

window = tkinter.Tk()
window.title("Mile to KM Converter")

# Label
mile_label = tkinter.Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)

converted_km = tkinter.Label(text="0")
converted_km.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

# Entry
mile_input = tkinter.Entry()
mile_input.grid(column=1, row=0)

# Button
calculate = tkinter.Button(text="Calculate", command=calculate)
calculate.grid(column=1, row=2)

window.mainloop()
