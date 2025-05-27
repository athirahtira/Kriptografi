class DES:
    def __init__(self):
        # Initial Permutation Table
        self.IP = [
            58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7
        ]
        
        # Final Permutation Table (IP^-1)
        self.FP = [
            40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25
        ]
        
        # Permutation Choice 1 for key generation
        self.PC1 = [
            57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4
        ]
        
        # Permutation Choice 2 for key generation
        self.PC2 = [
            14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32
        ]
        
        # Expansion table for F function
        self.E = [
            32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1
        ]
        
        # S-boxes
        self.SBOX = [
            # S1
            [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
             [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
             [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
             [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
            
            # S2
            [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
             [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
             [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
             [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
            
            # S3
            [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
             [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
             [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
             [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
            
            # S4
            [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
             [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
             [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
             [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
            
            # S5
            [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
             [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
             [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
             [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
            
            # S6
            [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
             [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
             [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
             [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
            
            # S7
            [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
             [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
             [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
             [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
            
            # S8
            [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
             [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
             [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
             [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
        ]
        
        # P permutation for F function
        self.P = [
            16, 7, 20, 21,
            29, 12, 28, 17,
            1, 15, 23, 26,
            5, 18, 31, 10,
            2, 8, 24, 14,
            32, 27, 3, 9,
            19, 13, 30, 6,
            22, 11, 4, 25
        ]
        
        # Left shifts for key generation
        self.SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    def permute(self, data, table):
        """Apply permutation based on given table"""
        return [data[i-1] for i in table]

    def xor(self, a, b):
        """XOR two bit arrays"""
        return [x ^ y for x, y in zip(a, b)]

    def left_shift(self, data, shifts):
        """Left circular shift"""
        return data[shifts:] + data[:shifts]

    def string_to_bits(self, text):
        """Convert string to bit array"""
        bits = []
        for char in text:
            byte = ord(char)
            for i in range(7, -1, -1):
                bits.append((byte >> i) & 1)
        return bits

    def bits_to_string(self, bits):
        """Convert bit array to string"""
        chars = []
        for i in range(0, len(bits), 8):
            byte = 0
            for j in range(8):
                if i + j < len(bits):
                    byte = (byte << 1) | bits[i + j]
            chars.append(chr(byte))
        return ''.join(chars)

    def pad_data(self, data):
        """Pad data to multiple of 64 bits"""
        while len(data) % 64 != 0:
            data.append(0)
        return data

    def group_bits(self, bits, group_size=4):
        """Group bits for better readability"""
        bit_str = ''.join(map(str, bits))
        return ' '.join(bit_str[i:i+group_size] for i in range(0, len(bit_str), group_size))

    def generate_keys(self, key, verbose=False):
        """Generate 16 subkeys from main key"""
        # Convert key to bits
        key_bits = self.string_to_bits(key.ljust(8)[:8])
        
        if verbose:
            print(f"Original key       : {self.group_bits(key_bits)}")
        
        # Apply PC1 permutation
        pc1_key = self.permute(key_bits, self.PC1)
        
        if verbose:
            print(f"After PC1          : {self.group_bits(pc1_key)}")
        
        # Split into left and right halves
        left = pc1_key[:28]
        right = pc1_key[28:]
        
        if verbose:
            print(f"Left half (C0)     : {self.group_bits(left)}")
            print(f"Right half (D0)    : {self.group_bits(right)}")
            print("\nSubkey generation:")
        
        subkeys = []
        for i in range(16):
            # Left shift both halves
            left = self.left_shift(left, self.SHIFTS[i])
            right = self.left_shift(right, self.SHIFTS[i])
            
            # Combine and apply PC2
            combined = left + right
            subkey = self.permute(combined, self.PC2)
            subkeys.append(subkey)
            
            if verbose:
                print(f"K{i+1:<2}                : {self.group_bits(subkey)}")
        
        return subkeys

    def f_function(self, right, subkey, verbose=False, round_num=0):
        """DES F function with detailed output"""
        # Expansion
        expanded = self.permute(right, self.E)
        if verbose:
            print(f"Expanded R{round_num-1} (E)     : {self.group_bits(expanded)}")
            print(f"Subkey K{round_num:<2}         : {self.group_bits(subkey)}")
        
        # XOR with subkey
        xored = self.xor(expanded, subkey)
        if verbose:
            print(f"After XOR (E ⊕ K)  : {self.group_bits(xored)}")
        
        # S-box substitution
        result = []
        for i in range(8):
            block = xored[i*6:(i+1)*6]
            row = (block[0] << 1) | block[5]
            col = (block[1] << 3) | (block[2] << 2) | (block[3] << 1) | block[4]
            val = self.SBOX[i][row][col]
            
            # Convert to 4 bits
            for j in range(3, -1, -1):
                result.append((val >> j) & 1)
        
        if verbose:
            print(f"After S-Box        : {self.group_bits(result)}")
        
        # P permutation
        final_result = self.permute(result, self.P)
        if verbose:
            print(f"After P-box Perm   : {self.group_bits(final_result)}")
        
        return final_result

    def des_round(self, left, right, subkey, verbose=False, round_num=0):
        """Single DES round with detailed output"""
        if verbose:
            print(f"\n--- Round {round_num:2} ---")
        
        new_left = right
        f_result = self.f_function(right, subkey, verbose, round_num)
        new_right = self.xor(left, f_result)
        
        if verbose:
            print(f"L{round_num:<2} = R{round_num-1:<2}          : {self.group_bits(new_left)}")
            print(f"R{round_num:<2} = L{round_num-1:<2} ⊕ F      : {self.group_bits(new_right)}")
        
        return new_left, new_right

    def encrypt_block(self, block, subkeys, verbose=False):
        """Encrypt a single 64-bit block with detailed output"""
        if verbose:
            print(f"Input block        : {self.group_bits(block)}")
        
        # Initial permutation
        ip_result = self.permute(block, self.IP)
        
        if verbose:
            print(f"After IP           : {self.group_bits(ip_result)}")
        
        # Split into left and right halves
        left = ip_result[:32]
        right = ip_result[32:]
        
        if verbose:
            print(f"\nInitial Permutation (IP):")
            print(f"L0                : {self.group_bits(left)}")
            print(f"R0                : {self.group_bits(right)}")
        
        # 16 rounds
        for i in range(16):
            left, right = self.des_round(left, right, subkeys[i], verbose, i+1)
        
        # Final swap and permutation
        combined = right + left
        if verbose:
            print(f"\nBefore final perm  : {self.group_bits(combined)}")
        
        final_result = self.permute(combined, self.FP)
        
        if verbose:
            print(f"After final perm   : {self.group_bits(final_result)}")
        
        return final_result

    def decrypt_block(self, block, subkeys, verbose=False):
        """Decrypt a single 64-bit block"""
        # Use subkeys in reverse order for decryption
        return self.encrypt_block(block, subkeys[::-1], verbose)

    def encrypt(self, plaintext, key, verbose=False):
        """Encrypt plaintext using DES with detailed output"""
        if verbose:
            print("="*80)
            print("DES ENCRYPTION PROCESS")
            print("="*80)
            print(f"Plaintext: {plaintext}")
            print(f"Key: {key}")
            print("="*80)
        
        # Generate subkeys
        subkeys = self.generate_keys(key, verbose)
        
        # Convert plaintext to bits and pad
        bits = self.string_to_bits(plaintext)
        bits = self.pad_data(bits)
        
        # Encrypt each 64-bit block
        ciphertext_bits = []
        block_num = 1
        for i in range(0, len(bits), 64):
            block = bits[i:i+64]
            if verbose:
                print(f"\n{'='*80}")
                print(f"ENCRYPTING BLOCK {block_num}")
                print(f"{'='*80}")
            encrypted_block = self.encrypt_block(block, subkeys, verbose)
            ciphertext_bits.extend(encrypted_block)
            block_num += 1
        
        return ciphertext_bits

    def decrypt(self, ciphertext_bits, key, verbose=False):
        """Decrypt ciphertext using DES with detailed output"""
        if verbose:
            print("="*80)
            print("DES DECRYPTION PROCESS")
            print("="*80)
            print(f"Key: {key}")
            print("="*80)
        
        # Generate subkeys
        subkeys = self.generate_keys(key, verbose)
        
        # Decrypt each 64-bit block
        plaintext_bits = []
        block_num = 1
        for i in range(0, len(ciphertext_bits), 64):
            block = ciphertext_bits[i:i+64]
            if verbose:
                print(f"\n{'='*80}")
                print(f"DECRYPTING BLOCK {block_num}")
                print(f"{'='*80}")
            decrypted_block = self.decrypt_block(block, subkeys, verbose)
            plaintext_bits.extend(decrypted_block)
            block_num += 1
        
        # Convert back to string and remove padding
        plaintext = self.bits_to_string(plaintext_bits)
        return plaintext.rstrip('\x00')


def encrypt_des(plaintext, key, verbose=False):
    des = DES()
    return des.encrypt(plaintext, key, verbose)


def decrypt_des(ciphertext_bits, key, verbose=False):
    des = DES()
    return des.decrypt(ciphertext_bits, key, verbose)


if __name__ == "__main__":
    # Test enkripsi dan dekripsi
    plaintext = "TUBES? 17 HARI?"
    key = "CAPEKASLI"  # 8-character key
    
    print("BASIC TEST (without detailed output):")
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    
    # Basic encryption
    encrypted = encrypt_des(plaintext, key, verbose=False)
    print(f"Encrypted (bits): {len(encrypted)} bits")
    print(f"Encrypted (hex): {hex(int(''.join(map(str, encrypted)), 2))}")
    
    # Basic decryption
    decrypted = decrypt_des(encrypted, key, verbose=False)
    print(f"Decrypted: {decrypted}")
    print(f"Encryption successful: {plaintext == decrypted}")
    
    print("\n" + "="*80)
    print("DETAILED TEST (with step-by-step output):")
    print("="*80)
    
    # Detailed encryption
    encrypted_verbose = encrypt_des(plaintext, key, verbose=True)
    
    # Detailed decryption
    print("\n")
    decrypted_verbose = decrypt_des(encrypted_verbose, key, verbose=True)
    
    print(f"\nFinal Result: {decrypted_verbose}")
    print(f"Verification: {plaintext == decrypted_verbose}")
