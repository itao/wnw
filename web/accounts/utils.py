import base64

def decode_b64(b64string):
	# Re-encode to ascii
	b64string = b64string.encode('ascii')
	padded = b64string + '=' * (4 - len(b64string) % 4)
	return base64.b64decode(padded)