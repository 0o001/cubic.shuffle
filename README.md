# cubic.shuffle

key = "5-u:1:0,l:1:4,r:1:1,d:3:3"
text = "--- hello world ---"
shuffledText = CubicShuffle.shuffle(text, key)
deshuffledText = CubicShuffle.deshuffle(shuffledText, key)

print("Text:", text)
print("Shuffled Text:", shuffledText)
print("Decoded Text:", deshuffledText)
