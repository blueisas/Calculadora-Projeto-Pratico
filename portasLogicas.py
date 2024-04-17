def _not(a):
    if a == 1:
        return 0
    else:
        return 1


def _and(a, b):
    if a == 1 and b == 1:
        return True
    else:
        return False


def nand(a, b):
    if not _and(a, b) is True:
        return False
    else:
        return True


def _or(a, b):
    if a == 1 or b == 1:
        return True
    else:
        return False


def nor(a, b):
    if _or(a,b) is True:
        return False
    else:
        return True


def xor(a, b):
    if _and(a, b) is True or nand(a, b) is True:
        return False
    else:
        return True


def nxor(a, b):
    if xor(a, b) is True:
        return False
    else:
        return True

