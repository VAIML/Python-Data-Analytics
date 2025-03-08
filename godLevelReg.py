import re
import isPhoneNumberValid
#import Comp_Animal_Lv2

#isPhoneNumberValid.isPhoneNumber('333-444-5555')
robocop = re.compile(r'robocop'. re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
nameRegex = re.compile('First Name: \w+')
so = nameRegex.search('First Name: Al Last Name: Sweigart ')
yo = nameRegex.search('First Name: Tom Dick Last Name: Harry')
print (yo.group())
#print (yo.group(1))
#print (yo.group(2))