'''
0x00: ra += rb
0x01: ra -= rb
0x02: ra *= rb
0x03: ra /= rb
0x04: ra %= rb
0x05: ra = rb
0x06: ra = b
0x07: R1 = ra, R2 = rb
0x08: if R1 == R2: jmp a
0x09: if R1 < R2: jmp a
0x0a: if R1 <= R2: jmp a
0x0b: if R1 > R2: jmp a
0x0c: if R1 >= R2: jmp a
0x0d: stack[ra] = rb
0x0e: ra = stack[rb]
0x0f: IO (r0 == 2: exit, r0 == 1: getc, r0 == 0: putc)
0x10: call a
0x11: ret (if empty stack: exit)
0x12: ra &= rb
0x13: ra ^= rb
0x14: ra ~= rb
0x15: jmp a
0x16: printf("[PR] %x\n", ra)
0x17: ra = ror lowbyte(ra)
0x18: ra = rol lowbyte(ra)
0x19: ra >>= rb
0x1a: ra = lowbyte(ra << rb)
default: nop
'''

p = print

code = "0602000000000000000603000000010000000604000000020000000702000000010000000C4800000000000000030000000004000000000200000003000000151B0000000000000012000000000300000011000000000000000006020000000C0000000603000000300000000D03000000020000000600000000000000000603000000310000000D030000000000000010EA000000000000000603000000310000000E00000000030000000604000000010000000000000000040000000604000000300000000E0300000004000000070000000003000000097E000000000000001100000000000000000601000000000000000603000000000000000003000000010000000E04000000030000000602000000010000000003000000020000000602000000100000000403000000020000000E05000000030000000503000000010000000003000000000000000602000000100000000403000000020000000003000000020000000E060000000300000005070000000100000006020000000800000004070000000200000005080000000600000018080000000700000013040000000800000005070000000500000013070000000000000000040000000700000006020000000001000004040000000200000014040000000000000005070000000100000006020000000D0000000207000000020000000602000000080000000407000000020000001704000000070000000607000000320000000D07000000000000000607000000330000000D07000000010000000607000000340000000D07000000020000000607000000350000000D07000000030000000607000000360000000D07000000040000000607000000370000000D07000000050000000607000000380000000D07000000060000000500000000050000000601000000070000001000000000000000000601000000000000000700000000010000000607000000320000000E00000000070000000607000000330000000E01000000070000000607000000340000000E02000000070000000607000000350000000E03000000070000000607000000360000000E04000000070000000607000000370000000E05000000070000000607000000380000000E06000000070000000857030000000000000602000000A50000001304000000020000000607000000320000000D07000000000000000607000000330000000D07000000010000000607000000340000000D07000000020000000607000000350000000D07000000030000000607000000360000000D07000000040000000607000000370000000D07000000050000000607000000380000000D07000000060000000500000000050000000601000000010000001000000000000000000601000000000000000700000000010000000607000000320000000E00000000070000000607000000330000000E01000000070000000607000000340000000E02000000070000000607000000350000000E03000000070000000607000000360000000E04000000070000000607000000370000000E05000000070000000607000000380000000E060000000700000008AD0400000000000006020000003C0000000004000000020000000602000000000100000404000000020000000607000000320000000D07000000000000000607000000330000000D07000000010000000607000000340000000D07000000020000000607000000350000000D07000000030000000607000000360000000D07000000040000000607000000370000000D07000000050000000607000000380000000D07000000060000000500000000050000000601000000020000001000000000000000000601000000000000000700000000010000000607000000320000000E00000000070000000607000000330000000E01000000070000000607000000340000000E02000000070000000607000000350000000E03000000070000000607000000360000000E04000000070000000607000000370000000E05000000070000000607000000380000000E060000000700000008030600000000000006020000007A0000000104000000020000000602000000FF0000001204000000020000000603000000200000000003000000010000000D030000000400000006020000000100000000010000000200000006020000001000000007010000000200000009F3000000000000000601000000000000000603000000100000000602000000050000000202000000010000000003000000020000000103000000000000000602000000100000000403000000020000000602000000200000000003000000020000000E07000000030000000D0100000007000000060200000001000000000100000002000000060200000010000000070100000002000000095406000000000000110000000000000000"
code = bytes.fromhex(code)
code = [code[i:i+9] for i in range(0, len(code), 9)]


DEBUG = 1
ANONYMOUS = 0
EXEC = 0

regs = [0] * 256
# stack = [0] * 512
stack = '00000000000000000000000000000000423791A759DABEEF01020304691337AC000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
stack = bytearray.fromhex(stack)
stack = stack[:256]
R1 = 0
R2 = 0

i = 10
if not EXEC:
	i = 0

while i < len(code):
	op = code[i][0]
	a = int.from_bytes(code[i][1:5], 'little')
	b = int.from_bytes(code[i][5:9], 'little')
	print = lambda *args, **kwargs: p(end=f' # {i}\n', *args, **kwargs)
	
	match op:
		case 0x00:
			if DEBUG: print(f'r{a} += r{b}')
			if ANONYMOUS: print(f'ra += rb'); i += 1; continue
			if not EXEC: i += 1; continue
			regs[a] += regs[b]
		case 0x01:
			if DEBUG: print(f'r{a} -= r{b}')
			if ANONYMOUS: print(f'ra -= rb'); i += 1; continue
			if not EXEC: i += 1; continue
			regs[a] -= regs[b]
		case 0x02:
			if DEBUG: print(f'r{a} *= r{b}')
			if ANONYMOUS: print(f'ra *= rb'); i += 1; continue
			if not EXEC: i += 1; continue
			regs[a] *= regs[b]
		case 0x03:
			if DEBUG: print(f'r{a} /= r{b}')
			if ANONYMOUS: print(f'ra /= rb'); i += 1; continue
			if not EXEC: i += 1; continue
			regs[a] //= regs[b]
		case 0x04:
			if DEBUG: print(f'r{a} %= r{b}')
			if ANONYMOUS: print(f'ra %= rb'); i += 1; continue
			if not EXEC: i += 1; continue
			regs[a] %= regs[b]
		case 0x05:
			if DEBUG: print(f'r{a} = r{b}')
			if ANONYMOUS: print(f'ra = rb'); i += 1; continue
			if not EXEC: i += 1; continue
			regs[a] = regs[b]
		case 0x06:
			if DEBUG: print(f'r{a} = {b}')
			if ANONYMOUS: print(f'ra = b'); i += 1; continue
			if not EXEC: i += 1; continue
			regs[a] = b
		case 0x07:
			if DEBUG: print(f'R1 = r{a}, R2 = r{b}')
			if ANONYMOUS: print(f'R1 = ra, R2 = rb'); i += 1; continue
			if not EXEC: i += 1; continue
			R1 = regs[a]
			R2 = regs[b]
		case 0x08:
			assert a % 9 == 0
			if DEBUG: print(f'if R1 == R2: jmp {a//9}')
			if ANONYMOUS: print(f'if R1 == R2: jmp {a//9}'); i += 1; continue
			if not EXEC: i += 1; continue
			if R1 == R2:
				i = a//9 - 1
		case 0x09:
			assert a % 9 == 0
			if DEBUG: print(f'if R1 < R2: jmp {a//9}')
			if ANONYMOUS: print(f'if R1 < R2: jmp a'); i += 1; continue
			if not EXEC: i += 1; continue
			if R1 < R2:
				i = a//9 - 1
		case 0x0a:
			assert a % 9 == 0
			if DEBUG: print(f'if R1 <= R2: jmp {a//9}')
			if ANONYMOUS: print(f'if R1 <= R2: jmp a'); i += 1; continue
			if not EXEC: i += 1; continue
			if R1 <= R2:
				i = a//9 - 1
		case 0x0b:
			assert a % 9 == 0
			if DEBUG: print(f'if R1 > R2: jmp {a//9}')
			if ANONYMOUS: print(f'if R1 > R2: jmp a'); i += 1; continue
			if not EXEC: i += 1; continue
			if R1 > R2:
				i = a//9 - 1
		case 0x0c:
			assert a % 9 == 0
			if DEBUG: print(f'if R1 >= R2: jmp {a//9}')
			if ANONYMOUS: print(f'if R1 >= R2: jmp a'); i += 1; continue
			if not EXEC: i += 1; continue
			if R1 >= R2:
				i = a//9 - 1
		case 0x0d:
			if DEBUG: print(f'stack[r{a}] = r{b}')
			if ANONYMOUS: print(f'stack[ra] = rb'); i += 1; continue
			if not EXEC: i += 1; continue
			stack[regs[a]] = regs[b] & 0xff
		case 0x0e:
			if DEBUG: print(f'r{a} = stack[r{b}]')
			if ANONYMOUS: print(f'ra = stack[rb]'); i += 1; continue
			if not EXEC: i += 1; continue
			regs[a] = stack[regs[b]]
		case 0x0f:
			if DEBUG: print(f'syscall # (r0 == 2: exit, r0 == 1: getc, r0 == 0: putc)')
			if ANONYMOUS: print(f'syscall # (r0 == 2: exit, r0 == 1: getc, r0 == 0: putc)'); i += 1; continue
			if not EXEC: i += 1; continue
			if a == 2: # exit
				print("Exiting VM")
				exit(0)
			elif a == 1: # getc
				char = input("Enter a character: ")
				if char:
					regs[b] = ord(char[0])
					if DEBUG: print(f'getc: {b} = {regs[b]}')
				else:
					print("No input received")
			elif a == 0: # putc
				print(chr(regs[b]), end='', flush=True)
				if DEBUG: print(f'putc: {b} = {regs[b]}')
			else:
				print(f"Unknown IO operation {a}")
		case 0x10:
			assert a % 9 == 0
			if DEBUG: print(f'call {a//9}')
			if ANONYMOUS: print(f'call a'); i += 1; continue
			if not EXEC: i += 1; continue
			stack.append(i & 0xff)
			i = a//9 - 1
		case 0x11:
			if DEBUG: print(f'ret')
			if ANONYMOUS: print(f'ret'); i += 1; continue
			if not EXEC: i += 1; continue
			i = stack.pop()
		case 0x12:
			if DEBUG: print(f'r{a} &= r{b}')
			if ANONYMOUS: print(f'ra &= rb'); i += 1; continue
			if not EXEC: i += 1; continue
			regs[a] &= regs[b]
		case 0x13:
			if DEBUG: print(f'r{a} ^= r{b}')
			if ANONYMOUS: print(f'ra ^= rb'); i += 1; continue
			if not EXEC: i += 1; continue
			regs[a] ^= regs[b]
		case 0x14:
			if DEBUG: print(f'r{a} = ~r{a}')
			if ANONYMOUS: print(f'ra = ~ra'); i += 1; continue
			if not EXEC: i += 1; continue
			regs[a] = ~regs[a]
		case 0x15:
			assert a % 9 == 0
			if DEBUG: print(f'jmp {a//9}')
			if ANONYMOUS: print(f'jmp a'); i += 1; continue
			if not EXEC: i += 1; continue
			i = a//9 - 1
		case 0x16:
			if DEBUG: print(f'printf("[PR] %x\n", ra): {a} -> {regs[a]}')
			if ANONYMOUS: print(f'printf("[PR] %x\n", ra)'); i += 1; continue
			if not EXEC: i += 1; continue
			print(f"[PR] 0x{regs[a]:x}")
		case 0x17:
			if DEBUG: print(f'r{a} = ror r{a} r{b}')
			if ANONYMOUS: print(f'ra = ror ra rb'); i += 1; continue
			if not EXEC: i += 1; continue
			regs[a] = ((regs[a] & 0xff) >> regs[b]) | ((regs[a] & 0xff) << (8 - regs[b]))
		case 0x18:
			if DEBUG: print(f'r{a} = rol r{a} r{b}')
			if ANONYMOUS: print(f'ra = rol ra rb'); i += 1; continue
			if not EXEC: i += 1; continue
			regs[a] = ((regs[a] & 0xff) << regs[b]) | ((regs[a] & 0xff) >> (8 - regs[b]))
		case 0x19:
			if DEBUG: print(f'r{a} >>= r{b}')
			if ANONYMOUS: print(f'ra >>= rb'); i += 1; continue
			if not EXEC: i += 1; continue
			regs[a] >>= regs[b]
		case 0x1a:
			if DEBUG: print(f'r{a} = lowbyte(r{a} << r{b})')
			if ANONYMOUS: print(f'ra = lowbyte(ra << rb)'); i += 1; continue
			if not EXEC: i += 1; continue
			regs[a] = (regs[a] << regs[b]) & 0xff
		
		case _:
			print(f'Not implemented: {op:02x} {a} {b}')

	i += 1


