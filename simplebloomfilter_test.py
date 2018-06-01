from simplebloomfilter import SimpleBloomFilter



lines = ['hola', 'hello', 'ciao', 'buongiorno', 'konichiwa', '124kge', 'kease',
		'testing', 'randomwords', 'loremipsum', 'something']

test = ['hola', 'mistake', 'something', 'buonanotte', 'chau', 'goodbye','hello', 'isthisworking?', 'andthis?', 'victory']
def test_filter(n,p):
	testcase = SimpleBloomFilter(n,p)
	for line in lines:
		testcase.put_item(line)

	for i in test:
		print(testcase.get_item(i))

test_filter(10000, 5) #10000b array 5 hash function iterations
test_filter(5000,2)