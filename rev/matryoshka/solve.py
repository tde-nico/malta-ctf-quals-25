keys = [
	0x89044212,
	0xB57D677C,
	0x36A311AD,
	0x13F906B8,
	0xE753018A,
	0xA2B08FE2,
	0x9F146446,
	0x080474D5,
	0xFC19CAA4,
	0xD6472EE8,
	0x9FACC793,
	0xAB0B7CD5,
	0x8ECB4682,
	0x5EEB93BD
]

flag = bytearray()

for f in range(len(keys)-1, -1, -1):
	for i in range(32, 128):
		for j in range(32, 128):

			password = bytes([i, j]) + flag
			k = 0x811c9dc5
			for b in password:
				k = ((k^b) * 0x1000193) & 0xffffffff

			if k == keys[f]:
				flag = bytes([i, j]) + flag
				print(f"Found: {flag}")
				break

		else:
			continue
		break
	else:
		print("No match found for key:", hex(keys[f]))
		exit(1)

print("Final flag:", f'maltactf{{{flag.decode()}}}')

# maltactf{5Ecrets_WiThIn_Rus$14N_DOL1s}
