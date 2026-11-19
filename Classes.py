import customtkinter as ctk


class GreetApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("GreetApp")
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


class GridApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("GridApp")
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

    def get(self):
        checked_checkboxses = []
        if self.checkbox1.get() == 1:
            checked_checkboxses.append(self.checkbox1.cget("text"))
        if self.checkbox2.get() == 1:
            checked_checkboxses.append(self.checkbox2.cget("text"))
        if self.checkbox3.get() == 1:
            checked_checkboxses.append(self.checkbox3.cget("text"))
        return checked_checkboxses


class MyDynamicCheckBoxFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxses = []

        self.title = ctk.CTkLabel(
            self, text=self.title, fg_color="gray30", corner_radius=6
        )
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxses.append(checkbox)

    def get(self):
        checked_checkboxses = []
        for checkbox in self.checkboxses:
            if checkbox.get() == 1:
                checked_checkboxses.append(checkbox.cget("text"))
        return checked_checkboxses


class FrameApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("FrameApp")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")
        self.checkbox_frame2 = MyCheckboxFrame(self)
        self.checkbox_frame2.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsw")

        self.button = ctk.CTkButton(
            self, text="my button", command=self.button_callback
        )
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def button_callback(self):
        print("Checked checkboxses: ", self.checkbox_frame.get())


class DynamicFrameApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("DynamicFrameApp")
        self.geometry("400x220")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame1 = MyDynamicCheckBoxFrame(
            self, "Values", values=["value 1", "value 2", "value 3"]
        )
        self.checkbox_frame1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.checkbox_frame2 = MyDynamicCheckBoxFrame(
            self, "Options", values=["Option 1", "Option 2"]
        )
        self.checkbox_frame2.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")

        self.button = ctk.CTkButton(
            self, text="my button", command=self.button_callback
        )
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def button_callback(self):
        print("Checked checkboxses: ", self.checkbox_frame1.get())
        print("Checked checkboxses: ", self.checkbox_frame2.get())


class LoginForm(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Login Form")
        self.geometry("400x300")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(5, weight=1)

        self.entry = ctk.CTkEntry(self, placeholder_text="Enter your username.")
        self.entry.grid(row=1, column=0, padx=20, pady=(0, 5), sticky="ew")
        self.entry.bind("<Return>", self.signin)

        self.entry2 = ctk.CTkEntry(
            self, placeholder_text="Enter your password.", show="*"
        )
        self.entry2.grid(row=2, column=0, padx=20, pady=5, sticky="ew")
        self.entry2.bind("<Return>", self.signin)

        self.button = ctk.CTkButton(self, text="Login", command=self.signin)
        self.button.grid(row=3, column=0, padx=20, pady=(5, 10), sticky="ew")

        self.label = ctk.CTkLabel(self, text="")
        self.label.grid(row=4, column=0, padx=20, pady=(5, 0))

    def signin(self, event=None):
        username = self.entry.get().strip()
        password = self.entry2.get()

        if username == "Dan" and password == "1234":
            self.label.configure(text=f"Hello, {username}!")
        else:
            self.label.configure(text="Username or Password are incorrect.")

    def destroy(self):
        for after_id in self.tk.eval("after info").split():
            self.after_cancel(after_id)
        super().destroy()
