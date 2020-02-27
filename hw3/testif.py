def testif(b, testname, msgOK="", msgFailed=""):
    if b:
        print("Success: " + testname + "; " + msgOK)
    else:
        print("Failed: " + testname + "; " + msgFailed)
    return b
