# Mood of the Day 🌈

## Package Summary
`termcolor` is a lightweight Python package for printing coloured, styled text in the terminal. It helps make console programs clearer — for example, displaying success messages in green, warnings in yellow, and errors in red.  
This mini-project demonstrates how `termcolor` can print motivational messages based on the user’s mood.

---

## Install and Run Instructions
**Prerequisite:** Python 3

1. **Install the required package**
   ```bash
   python3 -m pip install termcolor
---

## Code Explanation
**File to run:** `mood.py`

- **Lines 1 – 6:** Import and setup (`from termcolor import colored`).
- **Lines 8 – 25:** Function `show_mood_message(mood)` decides what message and colour to display based on user input.
- **Lines 10 – 24:** `if / elif / else` handles each mood:
  - *happy → magenta*  
  - *sad → blue*  
  - *angry → red*  
  - *tired → cyan*  
  - *anything else → green*
- **Lines 27 – 29:** Main block prompts the user (`input()`) and calls the function.

✅ One function, one control statement, comments, and the code runs successfully.

---

## Future Idea
If expanded into a bigger project, this package could power a **CLI Wellness Tracker** that:
- Logs moods daily with coloured entries (green = good, yellow = okay, red = rough day).  
- Tracks weekly mood averages and displays visual summaries.  
- Uses `matplotlib` or `pandas` to generate charts.  
- Could later be connected to a GUI app for journaling.

---

## Author
**Hamdah Omotosho**  
Rutgers University — Fall 2025
