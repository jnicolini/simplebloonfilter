# simplebloonfilter

This is a simple implementation of a Bloom Filter I made with Python 3

It took me a little more than I expected, not for code complexity but to figure out the best hash function to include in the implementation which is murmurhash 3, also I've used a bitarray because I've decided to use proper data types for this so you should import those libraries.

Regarding the filter the main complication I see here is the space-time trade-off we have to decide between staying wth low hash function iterations and a small array and risk false positives, or risk performance and make the process a lot more complex with big arrays and more iterations but lowering the chance of false positives.  

Finally, this exercise was kind of difficult considering I use Python mostly for automation purposes and this is not what I'm used to.
