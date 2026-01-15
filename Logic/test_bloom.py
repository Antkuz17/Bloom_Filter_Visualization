import bloom

# Create a Bloom Filter with 1000 bits and 3 hash functions
bf = bloom.BloomFilter(1000, 3)


# Add some elements
bf.insert("hello")
bf.insert("world")
bf.insert("python")

# Test lookups
print(f"Contains 'hello': {bf.lookup('hello')}")  # True
print(f"Contains 'world': {bf.lookup('world')}")  # True
print(f"Contains 'test': {bf.lookup('test')}")    # False

# Check stats
print(f"\nNumber of elements: {bf.get_num_elements()}")
print(f"Number of hash functions: {bf.get_num_hash_functions()}")
print(f"False positive probability: {bf.prob_false_pos():.6f}")

# Test clear
bf.clear()
print(f"\nAfter clear - contains 'hello': {bf.lookup('hello')}")  # Should be False
print(f"After clear - num elements: {bf.get_num_elements()}")     # Should be 0