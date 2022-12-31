---

name: Conway's Game of Life in your Terminal
tools: [C++, ncurses]
image: images/tuigol_static.png
description: Basic implementation of Conway's Game of Life that runs in your terminal

---

# `tuigol`
## Terminal UI (tui) Game of Life (gol)
[View on GitHub](https://github.com/nmarks99/tuigol) for installation and usage instructions.

## Overview

What is Conway's Game of Life you ask? It is an example of a *cellular automaton*.
It as a 2D grid ("universe") where each cell either has a living or dead 
agent. These agents live or die based on three simple rules:

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

The interesting thing is that depending on initial conditions, some very interesting and 
complex behiavor can emerge just by following these three simple rules. Two examples are the
[glider gun](https://playgameoflife.com/lexicon/Gosper_glider_gun) or this 
cool [spaceship](https://playgameoflife.com/lexicon/119P4H1V0)

A more in-depth explanation can be found on [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).


## Demo

For now the result is pretty uninteresting since the only option is to start with a 
random initialization. Later on I plan to add a user friendly way to specify a 
starting condition as well as define some preset conditions.


{% include image.html path="../images/tuigol_demo.gif" caption="Demo" width="800" %}


