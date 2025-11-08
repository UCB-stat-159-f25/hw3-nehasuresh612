[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/hw3-nehasuresh612/HEAD)

# Homework 3
### (Acknowledgement below from HW 2)
_This repository is public so that Binder can find it. All code and data is based on the original [LIGO Center for Open Science Tutorial Repository](https://github.com/losc-tutorial/LOSC_Event_tutorial). This repository is a class exercise that restructures the original LIGO code for improved reproducibility, as a homework assignment for the [Fall 2025 installment of UC Berkeley's Stat 159/259 course, _Reproducible and Collaborative Data Science](https://ucb-stat-159-f25.github.io/site/). Authorship of the original analysis code rests with the LIGO collaboration._

## Basic Description of Project
In this project, I’ll be continuing from HW 2 and working with the code from the Ligo Gravitational Wave Detection Tutorial. I’ve created an installable package for `ligotools` by adding a pyproject.toml file. I also added tests for some of the functions in `readligo.py`, which I created in the previous homework. 

Moreover, I created `utils.py` to add utility functions from the LOSC_Event_tutorial.ipynb notebook as well as tests for these utility functions. Note that my tests run with the GitHub command `python -m pytest ligotools` rather than `pytest ligotools`.

Next, I added binder support, which can be accessed via the link above. I also used MyST for local building and deployed the site in GitHub pages. Finally, I created a Makefile to run targets to updatr the conda environment, build a local html render of the MySt site, and clean excess files.


[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wOo27OxG)
