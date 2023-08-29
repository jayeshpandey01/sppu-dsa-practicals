'''
Second year Computer Engineering class, set A of students like Vanilla Ice-cream and set 
B of students like butterscotch ice-cream. Write C++ program to store two sets using 
linked list. compute and displaya) Set of students who like both vanilla and butterscotch
b) Set of students who like either vanilla or butterscotch or not both
c) Number of students who like neither vanilla nor butterscotch
'''

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

Node* insertNode(Node* head, int value) {
    Node* newNode = new Node();
    newNode->data = value;
    newNode->next = NULL;

    if (head == NULL) {
        head = newNode;
    }
    else {
        Node* current = head;
        while (current->next != NULL) {
            current = current->next;
        }

        current->next = newNode;
    }

    return head;
}

Node* intersection(Node* setA, Node* setB) {
    Node* result = NULL;

    Node* currentA = setA;
    while (currentA != NULL) {
        Node* currentB = setB;
        while (currentB != NULL) {
            if (currentA->data == currentB->data) {
                result = insertNode(result, currentA->data);
                break;
            }
            currentB = currentB->next;
        }
        currentA = currentA->next;
    }

    return result;
}

Node* unionSet(Node* setA, Node* setB) {
    Node* result = NULL;

    Node* currentA = setA;
    while (currentA != NULL) {
        result = insertNode(result, currentA->data);
        currentA = currentA->next;
    }

    Node* currentB = setB;
    while (currentB != NULL) {
        bool found = false;
        Node* currentResult = result;
        while (currentResult != NULL) {
            if (currentResult->data == currentB->data) {
                found = true;
                break;
            }
            currentResult = currentResult->next;
        }

        if (!found) {
            result = insertNode(result, currentB->data);
        }

        currentB = currentB->next;
    }

    return result;
}

int countElements(Node* head) {
    int count = 0;
    Node* current = head;
    while (current != NULL) {
        count++;
        current = current->next;
    }
    return count;
}

void displaySet(Node* head) {
    Node* current = head;
    while (current != NULL) {
        cout << current->data << " ";
        current = current->next;
    }
    cout << endl;
}

int main() {
    Node* setA = NULL;
    Node* setB = NULL;

    // Adding elements to setA
    setA = insertNode(setA, 1);
    setA = insertNode(setA, 2);
    setA = insertNode(setA, 3);
    setA = insertNode(setA, 4);

    // Adding elements to setB
    setB = insertNode(setB, 3);
    setB = insertNode(setB, 4);
    setB = insertNode(setB, 5);
    setB = insertNode(setB, 6);

    cout << "Set A: ";
    displaySet(setA);

    cout << "Set B: ";
    displaySet(setB);

    Node* intersectionSet = intersection(setA, setB);
    cout << "Set of students who like both vanilla and butterscotch: ";
    displaySet(intersectionSet);

    Node* unionSet = unionSet(setA, setB);
    cout << "Set of students who like either vanilla or butterscotch or not both: ";
    displaySet(unionSet);

    int countNeither = countElements(setA) + countElements(setB) - countElements(unionSet);
    cout << "Number of students who like neither vanilla nor butterscotch: " << countNeither << endl;

    return 0;
}
