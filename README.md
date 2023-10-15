# Auto Clicker

This is a simple Auto Clicker application built using Python and Tkinter GUI library. It allows users to automate mouse clicks at a specified rate and interval.

## Features

- **Click Rate**: Users can set the number of clicks per second.
- **Click Delay**: Set the delay between each click.
- **Time Units**: Choose between milliseconds, minutes, hours, or days for the click delay.
- **Left/Right Click**: Toggle between left and right mouse clicks.
- **Start/Stop**: Easily start and stop the auto clicker with a button or by using the hotkey (Shift + Alt + Q).
- **Native GUI**: Utilizes Tkinter for a simple and intuitive user interface.

## How to Use

1. Launch the application.
2. Specify the desired Click Rate and Click Delay.
3. Select the desired Time Unit for the Click Delay.
4. Choose between Left Click and Right Click.
5. Click the "Start Autoclicker" button to initiate the auto clicking.
6. Use the hotkey (Shift + Alt + Q) to start/stop the auto clicker.

## Notes

- Ensure that the application is run with the necessary permissions to allow automated mouse clicking.
- Use responsibly and avoid excessive or inappropriate use.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with most Python installations)

## Building the Executable

To create an executable file for the Auto Clicker, you can use a tool like PyInstaller. This will package the Python script and its dependencies into a standalone executable.

Example command for PyInstaller:

```bash
pyinstaller --onefile AutoClicker.py
