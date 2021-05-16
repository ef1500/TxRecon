# TxRecon
TxRecon is a script that can find the connections of any two twitter users. TxRecon also uses [WhatsMyName](https://github.com/WebBreacher/WhatsMyName), which is a high-speed username checker written by WebBreacher.

![TxTriangulation](https://user-images.githubusercontent.com/45581646/118382873-65b17e00-b5ae-11eb-9613-164a241199a4.PNG)

### Important Side note
You **MUST** have a twitter api key for this program to work.

## Usage
### General Usage
```python3 engine.py t1 t2```

This is the gneric usage of the script. If the account has a large amount of followers then you will most likey burn the API, so I'd suggest using the Mutuals Flag if you're concerned about that.

### Only searching for mutuals
```python3 engine.py t1 t2 -Mx```

This will find accounts that both targets follow, and then search them using WhatsMyName. It's ideal for accounts with large amounts of followers and it's fast.

### Searching a single target
```python3 engine.py t1 -Tx```

This will use WhatsMyName to search for the Username specified and then place it in a text file.
