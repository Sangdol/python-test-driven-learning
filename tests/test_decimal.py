from decimal import Decimal
import math


def test_comparison():
    assert Decimal("1.0") == Decimal("1.0")
    assert Decimal("1.0") == Decimal(1.0)

    # Be careful 1
    assert Decimal(1.1) == 1.1
    assert Decimal(1.1) != Decimal("1.1")
    assert Decimal(1.1) == Decimal(
        "1.100000000000000088817841970012523233890533447265625"
    )

    # Be careful 2
    assert Decimal(0.3) == 0.3
    assert Decimal(0.1 + 0.1 + 0.1) != 0.3
    assert Decimal(0.1 + 0.1 + 0.1) != Decimal(0.3)

    # Compare doesn't help
    # 1: bigger, -1: smaller, 0: equal
    assert Decimal(1.1).compare(Decimal("1.1")) == 1

    # Be careful 3
    assert Decimal("0.30") > 0.3

    # Rounding doesn't help
    assert round(Decimal("0.30"), 2) > 0.3

    # 0 always works
    assert Decimal("0.0") == 0
    assert Decimal("0.0") == Decimal(0)

    # Workaround
    assert math.isclose(Decimal("0.30"), 0.3)
