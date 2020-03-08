def test_bin():
    assert bin(4) == '0b100'


def test_literal():
    assert 0b100 == 4


def test_bin_to_int():
    assert int('100', 2) == 4
    assert int(bin(4), 2) == 4


def test_shift():
    assert 0b100 << 1 == 0b1000
    assert 0b100 >> 1 == 0b10


def test_xor_mask():
    assert 0b1001 ^ 0b1111 == 0b0110


def test_and_mask():
    assert 0b1010_0110 & 0b0000_1111 == 0b0000_0110


def test_or_mask():
    assert 0b1010_0110 | 0b1111_0000 == 0b1111_0110


def test_xor_calculation():
    # a ^ b ^ b == a
    assert 10 ^ 3 ^ 3 == 10


def test_counting_ones():
    # n & (n-1) removes the last 1.
    assert 0b11 & (0b11 - 1) == 0b10
    assert 0b10 & (0b10 - 1) == 0b00

    # counting ones
    n = 0b1101
    count = 0
    while n:
        n = n & (n - 1)
        count += 1

    assert count == 3


def test_not():
    assert ~0b0001 == -0b0010   # 1's complement of last two bits + minus sign
    assert ~0b0011 == -0b0100   # 1's complement of last three bits + minus sign

    # Two's complement
    assert ~0 == -1
    assert ~1 == -2


def test_bit_hex_decimal_byte():
    assert 0b1111_1111 == 255   # 8bit max
    assert 0b1111_1111 == 0xFF  # hex = 4 bits