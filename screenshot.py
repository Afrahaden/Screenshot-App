import time
import pyautogui
import os
import tkinter as tk
from tkinter import filedialog    


class ScreenshotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Screenshot App")
        self.master.geometry("270x120")

        self.screenshot_button = tk.Button(self.master, text="Take Screenshot", width=20, command=self.screenshot, fg="white", bg="blue")
        self.screenshot_button.pack(pady=10)

        self.select_directory_button = tk.Button(self.master, text="Select Directory", width=20, command=self.select_directory, fg="white", bg="green")
        self.select_directory_button.pack(pady=10)

        # Set the default directory to the user's home directory
        self.directory = os.path.expanduser("~")

    def screenshot(self):
        os.makedirs(self.directory + '/screenshotsData', exist_ok=True)

        # Create a unique filename for the screenshot
        name = int(round(time.time() * 1000))
        name = self.directory + '/screenshotsData/{}.png'.format(name)

        # Wait for 5 seconds to allow the user to switch to the desired screen
        time.sleep(5)

        # Take the screenshot and save it to the specified directory
        img = pyautogui.screenshot(name)
        img.show()

    def select_directory(self):
        # Allow the user to select a directory and store it in self.directory
        self.directory = filedialog.askdirectory()

root = tk.Tk()
app = ScreenshotApp(root)
root.mainloop()
