test:
	pipenv run pytest

test-watch:
	pipenv run ptw -- --disable-warnings --testmon
