# cubic.shuffle

```py
""""
key meaning:
split 5
up 1 times position 0
left 1 times position 4
rigth 1 times position 1
down 3 times position 3
""""
key = "5-u:1:0,l:1:4,r:1:1,d:3:3"
text = "--- hello world ---"

shuffledText = CubicShuffle.shuffle(text, key)
deshuffledText = CubicShuffle.deshuffle(shuffledText, key)

print("Text:", text)
#output: Text: --- hello world ---

print("Shuffled Text:", shuffledText)
#output: Shuffled Text: e llowdorl  ----h-- 

print("Decoded Text:", deshuffledText)
#output: Decoded Text: --- hello world --- 
```
