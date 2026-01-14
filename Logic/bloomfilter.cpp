#include <vector>
#include <iostream>
#include <cmath>
#include <functional>
#include <string>

class bloomFilter {
    public:

        // Insertion function into the bloom filter
        void insert(const std::string& element){

            // Most important loop: runs the input through each hash function and sets that value in bits array to one
            for (int i = 0; i < numHashFunctions; i++) {
                std::size_t index = hashN(element, i);
                bitArray[index] = true;
            }
            numElements++;

        }

        // Look up functions (possible to give false positives)
        bool lookup(const std::string& element) const {
            for (int i = 0; i < numHashFunctions; i++) {
                std::size_t index = hashN(element, i);
                
                // If any bit set to zero
                if (!bitArray[index]) { 
                    return false;        
                }
            }
            return true;  // All bits were 1, probably in the set
        }

        // Constructor for only size known
        bloomFilter(std::size_t numBits, std::size_t numHashFunctions){
            
            // Resizing the bool array for the provided number of bits
            bitArray.resize(numBits, false);

            // Setting num hash functions
            setNumHashFunctions(numHashFunctions);
        }
 
        // Returns the probability that a false positive will occur (formula from geeks for geeks)
        double probFalsePos() const{
            return std::pow(1 - std::pow(1 - 1.0/(bitArray.size()), numHashFunctions*numElements), numHashFunctions);                                                                                                      ^ add semicolon
        }

        // Getter for number elements, no setter since we calculate as we add
        std::size_t getNumElements() const{
            return numElements;
        }

        // Getters and setters for num hash functions
        void setNumHashFunctions(std::size_t input){
            numHashFunctions = input;
        }

        std::size_t getNumHashFunctions() const{
            return numHashFunctions;
        }

        // clears the entire filter along with all the elements
        void clear(){
            std::fill(bitArray.begin(), bitArray.end(), false);
            numElements = 0;  // Also reset counter
        }

        // Base inbuilt hashing function
        unsigned long long hash1(const std::string& input) const {
            std::hash<std::string> hasher;
            return hasher(input);
        }

        // Hash funciton 2 with a seed and distribution 
        unsigned long long hash2(const std::string& input) const {
            unsigned long long hash = 5381;
            for (char c : input) {
                hash = ((hash << 5) + hash) + c;
            }
            return hash;
        }

        // Generate N different hashes using double hashing, super cool
        unsigned long long hashN(const std::string& input, int n) const {
            return (hash1(input) + n * hash2(input)) % bitArray.size();
        }
        
    private:
        // Counts the number of elements currently in the filter
        std::size_t numElements{};

        // The actual filter storing the bit data 
        std::vector<bool> bitArray{};

        // The number of hashfunctions used in the filter
        std::size_t numHashFunctions{};
};