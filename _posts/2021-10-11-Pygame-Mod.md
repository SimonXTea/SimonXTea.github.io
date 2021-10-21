
# Pygame Slide Puzzle Mod

I had a simple college assignment to make a modified version of a Pygame called Slide Puzzle (by Al Sweigart). This Slide Puzzle Pygame mod was designed for Windows (Install with “pip install pypiwin32”, for any win32api issues use Google). Cross platform version doesn't require pypiwin32, and online and cross platform version will have less features. This should be compatible on Python version 3.7.9

How to play: The board is a 4x4 grid with fifteen tiles (numbered 1 through 15 going left to right) and one blank space. The tiles start out in random positions, and the player must slide tiles around until the tiles are back in their original order. 

Use wasd, arrow keys, or your mouse to control the tiles. Press M to pause the music. use + and - keys to control the volume. Press Reset to reset your game. Press Solve so the program finishes the game for you. Press New Game to start a new game. Press Escape key to exit out of the game.

[Download here for Windows](https://github.com/SimonXTea/SimonXTea.github.io/raw/main/projects/Pygame/Pygame%20Slide%20Puzzle%20Mod/Pygame%20mod.zip)

[Download here for cross-platform](https://github.com/SimonXTea/SimonXTea.github.io/raw/main/projects/Pygame/Pygame%20Slide%20Puzzle%20Mod/Pygame%20mod%20X.zip)

[Play online on Replit here](https://replit.com/@SimonXTea/Slide-Puzzle-Mod#main.py)

[Read source code here](https://github.com/SimonXTea/SimonXTea.github.io/tree/main/projects/Pygame/Pygame%20Slide%20Puzzle%20Mod)

[Original Pygame](https://inventwithpython.com/pygame/chapter4.html)

A preview can be seen below.

<iframe src="https://drive.google.com/file/d/1MJEldTm2xyzx0Oau5guS252dJk2PK_4L/preview" width="640" height="480" allow="autoplay"></iframe>

List of modifications
- A scoring system
- Redesign, night mode friendly
- Full screen **(Windows Exclusive)**
- Background music **(Missing online)**
- Mute music (Press M) **(Missing online)**
- Ability to change the volume **(Missing online)**
- Sound effects when moving tiles **(Missing online)**
- An easter egg / secret (Press w 10 times). This won’t affect your score. You can’t disable the secret once unlocked **(Missing online)**

You can also change the difficulty by changing BOARDWIDTH and BOARDHEIGHT in the code. This is a feature from the original pygame, not the mod.

I wanted to implement a lot more features in this game, like a creepy text adventure minigame (so, the easter egg would be this minigame instead of the music change), the machine moving tiles after you at random ocassions, among others, but unfortunately I didn't have enough time to develop these features, and it was not worth it since only my professor would see it.

I could had also made the fullscreen feature work on more operating systems and fix a few bugs (for example: The game can get stuck in the corner and the title bar can go missing)

![Pygame mod image](/assets/blog image/Pygame.png)
