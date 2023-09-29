struct Node {
    bool end;
    vector<Node*> child;

    Node() {
        end = false;
        child = vector<Node*>(2, nullptr);
    }
};

class Trie {
public:
    Node* root;

    Trie() {
        root = new Node();
    }

    void insert(int value) {
        Node* curr = root;
        for (int i = 30; i >= 0; i--) {
            int index = ((1 << i) & value) >> i;
            if (curr->child[index] == nullptr) {
                curr->child[index] = new Node();
            }
            curr = curr->child[index];
        }
        curr->end = true;
    }
};

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int answer = 0;
        Trie tree;
        for (int num : nums) {
            int temp = 0;
            Node* node = tree.root;
            for (int i = 30; i >= 0; i--) {
                int bit = ((1 << i) & num) >> i;
                if (node && node->child[1 - bit]) {
                    temp |= (1 << i);
                    node = node->child[1 - bit];
                } else if (node && node->child[bit]) {
                    node = node->child[bit];
                } else if ((answer & (1 << i)) > (temp & (1 << i))) {
                    break;
                }
            }
            answer = max(answer, temp);
            tree.insert(num);
        }
        return answer;
    }
};
