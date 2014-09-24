import unittest

'''
validate password
6-8 char
1 num
1 upper
1 lower

validate email
thing @ thing . thing

validate phone
### ### ####
##########
###-###-####
'''

##############
## Password ##
##############


class PassTest(unittest.TestCase):
    def validatePass(self, str):
        if passLenCheck(str) and upperCheck(str) and lowerCheck(str) and numCheck(str):
            return None
        return False
    
    def passLenCheck(self, str):
        if (len(str) > 5 and len(str) < 9):
            return True
        return False
    
    def upperCheck(self, str):
        for i in range(0, len(str)):
            if str[i].isupper():
                return True
        return False

    def lowerCheck(self, str):
        for i in range(0, len(str)):
            if str[i].islower():
                return True
        return False
    def numCheck(self, str):
        for i in range(0, len(str)):
            if str[i].isdigit():
                return True
        return False

############
## E-Mail ##
############

class emailTest(unittest.TestCase):
    def validateEmail(self, str):
        pass

    def Test(self, str):
        beginning = False
        at = False
        middle = False
        dot = False
        end = False
        '''
        if str[0] == "@":
            return False
        for i in range(0, len(str)):
            if str[i] == ".":
                return False
            if str[i] == "@":
                if str[i+1].isalpha():
                    return True
        return False
        '''
class UtilsTest(unittest.TestCase):
    #TEST THIGN EHRE PLS THAKN

if __name__ == "__main__":
    #basically unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(UtilsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
