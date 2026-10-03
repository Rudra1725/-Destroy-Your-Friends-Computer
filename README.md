# Fullscreen Black Screen with Tkinter

This Python script creates a **fullscreen, black window** using the built-in `tkinter` library.  
It is designed to cover the entire screen and stay on top of all other windows.  
The close button (❌) is disabled to prevent the user from closing the window manually.

---

## 🧠 Features

- Launches a **borderless fullscreen** black window.  
- Stays **always on top** of all other applications.  
- Disables the **window close button** to prevent accidental exit.  
- Uses only the **standard Python library** (no external dependencies).

---

## 🧩 Code Overview

```python
import tkinter 

root = tkinter.Tk()
root.attributes('-fullscreen', True)    # Enable fullscreen
root.attributes('-topmost', True)       # Keep window on top
root.config(bg='black')                 # Set background color to black
root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable close button
root.mainloop()                         # Run the Tkinter event loop
```


---

## 🚀 How to Run

1. Make sure you have **Python 3.x** installed.
2. Save the code to a file, for example:

   ```
   fullscreen_black.py
   ```
3. Run the file from the terminal or command prompt:

   ```bash
   python fullscreen_black.py
   ```
4. To **exit**, you’ll need to use a system shortcut (like `Alt + F4` on Windows or `Command + Q` on macOS).

---

## ⚠️ Why This Code May Not Work Perfectly on macOS

On macOS, `Tkinter`’s handling of fullscreen and window layering is **different from Windows and Linux**. The following issues may occur:

* The `-fullscreen` attribute may **not truly hide the menu bar or dock**.
* The `-topmost` attribute is **not always respected** by macOS’s window manager (the window might go behind other apps).
* The `WM_DELETE_WINDOW` override can still be bypassed via the macOS “Force Quit” dialog.

### ✅ What to Do on macOS

To make this work more reliably on macOS:

1. Replace:

   ```python
   root.attributes('-fullscreen', True)
   ```

   with:

   ```python
   root.attributes('-zoomed', True)
   ```

   (This makes the window fill the screen more consistently.)

2. Add the following lines before `root.mainloop()`:

   ```python
   root.lift()
   root.focus_force()
   ```

3. Make sure you’re using **Python installed via python.org**, not the **macOS system Python**, as Tkinter behaves inconsistently with the system version.
