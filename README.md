# Bloom Filter Visualizer

[![Bloom Filter Demo](https://img.youtube.com/vi/1wrPEuHxkR4/maxresdefault.jpg)](https://www.youtube.com/watch?v=1wrPEuHxkR4)

## What is a Bloom Filter?

A bloom filter is a space-efficient probabilistic data structure used to test whether an element is a member of a set. It can definitively tell you when an element is not in a set, but can only tell you an element might be in a set with a small probability of false positives.

## Why Use Bloom Filters Over Hash Maps?

Bloom filters use approximately 10 bits per element, while hash maps typically require 50-100 bytes per element. This means bloom filters are 40-80 times more memory efficient than hash maps.

The tradeoff is that bloom filters have a tunable false positive rate and cannot retrieve stored values or delete elements, while hash maps provide exact lookups and support deletions.

## Why I Built This

I built this visualization to understand bloom filters from the ground up by implementing the core algorithm in C++ for performance and learning low-level data structure design.

I used pybind11 to create Python bindings for the C++ implementation, allowing me to learn how to integrate compiled code with higher-level languages.

The GUI is built with Tkinter to provide real-time visualization of how bits are set in the filter as elements are inserted, making the abstract concept of probabilistic data structures concrete and interactive. The interface uses GitHub's color palette and contribution grid styling for a clean, familiar aesthetic.
