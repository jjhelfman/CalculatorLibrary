"""
Calculator library containing basic math operations.
"""
# TDD = writing failing tests before getting them to pass
# The test_ at the start of this file name lets pytest know this is a test
# Run the following -->
# The . is to test only the test_ file (not the venv folder!):
# pytest -v --cov . (remember,   -v, --verbose         increase verbosity.)

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtract(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)
