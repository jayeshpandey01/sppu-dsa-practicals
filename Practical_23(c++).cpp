'''
  
Write C++ program for storing binary number using doubly linked lists. Write functions
a) To compute 1‘s and 2‘s complement 
b) Add two binary numbers

'''

#include <iostream>
using namespace std;

// Structure for the doubly linked list node
struct Node {
    int data;
    Node* prev;
    Node* next;
};

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = new Node();
    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = NULL;
    return newNode;
}

// Function to insert a node at the end of the doubly linked list
Node* insertEnd(Node* head, int data) {
    if (head == NULL) {
        head = createNode(data);
        return head;
    }
    Node* temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    Node* newNode = createNode(data);
    temp->next = newNode;
    newNode->prev = temp;
    return head;
}

// Function to get the 1's complement of a binary number
void onesComplement(Node* head) {
    Node* temp = head;
    while (temp != NULL) {
        temp->data = (temp->data == 0) ? 1 : 0;
        temp = temp->next;
    }
}

// Function to get the 2's complement of a binary number
void twosComplement(Node* head) {
    Node* temp = head;
    int carry = 1;

    // Find the rightmost 1 in the list
    while (temp->next != NULL) {
        temp = temp->next;
    }

    // Perform 1's complement
    while (temp != NULL) {
        temp->data = (temp->data == 0) ? 1 : 0;
        temp = temp->prev;
    }

    // Add 1 to the 1's complement
    temp = head;
    while (temp != NULL) {
        int sum = temp->data + carry;
        temp->data = sum % 2;
        carry = sum / 2;
        temp = temp->next;
    }
}

// Function to add two binary numbers
Node* addBinaryNumbers(Node* head1, Node* head2) {
    Node* sumHead = NULL;
    int carry = 0;

    Node* temp1 = head1;
    Node* temp2 = head2;

    while (temp1->next != NULL) {
        temp1 = temp1->next;
    }
    while (temp2->next != NULL) {
        temp2 = temp2->next;
    }

    // Start adding the binary numbers from the rightmost bits
    while (temp1 != NULL || temp2 != NULL) {
        int sum = carry;
        if (temp1 != NULL) {
            sum += temp1->data;
            temp1 = temp1->prev;
        }
        if (temp2 != NULL) {
            sum += temp2->data;
            temp2 = temp2->prev;
        }
        carry = sum / 2;
        sum %= 2;
        sumHead = insertEnd(sumHead, sum);
    }

    // Add the remaining carry if any
    if (carry != 0) {
        sumHead = insertEnd(sumHead, carry);
    }

    return sumHead;
}

// Function to display the binary number
void displayBinaryNumber(Node* head) {
    Node* temp = head;
    while (temp != NULL) {
        cout << temp->data;
        temp = temp->next;
    }
    cout << endl;
}

int main() {
    Node* binaryNumber1 = NULL;
    Node* binaryNumber2 = NULL;

    // Input first binary number
    cout << "Enter binary number 1: ";
    string num1;
    cin >> num1;
    for (int i = 0; i < num1.length(); i++) {
        int digit = num1[i] - '0';
        binaryNumber1 = insertEnd(binaryNumber1, digit);
    }

    // Input second binary number
    cout << "Enter binary number 2: ";
    string num2;
    cin >> num2;
    for (int i = 0; i < num2.length(); i++) {
        int digit = num2[i] - '0';
        binaryNumber2 = insertEnd(binaryNumber2, digit);
    }

    cout << "Binary Number 1: ";
    displayBinaryNumber(binaryNumber1);

    cout << "Binary Number 2: ";
    displayBinaryNumber(binaryNumber2);

    cout << "1's Complement of Binary Number 1: ";
    onesComplement(binaryNumber1);
    displayBinaryNumber(binaryNumber1);

    cout << "2's Complement of Binary Number 2: ";
    twosComplement(binaryNumber2);
    displayBinaryNumber(binaryNumber2);

    cout << "Sum of Binary Number 1 and Binary Number 2: ";
    Node* sum = addBinaryNumbers(binaryNumber1, binaryNumber2);
    displayBinaryNumber(sum);

    return 0;
}
