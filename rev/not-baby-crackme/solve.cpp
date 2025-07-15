#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

uint8_t consts[16] = {
	0x42, 0x37, 0x91, 0xA7,
	0x59, 0xDA, 0xBE, 0xEF,
	0x01, 0x02, 0x03, 0x04,
	0x69, 0x13, 0x37, 0xAC,
};

uint8_t rotl(uint8_t x, int n) {
    return (uint8_t)((x << n) | (x >> (8 - n)));
}

uint8_t rotr(uint8_t x, int n) {
    return (uint8_t)((x >> n) | (x << (8 - n)));
}

void do_round(uint8_t* mem, uint8_t rind) {
	uint8_t temp[16];
	for (int i = 0; i < 16; i++) {
		uint8_t x = mem[i];
		uint8_t y = mem[(i + 1) % 16];
		uint8_t rk = consts[(rind + i) % 16];

		x ^= rotl(rk, i % 8);
		x += y ^ rind;
		x = ~x;
		x = rotr(x, i * 5 % 8);

		if (y & 128) {
			x ^= 165;
		}

		if (y & 2) {
			x += 60;
		}

		if (y & 4) {
			x -= 122;
		}

		temp[i] = x;
	}

	for (int i = 0; i < 16; i++) {
		mem[i] = temp[(5 * i - rind) & 15];
	}
}

void encrypt(uint8_t* mem) {
	for (uint8_t i = 0; i < 12; i++) {
		do_round(mem, i);
	}
}

void undo_round(vector<vector<uint8_t>>& mems, uint8_t rind) {
	vector<vector<uint8_t>> out_mems;
	for (const auto& input : mems) {
		uint8_t temp[16];
		for (int i = 0; i < 16; i++) {
			temp[(5 * i - rind) & 15] = input[i];
		}

		int valid2 = 0;
		for (int s = 0; s < 256; s++) {
			uint8_t mem[17];
			mem[16] = (uint8_t)s;
			for (int i = 15; i >= 0; i--) {
				vi valid;
				for (int t = 0; t < 256; t++) {
					uint8_t x = (uint8_t)t;
					uint8_t y = mem[i + 1];
					uint8_t rk = consts[(rind + i) % 16];

					x ^= rotl(rk, i % 8);
					x += y ^ rind;
					x = ~x;
					x = rotr(x, i * 5 % 8);

					if (y & 128) {
						x ^= 165;
					}

					if (y & 2) {
						x += 60;
					}

					if (y & 4) {
						x -= 122;
					}

					if (temp[i] == x) valid.push_back(t);
				}
				assert(valid.size() == 1);
				mem[i] = (uint8_t)valid[0];
			}
			if (mem[0] == s) {
				valid2++;
				out_mems.push_back(vector<uint8_t>(mem, mem + 16));
			}
		}
	}
	mems = out_mems;
}

void decrypt(uint8_t* mem) {
	vector<vector<uint8_t>> mems;
	mems.push_back(vector<uint8_t>(mem, mem + 16));
	for (int i = 11; i >= 0; i--) {
		undo_round(mems, (uint8_t)i);
	}
	for (const auto& m : mems) {
		for (int i = 0; i < 16; i++) if (m[i] >= 128) goto skip;
		cout << string(m.data(), m.data() + 16);
skip:;
	}
}

int main() {
	uint8_t target[64] = {
		0x39, 0xce, 0x69, 0x39, 0xa6, 0x61, 0x7c, 0xf4,
		0x0b, 0x3a, 0x21, 0x8d, 0x59, 0xf0, 0x15, 0x80,
		0x66, 0x41, 0x96, 0x75, 0xfb, 0x36, 0x67, 0x5c,
		0xa7, 0x95, 0x32, 0xee, 0xbc, 0xf7, 0xbf, 0xc2,
		0x95, 0x75, 0x60, 0x51, 0xb7, 0xaa, 0xa5, 0xd5,
		0x82, 0x37, 0xeb, 0x47, 0x7d, 0x8e, 0x60, 0xc8,
		0x9e, 0x6f, 0xa0, 0x88, 0x84, 0x0c, 0x3f, 0x9e,
		0x7c, 0x09, 0x17, 0x8c, 0x5f, 0x96, 0x0e, 0xd7,
	};

	for (int i = 0; i < 4; i++) {
		decrypt(target + 16*i);
	}
	cout << endl;
}
