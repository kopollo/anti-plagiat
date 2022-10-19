from algo import levenstein_distance


def test_strings_are_equal():
    a = "abca"
    b = "abca"
    assert levenstein_distance(a, b) == 0


def test_strings_are_diff():
    a = "abca"
    b = "vcdh"
    assert levenstein_distance(a, b) == len(a)


def test_add_or_delete_op():
    a = "abcaxxxxxx"
    b = "abca"
    assert levenstein_distance(a, b) == abs(len(a) - len(b))


def test_delete_op():
    a = "ghabcag"
    b = "abca"
    assert levenstein_distance(a, b) == 3


def test_delete_and_add_op():
    a = "habc"
    b = "abxxxc"
    assert levenstein_distance(a, b) == 4


def test_change_op():
    a = "abgcs"
    b = "abzcz"
    assert levenstein_distance(a, b) == 2


def test_multiply_op():
    a = "abcdeh"
    b = "xabjde"
    assert levenstein_distance(a, b) == 3


def test_list_given():
    a = [32, 6, 9, 3, 4]
    b = [32, 1, 4, 4]
    assert levenstein_distance(a, b) == 3


def test_long_str():
    lhs = "x" * 1000
    rhs = "x"
    assert levenstein_distance(lhs, rhs) == 999


def test_symmetric():
    lhs = "abcdexxxx"
    rhs = "bcdsr"
    assert levenstein_distance(lhs, rhs) == levenstein_distance(rhs, lhs)


def test_short_str():
    lhs = "x"
    rhs = "b"
    assert levenstein_distance(lhs, rhs) == 1


def test_empty_str():
    lhs = ""
    rhs = ""
    assert levenstein_distance(lhs, rhs) == 0
