default: run

install:
	pip install --user simplejson pyglet

.PHONY: run
run:
	python src/server.py & python src/client.py & python src/client.py

.PHONY: kill
kill:
	pkill python

.PHONY: start-server
start-server:
	python src/server.py

.PHONY: start-client
start-client:
	python src/client.py

.PHONY: format
format:
	autopep8 --in-place --aggressive --aggressive src/*.py