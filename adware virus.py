#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import threading
import time

def show_ad():
    def popup():
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Advertisement", "This is an demo of an Ad Popup")
        root.destroy()
    # Run popup in a separate thread to avoid blocking
    threading.Thread(target=popup).start()

def ad_loop():
    while True:  # Infinite loop to keep showing ads
        show_ad()
        time.sleep(3)  # Pause for 10 seconds before next ad

if __name__ == "__main__":
    print("Starting real-time Educational Adware Demo. Press Ctrl+C to stop.")
    ad_thread = threading.Thread(target=ad_loop, daemon=True)
    ad_thread.start()
    # Keep main thread alive to let ad thread run
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDemo stopped by user.")
