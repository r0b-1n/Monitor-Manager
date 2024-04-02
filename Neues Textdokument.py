import time
import win32gui
import win32con

# Function to move a window to a specific monitor and maximize it
def move_window(window_title, x, y, width, height):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd != 0:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.MoveWindow(hwnd, x, y, width, height, True)
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    else:
        print(f"Window '{window_title}' not found.")

# Main program
if __name__ == "__main__":
    while True:
        # Move first application window to the first monitor and maximize it
        move_window("Papierkorb", 0, 0, 1920, 1080)  # Adjust width and height as needed

        # Move second application window to the second monitor and maximize it
        move_window("Systemsteuerung", 1920, 0, 1920, 1080)  # Adjust width and height as needed

        # Wait for a period of time before checking again (e.g., 1 minute)
        time.sleep(60)
