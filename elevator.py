import tkinter as tk

class ElevatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Elevator")

        # Create buttons for the three doors
        self.button_a = tk.Button(master, text="Door A", command=lambda: self.show_keypad("A"))
        self.button_a.pack(side=tk.LEFT)
        self.button_b = tk.Button(master, text="Door B", command=lambda: self.show_keypad("B"))
        self.button_b.pack(side=tk.LEFT)
        self.button_c = tk.Button(master, text="Door C", command=lambda: self.show_keypad("C"))
        self.button_c.pack(side=tk.LEFT)

        # Create keypad window
        self.keypad = tk.Toplevel(master)
        self.keypad.title("Floor Number")
        self.keypad.withdraw() # Hide keypad window initially
        self.keypad_buttons = []
        for i in range(1, 13):
            if i <= 4:
                door = "A"
            elif i <= 8:
                door = "B"
            else:
                door = "C"
            if door == "A" and i <= 4 or door == "B" and 5 <= i <= 8 or door == "C" and i >= 9:
                button = tk.Button(self.keypad, text=str(i), width=3, command=lambda x=i: self.select_floor(x))
                button.grid(row=(i-1)//3, column=(i-1)%3)
                self.keypad_buttons.append(button)

        # Initialize current and destination floors to 0
        self.current_floor = 0
        self.dest_floor = 0

        # Create label to display current and destination floors
        self.label = tk.Label(master, text="")
        self.label.pack()

    # Handler function for door button clicks
    def show_keypad(self, door):
        self.current_door = door
        for button in self.keypad_buttons:
            button.destroy() # Destroy old buttons
        self.keypad_buttons.clear() # Clear list of buttons
        for i in range(1, 13):
            if door == "A" and i <= 4 or door == "B" and 5 <= i <= 8 or door == "C" and i >= 9:
                button = tk.Button(self.keypad, text=str(i), width=3, command=lambda x=i: self.select_floor(x))
                button.grid(row=(i-1)//3, column=(i-1)%3)
                self.keypad_buttons.append(button)
        self.keypad.deiconify() # Show keypad window

    # Handler function for floor button clicks
    def select_floor(self, floor_num):
        print(f"Elevator going from floor {self.current_floor} to floor {floor_num} from door {self.current_door}")
        self.current_floor = floor_num
        self.dest_floor = floor_num
        self.label.config(text=f"Current floor: {self.current_floor}, Destination floor: {self.dest_floor}")
        self.keypad.withdraw() # Hide keypad window after floor number is selected

root = tk.Tk()
my_gui = ElevatorGUI(root)
root.mainloop()
