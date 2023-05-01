#include <iostream>
#include <vector>


using namespace std;
class Node {
    public:
        Node* prev;
        int data;
        Node* next;
        Node(int data) {
            this->prev = NULL;
            this->data = data;
            next = NULL;
        }
};

class Double_Linked_List {
    public:
        Node* head;
        Node* tail;
        Double_Linked_List() {
            this->head = NULL;
            tail = NULL;
        }

        void create() {
            int data;
            cout << "Enter data: ";
            cin >> data;
            Node* new_node = new Node(data);
            head = new_node;
            tail = new_node;
            cout << data << ":" << new_node << endl;
        }

        void insertion() {
            if (head == NULL) {
                cout << "Create a node and then try to insert new nodes" << endl;
            } else {
                int choice;
                cout << "Insert at:\n\t1. Start\n\t2. End" << endl;
                cout << "Enter choice: ";
                cin >> choice;
                int data;
                cout << "Enter data: ";
                cin >> data;
                switch(choice) {
                    case 1: {
                        Node* new_node = new Node(data);
                        head->prev = new_node;
                        new_node->next = head;

                        if (head->next == NULL){
                            tail = head;
                        }
                        head = new_node;

                        cout << data << ":" << new_node << endl;
                        cout << new_node->prev << " - " << new_node->data << " - " << new_node->next << endl;
                        break;
                    }
                    case 2: {
                        Node* new_node = new Node(data);
                        new_node->prev = tail;
                        tail->next = new_node;
                        tail = new_node;
                        cout << new_node->prev << " - " << new_node->data << " - " << new_node->next << endl;
                        break;
                    }
                    default : {
                        cout << "Please select a valid choice..." << endl;
                    }
                }
                
            }
        }

        void deletion() {
            if (tail == NULL || head == NULL) {
                cout << "There are no nodes left to delete" << endl;
            } else {
                Node* tail_node = tail;

                if (tail->prev == NULL) {
                    head = NULL;
                    tail = NULL;
                } else {
                    tail->prev->next = NULL;
                    tail = tail->prev;
                }
                delete tail_node;
            }
        }
        void display() {
            if(head == NULL) {
                cout << "No nodes to display..." << endl;
            } else {
                cout << "Select:\n\t1. From start\n\t2. From end" << endl;
                int choice;
                cout << "Enter your choice: ";
                cin >> choice;
                switch (choice) {
                    case 1:{
                        Node* curr_node = head;
                        cout << "Printing values from the start..." << endl;
                        while (curr_node->next != NULL) {
                            // cout << curr_node->data << "  ";
                            cout << curr_node->prev << " - " << curr_node->data << " - " << curr_node->next << "  ";
                            curr_node = curr_node->next;
                        }
                        cout << curr_node->prev << " - " << curr_node->data << " - " << curr_node->next << endl;
                        break;
                    };
                    case 2:{
                        Node* curr_node = tail;
                        cout << "Printing values from the end..." << endl;
                        while (curr_node->prev != NULL) {
                            cout << curr_node->prev << " - " << curr_node->data << " - " << curr_node->next << "  ";
                            curr_node = curr_node->prev;
                        }
                        // cout << curr_node->data << endl;
                        cout << curr_node->prev << " - " << curr_node->data << " - " << curr_node->next << endl;
                        break;
                    };
                    default: {
                        cout << "Select a valid choice: " << endl;
                        break;
                    }
                }
            }
        }
};


int main() {
    // Class_Name name = new Class_Name is different from Class_Name name;
    Double_Linked_List dll;
    bool cnd = true;
    while (cnd) {
        cout << "Menu:\n\t1. Create\n\t2. Insert\n\t3. Display\n\t4. Delete\n\t5. Quit" << endl;
        int query;
        cout << "Enter your choice: ";
        cin >> query;
        switch (query) {
            case 1:
                dll.create();
                break;
            case 2:
                dll.insertion();
                break;
            case 3:
                dll.display();
                break;
            case 4:
                dll.deletion();
                break;
            case 5:
                cnd = false;
                cout << "Quitting..." << endl;
                break;
            default:
                cout << "Please select a valid choice: " << endl;
                break;
        }
    }
    return 0;
}