def test_primative(n: int):
    n = 99


def test_object(obj):
    #obj['foo'] = 999
    obj = {'foo': 999}


x = 123
test_primative(x)
print(f"test_primative: x {x}")


o = {'foo': 123}
test_object(o)
print(f"test_object: o {o}")
