import json
from urllib.request import Request, urlopen
import time
from threading import Thread, Lock

websites = ["https://www.rfc-editor.org/rfc-index.txt", "https://www.rfc-editor.org/rfc/rfc1000.txt"]
print("Counting alphabet on websites: \n{}".format(("\n".join(websites))))
finished_count = 0

def count_letters(url, freq, mutex):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    req = Request(url, headers=headers)
    response = urlopen(req)
    data = str(response.read())

    mutex.acquire()
    for l in data:
        letter = l.lower()
        if letter in freq:
            freq[letter] += 1
    global finished_count
    finished_count += 1
    mutex.release()

def main():
    freq = {}
    mutex = Lock()
    for c in "abcdefghijklmnopqrstuvwxyz":
        freq[c] = 0
    start = time.time()
    for i in range(len(websites)):
        Thread(target=count_letters, args=(websites[i], freq, mutex)).start()

    while True:
        mutex.acquire()
        if finished_count == len(websites):
            break
        mutex.release()
    finish = time.time()
    print(json.dumps(freq, indent=4))
    print("\nThe program took {:.2f} seconds to execute.".format(finish-start))

main()