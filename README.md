# 🏝️ Treasure Island

> A text-based adventure game in Python where every choice you type decides whether you find the treasure or meet a bad end.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-completed-brightgreen?style=for-the-badge)
![Project](https://img.shields.io/badge/project-personal-blueviolet?style=for-the-badge)

---

## 📌 About the Project

**Treasure Island** is an interactive console game written in Python. The player starts at a crossroads and makes a series of choices (which path to take, whether to wait or swim, which door to open). Each choice leads either to a new scene or to an ending. Only one sequence of choices reaches the treasure.

This is a **personal project developed independently** as part of my programming portfolio. It was built to practise conditional logic: how a program reads input, compares it against expected values and branches into different outcomes.

---

## 🎯 Learning Objectives

- **Conditional statements**: using `if`, `elif` and `else` to choose what happens next.
- **Nested conditionals**: placing decisions inside other decisions to build a multi-step story.
- **User input handling**: reading choices from the terminal with `input()`.
- **String normalisation**: using `.lower()` so the game accepts `LEFT`, `Left` and `left` alike.
- **Terminal styling**: colouring text with ANSI escape codes.
- **Raw strings and ASCII art**: using `r'''...'''` so backslashes in the artwork are printed literally.

---

## ⚙️ How It Works

```
                         Crossroads
                        /          \
                   "right"        "left"
                      |              |
                  Game Over       The lake
                  (pitfall)      /        \
                            "swim"       "wait"
                              |             |
                          Game Over     Three doors
                           (trout)    /     |      \
                                   red    blue    yellow
                                    |       |        |
                               Game Over Game Over  YOU WIN
                                (fire)   (beasts)   (treasure)
```

### Code Walkthrough

```python
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print('You are at a cross road. Where do you want to go?')

left_or_right=str(input('Type \"left" or  "right" :')).lower()
if left_or_right == 'right':
    print('You take the path on the right. Unaware of the pitfall, you step on loose soil and fall into a hole. Game Over.')
else:
    print('You follow the left path until you reach the edge of a dark, wide lake.')
    wait_swim=str(input('Type \"wait" or "swim" :  ')).lower()
    if wait_swim == 'swim':
        print('Impatient, you dive into the water to swim across. Suddenly, a giant trout emerges from the deep. Attacked by trout. Game Over.')
    else:
        print('You choose to wait patiently at the shore until a safe passage appears. On the other side, you find an ancient structure with three colored doors.')
        door=str(input('Type ' + '\33[1;31mred door\33[m ' + 'or ' + '\33[1;34mblue door\33[m ' + 'or ' + '\33[1;33myellow door\33[m : ')).lower()
        if door == 'red door':
            print('You open the red door and an inferno engulfs the room. Burned by fire. Game Over.')
        elif door == 'blue door':
            print('You open the blue door into a dark chamber full of hungry creatures. Eaten by beasts. Game Over.')
        elif door == 'yellow door':
            print('You open the yellow door. The room opens up to reveal the chest full of legendary gold. You Win!')
        else:
             print('Action invalid. Game Over.')
```

| Line / Section | Responsibility |
|---|---|
| `print(r'''...''')` | Displays the ASCII treasure map as a raw string |
| `print("Welcome...")` and the next two prints | Introduce the game and the mission |
| `left_or_right = ...input(...).lower()` | Reads the first choice and normalises it to lowercase |
| `if left_or_right == 'right'` | Ending 1: the player falls into a hole |
| `else` + `wait_swim = ...` | The left path leads to the lake and asks for a second choice |
| `if wait_swim == 'swim'` | Ending 2: the player is attacked by a giant trout |
| `else` + `door = ...` | Waiting leads to the three coloured doors and a third choice |
| `if / elif door == ...` | Red and blue doors lead to losing endings; the yellow door wins the game |
| final `else` | Handles an invalid door choice with "Action invalid. Game Over." |

**Technical notes.** The door prompt is coloured with ANSI escape codes: `\33[1;31m` switches the text to bold red, `\33[1;34m` to bold blue, `\33[1;33m` to bold yellow, and `\33[m` resets the style. The treasure map is printed from a raw string (`r'''...'''`), which keeps backslashes as plain characters instead of treating them as escape sequences.

One behaviour worth knowing: the first two questions use `else` for the "safe" branch. That means any answer other than `right` at the crossroads is treated as `left`, and any answer other than `swim` at the lake is treated as `wait`. Only the final question, with its `elif` chain, reports an invalid choice.

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/) installed
- A terminal that supports ANSI colours (most modern terminals do)
- No external libraries required

### Installation and Execution

```bash
git clone https://github.com/guiggsp-hub/Treasure-Island.git
cd Treasure-Island
python main.py
```

### Sample Run

```
(ASCII treasure map is displayed here)
Welcome to Treasure Island.
Your mission is to find the treasure.
You are at a cross road. Where do you want to go?
Type "left" or  "right" :left
You follow the left path until you reach the edge of a dark, wide lake.
Type "wait" or "swim" :  wait
You choose to wait patiently at the shore until a safe passage appears. On the other side, you find an ancient structure with three colored doors.
Type red door or blue door or yellow door : yellow door
You open the yellow door. The room opens up to reveal the chest full of legendary gold. You Win!
```

---

## 🧠 Skills Demonstrated

`Python` · `Conditional Logic` · `Nested if/elif/else` · `User Input` · `String Methods` · `Raw Strings` · `ANSI Escape Codes` · `CLI Applications`

---

## 👤 Author

Developed independently by **Guilherme Garcia** as part of a personal programming portfolio.

[![GitHub](https://img.shields.io/badge/GitHub-guiggsp--hub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/guiggsp-hub)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Guilherme%20Garcia-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guilherme-garcia-796633287/)
