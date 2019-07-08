default: run

install:
	pip install --user simplejson pyglet

.PHONY: run
run:

.PHONY: start-server
start-server:


.PHONY: format
format:
	autopep8 --in-place --aggressive --aggressive *.py