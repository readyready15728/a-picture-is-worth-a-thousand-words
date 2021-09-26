# A Picture Is Worth A Thousand Words
## Or is it really?

I've been thinking about that aphorism lately and quantifying it in
information-theoretic terms. To that end, I stole some Python from Rosetta
Code, calculated the entropy of every word in `/usr/share/dict/words`,
averaged over those 100,000+ words, then multiplied that by 1,000 to get the
size of a picture in bits:

```
A picture is worth ~1000 × 2.91, or ~2909.56 bits
```

Accordingly, here are a little over 214 pictures of Claude Shannon:

![214 Claude Shannons](claude-shannon.jpg)
