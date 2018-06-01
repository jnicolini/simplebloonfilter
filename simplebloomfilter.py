from bitarray import bitarray
import mmh3

class SimpleBloomFilter:
	def __init__(self, array_size, hash_iter):
# for our Bloom filter we're going to need two variables, the bit array size and the number of times we are going to run the hash function in our string
		self.array_size = array_size
		self.hash_iter = hash_iter
		self.bit_array = bitarray(array_size)
		self.bit_array.setall(0) # setter to initialize all the bits in the array to 0


	def put_item(self, item):
		for i in range(self.hash_iter):
			bit = mmh3.hash(item,i) % self.array_size
			self.bit_array[bit] = 1

	def get_item(self, item):
		for i in range(self.hash_iter):
			bit = mmh3.hash(item,i) % self.array_size
			if self.bit_array[bit] == 0:
				return "The item %s is not in the list" % (item)
			else:
				return "The item %s is PROBABLY in the list" % (item)


