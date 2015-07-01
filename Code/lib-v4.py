def f(n):
    """
    Funktion nimmt n (Integer) und gibt zurück:
      für n >= 0: die Summe von 0 bis n
      für n <  0: -1
    """
    if n >= 0:
        return n * (n + 1) // 2
    else:
        return -1

def test_f_positive():
    assert f(3) == 0 + 1 + 2 + 3
    assert f(10) == 55

def test_f_negative():
    assert f(-20) == -1
    assert f(-10) == -1

def test_f_grenzfall():
    assert f(0) == 0
    assert f(-1) == -1
