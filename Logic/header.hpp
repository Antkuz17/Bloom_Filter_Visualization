class bloomFilter {
    public:

        // Insertion function into the bloom filter
        void insert(auto element);

        // Look up functions (possible to give false positives)
        bool lookup(auto element);

        // Constructor for only size known
        bloomFilter(std::size_t size);

        // Returns the probability that a false positive will occur 
        double probFalsePos();

        // Getters and setters for num elements
        void setNumElements();
        std::size_t setNumElements();

        // Getters and setters for num hash functions
        void setNumHashFunctions(std::size_t numHashfunctions);
        std::size_t getNumHashFunctions();

        // clears the entire filter along with all the elements
        
    private:
        std::size_t numElements{};
        bool *bloomBits{nullptr};
        std::size_t numHashfunctions{};




}