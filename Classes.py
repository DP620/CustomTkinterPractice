import customtkinter as ctk


class greetApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Greeting")
        self.geometry("360x180")
        self.grid_columnconfigure(0, weight=1)

        self.entry = ctk.CTkEntry(self, placeholder_text="Enter your name...")
        self.entry.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        self.entry.bind("<Return>", self.greet)

        self.button = ctk.CTkButton(self, text="Say hello!", command=self.greet)
        self.button.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.label = ctk.CTkLabel(self, text="")
        self.label.grid(row=2, column=0, padx=20, pady=(10, 20))

    def greet(self, event=None):
        name = self.entry.get().strip()
        if name:
            self.label.configure(text=f"Hello, {name}!")
        else:
            self.label.configure(text="Please enter your name.")

    def destroy(self):
        for after_id in self.tk.eval("after info").split():
            self.after_cancel(after_id)
        super().destroy()


class gridApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x150")
        self.grid_columnconfigure(0, weight=1)

        self.button = ctk.CTkButton(
            self, text="my button", command=self.button_callback
        )
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        self.checkbox1 = ctk.CTkCheckBox(self, text="Checkbox 1")
        self.checkbox1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
        self.checkbox2 = ctk.CTkCheckBox(self, text="Checkbox 2")
        self.checkbox2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

    def button_callback(self):
        print("Button pressed")


class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.checkbox1 = ctk.CTkCheckBox(self, text="Checkbox 1")
        self.checkbox1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox2 = ctk.CTkCheckBox(self, text="Checkbox 2")
        self.checkbox2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox3 = ctk.CTkCheckBox(self, text="Checkbox 3")
        self.checkbox3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")


class frameApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.button = ctk.CTkButton(
            self, text="my button", command=self.button_callback
        )
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("Button pressed")
