import tkinter as tk
import time
def update_time():
    # Get current time string in 12-hour format (HH:MM:SS AM/PM)
    # Change "%I:%M:%S %p" to "%H:%M:%S" if you want 24-hour military time
    current_time = time.strftime("%I:%M:%S %p")
    
    # Update the text of the label
    clock_label.config(text=current_time)
    
    # Call this function again after 1000ms (1 second)
    clock_label.after(1000, update_time)

# Set up the main application window
root = tk.Tk()
root.title("Python Digital Clock")
root.geometry("350x150")
root.configure(bg="black")
root.resizable(False, False)

# Style and place the clock text
clock_label = tk.Label(
    root, 
    font=("Helvetica", 36, "bold"), 
    bg="black", 
    fg="#00FF00"  # Retro matrix green color
)
clock_label.pack(expand=True)

# Start the clock loop
update_time()

# Run the window application
root.mainloop()

    play_game()