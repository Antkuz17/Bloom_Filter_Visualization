    #include <pybind11/pybind11.h>
    #include <pybind11/stl.h>  // For automatic conversion of std::vector, std::string
    #include "bloomFilter.h"   // Your bloom filter header

    namespace py = pybind11;

    PYBIND11_MODULE(bloom, m) {
        m.doc() = "Bloom Filter Python bindings";  // Module docstring

        py::class_<bloomFilter>(m, "BloomFilter")
            .def(py::init<std::size_t, std::size_t>(), 
                py::arg("numBits"), 
                py::arg("numHashFunctions"))
            .def("insert", &bloomFilter::insert)
            .def("lookup", &bloomFilter::lookup)
            .def("clear", &bloomFilter::clear)
            .def("get_num_elements", &bloomFilter::getNumElements)
            .def("get_num_hash_functions", &bloomFilter::getNumHashFunctions)
            .def("prob_false_pos", &bloomFilter::probFalsePos);
    }