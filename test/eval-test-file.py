with open('../temp/test.py') as fh:
    data = {'foo': "Hello"}
    exec(fh.read(), data)
