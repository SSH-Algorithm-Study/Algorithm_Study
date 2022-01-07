/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        for(auto it = head->next; it!=NULL; it=it->next){
            for(auto start = head; start!=it; start=start->next){
                if(start->val > it->val){
                    swap(start->val, it->val);
                }
            }
        } // for문 끝
        return head;
    }
};