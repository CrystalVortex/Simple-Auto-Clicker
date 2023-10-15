import tkinter as tk
from tkinter import ttk
import pyautogui
import keyboard

class AutoClicker:
    def __init__(self, cps, click_delay, time_unit):
        self.cps = cps
        self.click_delay = click_delay
        self.time_unit = time_unit
        self.left_click = True  # Default to left click
        self.running = False

    def start_clicking(self):
        self.running = True
        self.click()

    def click(self):
        if self.running:
            if self.left_click:
                pyautogui.click(button='left')
            else:
                pyautogui.click(button='right')
            self.after_click()

    def after_click(self):
        if self.time_unit == "ms":
            delay = self.click_delay / 1000
        elif self.time_unit == "minutes":
            delay = self.click_delay * 60
        elif self.time_unit == "hours":
            delay = self.click_delay * 60 * 60
        elif self.time_unit == "days":
            delay = self.click_delay * 60 * 60 * 24

        self.root.after(int(delay * 1000), self.click)

    def stop_clicking(self):
        self.running = False

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        self.root = parent
        self.autoclicker = None
        self.autoclicker_running = False

        self.LabelAmountOfCPS = ttk.Label(self, text="Amount of Clicks:")
        self.LabelAmountOfCPS.pack(side="top", pady=15)

        self.InputAmountOfCPS = ttk.Entry(self)
        self.InputAmountOfCPS.insert(0, "1")
        self.InputAmountOfCPS.pack(side="top", pady=10)

        LabelClickDelay = ttk.Label(self, text="Click Delay:")
        LabelClickDelay.pack(side="top", pady=5)

        self.InputClickDelay = ttk.Entry(self)
        self.InputClickDelay.insert(0, "100")
        self.InputClickDelay.pack(side="top", pady=5)

        LabelTimeUnit = ttk.Label(self, text="Time Unit:")
        LabelTimeUnit.pack(side="top", pady=5)

        self.TimeUnitCombo = ttk.Combobox(self, values=["ms", "minutes", "hours", "days"])
        self.TimeUnitCombo.set("ms")
        self.TimeUnitCombo.pack(side="top", pady=5)

        self.ClickToggle = ttk.Checkbutton(self, text="Left Click")
        self.ClickToggle.pack(side="top", pady=5)

        self.LabelInfo = ttk.Label(self,text="Use: Alt+Shift+Q to start or click start")
        self.LabelInfo.pack(side="bottom",pady=15)

        self.StartStopButton = ttk.Button(self, text="Start Autoclicker", command=self.toggle_autoclicker)
        self.StartStopButton.pack(side="bottom", pady=0)

        # Register the hotkey
        keyboard.add_hotkey('shift+alt+q', self.toggle_autoclicker)

    def toggle_autoclicker(self):
        if self.autoclicker_running:
            self.stop_autoclicker()
        else:
            self.start_autoclicker()

    def start_autoclicker(self):
        cps = float(self.InputAmountOfCPS.get())
        click_delay = float(self.InputClickDelay.get())
        time_unit = self.TimeUnitCombo.get()

        if cps <= 0 or click_delay < 0:
            # Invalid input, prevent starting
            return

        self.autoclicker = AutoClicker(cps, click_delay, time_unit)
        self.autoclicker.left_click = self.ClickToggle.instate(['selected'])
        self.autoclicker.root = self.root

        self.autoclicker.start_clicking()

        self.autoclicker_running = True
        self.StartStopButton["text"] = "Stop Autoclicker"

    def stop_autoclicker(self):
        if self.autoclicker:
            self.autoclicker.stop_clicking()

            self.autoclicker_running = False
            self.StartStopButton["text"] = "Start Autoclicker"

root = tk.Tk()
root.title("Auto Clicker")

# Simply set the theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")

app = App(root)
app.pack(fill="both", expand=True)

# Set a minsize for the window, and place it in the middle
root.update()
root.resizable(width=False, height=False)
root.minsize(root.winfo_width(), root.winfo_height())
root.geometry("250x500")

app.mainloop()
