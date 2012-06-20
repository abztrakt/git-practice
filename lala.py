""" A badly formatted python script for testing a pre-commit hook. """

# This is a really long comment so that PEP8 gets upset about it. It thinks lines should only be 80 chars or less.


def main():
    name = "Craig"
    string="Hi %s" % name
    import random
    randnum = random.randrange(1, 99)
    return string

if __name__=="__main__":
    print main()
