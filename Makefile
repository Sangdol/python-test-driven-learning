type-test:
	mypy test_type.py --check-untyped-defs

test:
	poetry run pytest

# Todo
#test-watch:
	#poetry run ptw -- --disable-warnings --testmon
