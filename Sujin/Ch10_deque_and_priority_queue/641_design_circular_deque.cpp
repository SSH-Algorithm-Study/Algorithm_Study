#include <iostream>
using namespace std;

struct Node{
    int val;
    Node* next;
    Node(int v, Node*n = nullptr){
        val = v;
        next = n;
    }
};

class MyCircularDeque {
public:
    Node* front = NULL;
    Node* rear = NULL;
    int count;
    int maxCount;
    /** Initialize your data structure here. Set the size of the deque to be k. */
    MyCircularDeque(int k) {
        count=0;
        maxCount=k;
    }
    
    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    bool insertFront(int value) {
        if(count==maxCount) return false;
        
        Node* nd = new Node(value);
        if(count==0){
            front = nd;
            rear = nd;
        }
        else{
            nd->next = front;
            front = nd;
        }
        count++;
        return true;
    }
    
    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    bool insertLast(int value) {
        if(count==maxCount) return false;
        
        Node* nd = new Node(value);
        if(count==0){
            front = nd;
            rear = nd;
        }
        else{
            rear->next = nd;
            rear = nd;
        }
        count++;
        return true;
    }
    
    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    bool deleteFront() {
        if(count==0) return false;
        
        Node* delNode = front; // delNode : 삭제할 노드를 가리킴
        front = front->next;
        delete(delNode);
        count--;
        return true;
    }
    
    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    bool deleteLast() {
        if(count==0) return false;
        
        Node* delNode = rear;
        
        Node* cur = front; // cur : 삭제할 노드의 이전노드를 찾기위한 포인터
        while(cur->next!=rear && count>2) cur=cur->next;
        rear = cur; // rear 자리 다시 찾아주기
        
        delete(delNode);
        count--;
        return true;
    }
    
    /** Get the front item from the deque. */
    int getFront() {
        if(count==0) return -1;
        return front->val;
    }
    
    /** Get the last item from the deque. */
    int getRear() {
        if(count==0) return -1;
        return rear->val;
    }
    
    /** Checks whether the circular deque is empty or not. */
    bool isEmpty() {
        return count==0;
    }
    
    /** Checks whether the circular deque is full or not. */
    bool isFull() {
        return count==maxCount;
    }
};