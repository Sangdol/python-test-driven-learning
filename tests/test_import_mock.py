import sys

from unittest.mock import Mock
from unittest.mock import patch

import stub.package_test_math as test_math


@patch('stub.package_test_math.package_test_subtract')
def test_mocked_subtract(mocked_subtract):
    mocked_subtract.subtract.return_value = 5
    assert test_math.subtract(2, 3) == 5

