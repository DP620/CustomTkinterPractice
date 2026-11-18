import customtkinter as ctk


def greet():
    name = entry.get()
    label.configure(text=f"Hello, {name}!")


app = ctk.CTk()
app.title("Greeting")
app.geometry("360x180")
app.grid_columnconfigure(0, weight=1)

entry = ctk.CTkEntry(app, placeholder_text="Your name")
entry.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

button = ctk.CTkButton(app, text="Say hello!", command=greet)
button.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

label = ctk.CTkLabel(app, text="")
label.grid(row=2, column=0, padx=20, pady=(10, 20))

app.mainloop()
