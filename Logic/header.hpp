#include <vector>
#include <iostream>

class bloomFilter {
    public:

        // Insertion function into the bloom filter
        void insert(const std::string& element);

        // Look up functions (possible to give false positives)
        bool lookup(const std::string& element) const;

        // Constructor for only size known
        bloomFilter(std::size_t size, std::size_t numHashFunctions);

        // Returns the probability that a false positive will occur 
        double probFalsePos() const;

        // Getter for number elements, no setter since we calculate as we add
        std::size_t getNumElements() const;

        // Getters and setters for num hash functions
        void setNumHashFunctions(std::size_t numHashFunctions);
        std::size_t getNumHashFunctions() const;

        // clears the entire filter along with all the elements
        void clear();

        // Hash function 1
        unsigned long long hash1(auto input) const;

        // Hash function 1
        unsigned long long hash2(auto input) const;

    
        
    private:
        // Counts the number of elements currently in the filter
        std::size_t numElements{};

        // The actual filter storing the bit data 
        std::vector<bool> bitArray{};

        // The number of hashfunctions used in the filter
        std::size_t numHashFunctions{};






};