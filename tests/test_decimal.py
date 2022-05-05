from decimal import Decimal


def test_comparison():
    assert Decimal("1.0") == Decimal("1.0")
    assert Decimal("1.0") == Decimal(1.0)

    # Be careful
    assert Decimal("1.1") != Decimal(1.1)
    assert Decimal(1.1) == Decimal(
        "1.100000000000000088817841970012523233890533447265625"
    )
