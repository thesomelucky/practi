#include <iostream>
#include <queue>
#include <vector>
#include <string>
using namespace std;

struct Node {
    char ch;
    int freq;
    Node* left;
    Node* right;

     Node(char c, int f, Node* l = nullptr, Node* r = nullptr)
         : ch(c), freq(f), left(l), right(r) {}
};

struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq;
    }
};

void print(Node* root, const string& code) {
    if (root == nullptr) {
        return;
    }

     if (root->left == nullptr && root->right == nullptr) {
         cout << root->ch << " : "
              << (code.empty() ? "0" : code) << endl;
         return;
     }

     print(root->left, code + "0");
     print(root->right, code + "1");
}

int main() {
    int n;
    cout << "Enter the number of chars: ";
    cin >> n;

     if (!cin || n <= 0) {
         cout << "Number of characters must be positive.\n";
         return 1;
     }

     priority_queue<Node*, vector<Node*>, Compare> pq;
     cout << "Enter char and its freq: " << endl;

     for (int i = 0; i < n; ++i) {
         char c;
         int f;

       cin >> c >> f;

       if (!cin || f <= 0) {
           cout << "Frequency must be positive.\n";
           return 1;
       }

       pq.push(new Node(c, f));
   }

   while (pq.size() > 1) {
       Node* l = pq.top();
       pq.pop();
       Node* r = pq.top();
       pq.pop();
       pq.push(new Node('$', l->freq + r->freq, l, r));
   }
   Node* root = pq.top();
   print(root, "");

   return 0;
}
