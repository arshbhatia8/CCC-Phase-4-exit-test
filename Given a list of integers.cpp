SinglyLinkedListNode* condense(SinglyLinkedListNode* head) {
// your code goes here
      if(head == NULL || head->next==NULL)
       return head;
       unordered_map<int,int>m;
      // Node*newhead = NULL,*tail=NULL;
       SinglyLinkedListNode*curr=head;
       SinglyLinkedListNode*prev = NULL;
       while(curr!=NULL)
       {
           m[curr->data]++;
           if(m[curr->data]>1)
           {
              SinglyLinkedListNode*to_del = curr;
              prev->next = curr->next;
              curr = curr->next;
              delete(to_del);
           } 
           else {
             prev = curr;
             curr = curr->next;
            }
           
       }
       return head;
}
