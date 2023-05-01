#include <iostream>
#include <vector>

// class Node{
//     int data;
//      next;
// }

using namespace std;

class Node
{
public:
    int data;
    Node *next;
    Node(int d) : data(d), next(NULL) {}
};

class Single_Linked_List
{
public:
    Node *head;
    Single_Linked_List()
    {
        head = NULL;
    }

    void create(int data)
    {
        if (head == NULL)
        {
            Node *node = new Node(data);
            head = node;
        }
        else
        {
            cout << "Node exists, start pushing data to the node!\nHint: use push_end() or push_start() instead;" << endl;
        }
    }

    void push_end(int data)
    {
        // initiallise new node
        Node *new_node = new Node(data);
        if (head == NULL)
        {
            cout << "Please create a node before pushing the data!\nHint: Use create() instead" << endl;
        }
        else
        {
            // To store a the head in a dummy node and update it untill we reach the end of the node
            Node *temp = head;

            // Cant use a dot operator as it will not work with pointers
            while (temp->next != NULL)
            {
                temp = temp->next;
            }
            temp->next = new_node;
        }
    }

    void push_front(int data)
    {
        if (head != NULL)
        {
            // initiallise new node
            Node *new_node = new Node(data);
            new_node->next = head;
            head = new_node;
        }
        else
        {
            cout << "Please create a node before pushing the data!\nHint: Use create() instead" << endl;
        }
    }

    void pop()
    {
        if (head == NULL)
        {
            cout << "There are no nodes to remove" << endl;
        }
        else
        {
            Node *temp = head;
            if (head->next == NULL)
            {
                delete head;
                head = NULL;
            }
            else
            {
                while (temp->next->next != NULL)
                {
                    temp = temp->next;
                }
                delete temp->next;
                temp->next = NULL;
            }
        }
    }

    void Display()
    {
        if (head == NULL)
        {
            cout << "There are no nodes to display" << endl;
        }
        else
        {
            cout << "The nodes are as follows: ";
            int count = 1;
            Node *current_node = head;
            while (current_node->next != NULL)
            {
                count++;
                cout << current_node->data << " -> ";
                current_node = current_node->next;
            }
            // Printing out the last node
            cout << current_node->data << endl;
        }
    }
};

int main()
{
    Single_Linked_List Linked_List;
    bool condition = true;

    while (condition)
    {
        cout << "Menu" << endl;
        cout << "\t1. Create" << endl;
        cout << "\t2. Push end" << endl;
        cout << "\t3. Push front" << endl;
        cout << "\t4. Pop" << endl;
        cout << "\t5. Display" << endl;
        cout << "\t6. Quit" << endl;
        int query;
        cout << "Enter your choice: ";
        cin >> query;
        switch (query)
        {
        case 1:
        {
            int data;
            cout << "Enter data: ";
            cin >> data;
            Linked_List.create(data);
            break;
        }
        case 2:
        {
            int data;
            cout << "Enter data: ";
            cin >> data;
            Linked_List.push_end(data);
            break;
        }
        case 3:
        {
            int data;
            cout << "Enter data: ";
            cin >> data;
            Linked_List.push_front(data);
            break;
        }
        case 4:
        {
            Linked_List.pop();
            break;
        }
        case 5:
        {
            Linked_List.Display();
            break;
        }
        case 6:
            condition = false;
            cout << "Quitting..." << endl;
            break;
        default:
            cout << "Please enter a valid condition\n\nOptions ranging from 1 to 6" << endl;
        }
    }
}