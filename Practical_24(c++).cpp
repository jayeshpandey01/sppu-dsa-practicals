'''
  Write C++ program to realize Set using Generalized Liked List (GLL) 
e.g. A ={ a, b, {c, d,e, {}, {f,g}, h, I, {j,k}, l, m}. Store and print as set notation.
  '''

  #include<iostream>
using namespace std;

// Structure for GLL node
struct GLLNode {
    char symbol;
    GLLNode* next;
    GLLNode* down;
};

// Function to create a new GLL node
GLLNode* createNode(char symbol) {
    GLLNode* newNode = new GLLNode;
    newNode->symbol = symbol;
    newNode->next = newNode->down = nullptr;
    return newNode;
}

// Function to insert a new element into the GLL set
GLLNode* insertSet(GLLNode* root, char symbol) {
    if (root == nullptr) {
        root = createNode(symbol);
    } else if (symbol < root->symbol) {
        GLLNode* temp = createNode(symbol);
        temp->next = root;
        root = temp;
    } else if (symbol > root->symbol) {
        root->down = insertSet(root->down, symbol);
    }
    return root;
}

// Function to display the GLL set in set notation
void displaySet(GLLNode* root) {
    if (root == nullptr)
        return;

    if (root->symbol == '{') {
        cout << root->symbol;
        displaySet(root->down);
        cout << "}" << " ";
    } else {
        cout << root->symbol << " ";
    }

    displaySet(root->next);
}

int main() {
    GLLNode* set = nullptr;

    // Inserting elements into the set
    set = insertSet(set, 'a');
    set = insertSet(set, 'b');
    set = insertSet(set, 'c');
    set = insertSet(set, 'd');

    GLLNode* nestedSet1 = createNode('{');
    nestedSet1->down = insertSet(nestedSet1->down, 'f');
    nestedSet1->down = insertSet(nestedSet1->down, 'g');

    GLLNode* nestedSet2 = createNode('{');
    nestedSet2->down = insertSet(nestedSet2->down, 'j');
    nestedSet2->down = insertSet(nestedSet2->down, 'k');

    set = insertSet(set, 'e');
    set = insertSet(set, '{');
    set = insertSet(set, '}');
    set = insertSet(set, 'h');
    set = insertSet(set, 'i');
    set = insertSet(set, nestedSet1);
    set = insertSet(set, 'l');
    set = insertSet(set, 'm');
    set = insertSet(set, nestedSet2);

    // Displaying the set in set notation
    cout << "Set: ";
    displaySet(set);

    return 0;
}
