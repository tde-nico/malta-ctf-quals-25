from z3 import *


enc = [
	0x39, 0xce, 0x69, 0x39, 0xa6, 0x61, 0x7c, 0xf4,
	0x0b, 0x3a, 0x21, 0x8d, 0x59, 0xf0, 0x15, 0x80,
	0x66, 0x41, 0x96, 0x75, 0xfb, 0x36, 0x67, 0x5c,
	0xa7, 0x95, 0x32, 0xee, 0xbc, 0xf7, 0xbf, 0xc2,
	0x95, 0x75, 0x60, 0x51, 0xb7, 0xaa, 0xa5, 0xd5,
	0x82, 0x37, 0xeb, 0x47, 0x7d, 0x8e, 0x60, 0xc8,
	0x9e, 0x6f, 0xa0, 0x88, 0x84, 0x0c, 0x3f, 0x9e,
	0x7c, 0x09, 0x17, 0x8c, 0x5f, 0x96, 0x0e, 0xd7,
]

consts = bytes.fromhex('423791A759DABEEF01020304691337AC')


def rol_bv(val, shift):
    return RotateLeft(val, shift)


def ror_bv(val, shift):
    return RotateRight(val, shift)


def bit_bv(val, bit_idx):
    return Extract(bit_idx, bit_idx, val)


def func_26(idx, block):
    tmp = [BitVec(f'tmp_{idx}_{i}', 8) for i in range(16)]

    for i in range(16):
        curr = block[i]
        nxt = block[(i + 1) % 16]

        rol_const = rol_bv(BitVecVal(consts[(i + idx) % 16], 8), i % 8)
        curr = curr ^ rol_const

        curr = ZeroExt(8, curr) + ZeroExt(8, nxt ^ BitVecVal(idx, 8))
        curr = ~curr & 0xFF
        curr = Extract(7, 0, curr)

        curr = ror_bv(curr, (i * 13) % 8)

        curr = If(bit_bv(nxt, 7) == 1, curr ^ BitVecVal(165, 8), curr)
        curr = If(bit_bv(nxt, 1) == 1, (curr + 60) & 0xFF, curr)
        curr = If(bit_bv(nxt, 2) == 1, (curr - 122) & 0xFF, curr)

        tmp[i] = curr

    out_block = [tmp[(16 + 5 * i - idx) % 16] for i in range(16)]
    return out_block


def entrypoint(block):
    for i in range(12):
        block = func_26(i, block)
    return block


for b in range(4):
    s = Solver()
    flag = [BitVec(f'flag_{b*16+i}', 8) for i in range(16)]

    if b != 3:
        for i in range(16):
            s.add(flag[i] >= 32, flag[i] <= 126)

    block = flag[:]
    encrypted = entrypoint(block)
    for i in range(16):
        s.add(encrypted[i] == enc[b*16+i])

    if s.check() == sat:
        m = s.model()
        output = [m[flag[i]].as_long() for i in range(16)]
        print("Flag:", bytes(output))
    else:
        print("No solution found")

# maltactf{i_really_hope_the_relocations_got_you_:P}
