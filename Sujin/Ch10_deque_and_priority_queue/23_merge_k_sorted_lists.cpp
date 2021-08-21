#include <iostream>
#include <vector>
#include <queue>
using namespace std;

 struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};

struct compare{
    bool operator()(ListNode* &a, ListNode* &b){
        return (a->val) > (b->val); // 오름차순 정렬
    }
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode* >, compare> pq;
        
        ListNode* head = new ListNode(0);
        ListNode* tmp = head;
        
        for(int i=0; i<lists.size(); i++){
            if(lists[i]!=NULL) pq.push(lists[i]);
        }
        while(pq.size()>0){
            ListNode* p = pq.top();
            tmp->next = new ListNode(p->val);
            tmp = tmp->next;
            pq.pop();
            if(p->next!=NULL) pq.push(p->next);
        }
        
        return head->next;
    }
};