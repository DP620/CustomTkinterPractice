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


class gridApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x150")

        self.button = ctk.CTkButton(
            self, text="my button", command=self.button_callback
        )
        self.button.grid(row=0, column=0, padx=20, pady=20)

    def button_callback(self):
        print("Button pressed")
