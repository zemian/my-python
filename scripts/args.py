# python /Users/zemian/my-py/learn-python/args.py one two three
# Argument /Users/zemian/my-py/learn-python/args.py
# Argument one
# Argument two
# Argument three
import sys

for arg in sys.argv:
    print("Argument %s" % arg)
