#include <iostream>
using namespace std;

class MyHashMap {
public:
    /** Initialize your data structure here. */
    int arr[1000001];
    
    MyHashMap() {
        fill_n(arr, 1000001, -1);
    }
    
    /** value will always be non-negative. */
    void put(int key, int value) {
        arr[key] = value;
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        return arr[key];
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        arr[key]=-1;
    }
};