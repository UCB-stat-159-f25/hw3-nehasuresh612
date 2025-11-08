# incase I need to create an environment
.ONESHELL:
SHELL = /bin/bash

# create env phony target that updates the ligo environment I have
.PHONY: env
env :
	conda env update --name ligo --file environment.yml --prune

# create html phony target that builds local html rendering 
.PHONY: html
html :
	myst build --html

# create clean phony that cleans up figures, audio and _build folders
.PHONY: clean
clean :
	#rm -f _build/* audio/* figures/* --> not letting me delete directory for __build
	rm -rf _build/ audio/* figures/*