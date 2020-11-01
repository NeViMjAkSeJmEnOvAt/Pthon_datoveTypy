strikacky = 'Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech'

def charFrequency(strikacky):
    frequency = {}
    for x in strikacky:
        if x in frequency:
            frequency[x] += 1
        else:
            frequency[x] = 1
    print(frequency)

charFrequency(strikacky)