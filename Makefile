MODULE := booking_gauger_tpoter

run:
	@python -m $(MODULE)

test:
	@pytest

.PHONY:
	 clean test

clean:
	 rm -rf .pytest.pycache .coverage coverage.xml


