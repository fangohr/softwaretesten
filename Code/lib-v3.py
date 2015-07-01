def f(n):
    """
    Funktion nimmt n (Integer) und gibt zurück:
      für n >= 0: die Summe von 0 bis n
      für n <  0: -1
    """
    if n >= 0:
        summe = 0
        for i in range(0, n + 1):  # Schleife von 0 bis n
            summe = summe + i
        return summe
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
