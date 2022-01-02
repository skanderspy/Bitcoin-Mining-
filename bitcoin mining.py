from hashlib import sha256
import time
MAX_NONCE = 100000000000
def SHA256(text):
    return (sha256(text.encode("ascii")).hexdigest())

def mine(block_num,transactions, previous_hash,prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_num) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print("Yay! Successfully mined bitcoins with nonce value:",{nonce})
            return new_hash

    raise BaseException("Couldn't find correct has after trying these many times:",MAX_NONCE)


if __name__ == '__main__':
    #print(SHA256("ABC"))
    transactions = '''
    Praneeth -> Ajay -> 120, 
    Ajay -> James -> 40,
    Melinda -> Praneeth -> 20 
    '''
    difficulty = 6
    start = time.time()
    print("start mining")
    new_hash = mine(3,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7',difficulty)
    total_time = str((time.time() - start))
    print("End mining...")
    print("Time taken(sec):",total_time)
    print(new_hash)

