#
# See also the "tool.pytest.ini_options" section of pyproject.toml
#

test:
	poetry run pytest tests/*.py

# If testmon doesn't work, try deleting the .testmondata directory.
test-watch:
	poetry run ptw tests/*.py -- --testmon

doctest-watch:
	poetry run ptw tests/*.py -- --testmon --doctest-modules
