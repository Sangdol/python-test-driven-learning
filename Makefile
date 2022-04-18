test:
	poetry run pytest tests/*.py

# If testmon doesn't work, try deleting the .testmondata directory.
test-watch:
	poetry run ptw tests/*.py -- --disable-warnings --testmon -v -s
