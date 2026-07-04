/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    int cnt=0;
    struct ListNode* temp=head;
    if (head==NULL || head->next==NULL){
        return head;
        }
    while(temp!=NULL){
        cnt++;
        temp=temp->next;
    }
    int mid=(cnt/2)+1;
    temp=head;

    while(temp!=NULL){
        mid=mid-1;

        if (mid==0){
            break;
        }
        temp=temp->next;
    }
     return temp;  
}