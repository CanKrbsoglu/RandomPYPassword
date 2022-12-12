import string
import random

def random_password_generator():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.printable
    size = 15
    return ''.join(random.choice(chars) for x in range(size, 25))

def random_password_generator_ico():
	random_password_generator_ico = """
	#############################################################
	                 T E R A P İ-PYTHON
	#############################################################                                 
	#############################################################
              ismailcan karabaşoğlu Password Generator
	#############################################################
	"""
	print(random_password_generator_ico)
