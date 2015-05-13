from random import choice
from string import ascii_lowercase, ascii_uppercase, digits
def base64(length):
	return ''.join(choice(ascii_lowercase + ascii_uppercase + digits) for _ in range(length))
