

from collections import Counter

def decrypt_message(text, mapping):
    """Apply letter subs to decrypt text"""
    result = ""
    for char in text:
        if char.isalpha():
            result += mapping.get(char.upper(), char)
        else:
            result += char
    return result

def analyze_freq(text):
    """Count letter freq in the text"""
    letters = [c.upper() for c in text if c.isalpha()]
    return Counter(letters)

def create_mapping(cipher_freq):
    """Create subs mapping based on freq analysis"""

    english_letters = "ETANOISHRDLCFMUPYBKGVXWQ"
    
   
    cipher_letters = [letter for letter, count in cipher_freq.most_common()]
    
  
    mapping = {}
    for i, cipher_letter in enumerate(cipher_letters):
        if i < len(english_letters):
            mapping[cipher_letter] = english_letters[i]
        else:
            mapping[cipher_letter] = 'Z'
    
    return mapping

def main():

    encrypted = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""
    
    print("CRYPTO PROJECT - FREQUENCY ANALYSIS")
    print("=" * 40)
    

    print("\n1. Analyzing letter frequencies...")
    freq = analyze_freq(encrypted)
    
    print("Most common letters in ciphertext:")
    for letter, count in freq.most_common(10):
        percentage = (count / sum(freq.values())) * 100
        print(f"  {letter}: {count} times ({percentage:.1f}%)")
    

    print("\n2. Creating substitution mapping...")
    mapping = create_mapping(freq)
    
    print("Letter substitutions:")
    for cipher, plain in sorted(mapping.items()):
        print(f"  {cipher} → {plain}")
    
    # Step 3: Decrypt
    print("\n3. Decrypting message...")
    decrypted = decrypt_message(encrypted, mapping)
    
    print("\nDecrypted message:")
    print("-" * 40)
    print(decrypted)
    print("-" * 40)
    
    print("\n" + "=" * 40)
    print("Decryption complete!")
    print("Press any key to continue...")
    input()

if __name__ == "__main__":
    main()
