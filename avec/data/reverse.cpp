/* copied from https://github.com/alexprut/HackerRank/blob/master/Data%20Structures/Linked%20Lists/Print%20in%20Reverse/Solution.cpp
  Print elements of a linked list in reverse order as standard output
  head pointer could be NULL as well for empty list
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
void ReversePrint(Node *head)
{
    if (head != NULL) {
        if (head->next != NULL) {
            ReversePrint(head->next);
        }
        cout << head->data << "\n";
    }
}