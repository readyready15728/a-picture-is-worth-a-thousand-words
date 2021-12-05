# A Picture Is Worth A Thousand Words
## Or is it really?

I've been thinking about that aphorism lately and quantifying it in
information-theoretic terms. To that end, I stole some Python from Rosetta
Code, calculated the entropy of every word in `/usr/share/dict/words`,
averaged over those 100,000+ words, then multiplied that by 1,000 to get the
size of a picture in bits:

```
A picture is worth ~1000 × 2.70, or ~2702.30 bits
```

Accordingly, here are almost 231 pictures of Claude Shannon:

![231 Claude Shannons](claude-shannon.jpg)
