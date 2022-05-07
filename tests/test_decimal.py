from decimal import Decimal
import math


def test_comparison():
    assert Decimal('1.0') == Decimal('1.0')

    # Be careful 1. don't pass a float to Decimal
    assert Decimal(1.1) == 1.1  # the 1.1 arugment is already flaot
    assert Decimal(1.1) != Decimal('1.1')  # so this is not equal
    assert Decimal(1.1) == Decimal(
        '1.100000000000000088817841970012523233890533447265625'
    )
    assert Decimal(0.3) == 0.3
    assert Decimal(0.1 + 0.1 + 0.1) != 0.3
    assert Decimal(0.1 + 0.1 + 0.1) != Decimal(0.3)

    # This sometimes works which makes things more confusing
    assert Decimal('1.0') == Decimal(1.0)

    # Be careful 2. don't compare a float to Decimal
    assert Decimal('0.30') > 0.3

    # Rounding doesn't help
    assert Decimal('0.30') > round(0.3, 2)

    # Rounding helps in some cases
    assert Decimal(0.3) - Decimal('0.3') != 0
    assert round(Decimal(0.3) - Decimal('0.3'), 2) == 0

    # 0 always works
    assert Decimal('0.0') == 0
    assert Decimal('0.0') == Decimal(0)

    # Workaround / right way
    assert math.isclose(Decimal('0.30'), 0.3)
    assert Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3')
