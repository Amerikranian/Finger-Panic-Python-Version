# Finger-Panic-Python-Version
## An Example Game Using Lucia.
This is almost a direct conversion of a BGT game sharing the same name.
The game in question can be found [here](https://github.com/stas-prze/masonopensrc/tree/master/finger%20panic%202.0/src)
## Running Issues
Please read this section if the game fails to run. Right now, the only major error, pasted below, pertains to accessible_output2.
### Error text:
AttributeError: module 'win32com.gen_py.F152C4EF-B92F-4139-A901-E8F1E28CC8E0x0x1x0' has no attribute 'CLSIDToClassMap'
## Fixing Error Instructions
1. Open your run dialogue (windows r)
2. Type in 'appdata' without the quotation marks
3. Select 'local'
4. Select 'temp'
5. Delete the 'gen_py' folder.
That's it! You should be able to run the game now.
## Notes
Not all of the game is quite implemented. Some of it was left out on purpose. The goal is to provide a beginner with a decent project to get started with, as open-source Python materials are sorely lacking in the blind community. It is my hope that by providing this template, those transitioning from other languages will have an easier time learning Python
### No Executable
The game was meant more as a practice project. Should you choose to distribute this, I will not stop you, but as of right now you are on your own in regards to actual compilation process. If you aren't sure how to compile a python file into an executable, check out the section of my guide titled "Compiling code" found [here](https://forum.audiogames.net/topic/30141/python-guide-part-3-menus-timers-and-more/). If you still have questions about pyinstaller, chances are the official [Pyinstaller page](http://www.pyinstaller.org/) can help you.
## What Is Missing?
1. No cheatcodes. I considered the implementation and decided to leave it as an exercise.
2. Pausing the game. Again, left as an exercise, much simpler than cheats if I do say so myself.
## Can I Contribute?
Yes and no. While I will take contributions, I will not take versions which add any features mentioned as being exercises. This is meant as a beginner project. I appreciate improvements to the code, but I will not accept polls which add features the beginners are supposed to try and do themselves
## I'm stuck on what to add to the game
Check out the ideas file in the src directory for some inspiration
