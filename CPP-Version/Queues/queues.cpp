#include <iostream>
#include <vector>

using namespace std;

class Queue
{
    int queue_size;
    int front = -1;
    int rear = -1;
    int queue[];

public:
    Queue()
    {
        cout << "Enter queue size: ";
        cin >> queue_size;
    }
    void create()
    {
        for (int i = 0; i < queue_size; i++)
        {
            queue[i] = 0; // initialize each element to 0
        }
    }

    int isFull()
    {
        if (rear == queue_size - 1)
        {
            return 1;
        }
        return 0;
    }

    int isEmpty()
    {
        if (front == rear)
        {
            return 1;
        }
        return 0;
    }

    void enqueue()
    {
        cout << "Front: " << front << " Rear: " << rear << endl;
        if (isFull())
        {
            cout << "-------------Queue is full-------------" << endl;
        }
        else
        {
            rear += 1;
            int enqueue_val;
            cout << "Enter value: ";
            cin >> enqueue_val;
            queue[rear] = enqueue_val;
        }
    }

    void dequeue()
    {
        if (isEmpty())
        {
            cout << "-------------Queue is empty-------------" << endl;
        }
        else
        {
            front += 1;
            queue[front] = 0;
        }
    }

    void display()
    {
        vector<int> req_arr;
        for (int i = front + 1; i < rear + 1; i++)
        {
            cout << queue[i] << " ";
            req_arr.push_back(queue[i]);
        }
        cout << endl;
        if (req_arr.size() != 0)
        {
            cout << "-------------Queue as follows-------------" << endl;

            for (int i = front + 1; i < rear + 1; i++)
            {
                cout << queue[i] << " ";
            }
            cout << endl;
        }
        else if (req_arr.size() == 0)
        {
            if (rear == queue_size)
            {
                cout << "-------------Cannot print from an empty queue-------------" << endl;
            }
            else
            {
                cout << "-------------Enqueue elements in queue to view-------------" << endl;
            }
        }
    }
};

int main()
{
    Queue MyStack;
    MyStack.create();
    // MyStack.display();
    MyStack.enqueue();
    // MyStack.display();
    MyStack.enqueue();
    MyStack.enqueue();
    MyStack.enqueue();
    MyStack.display();
    MyStack.enqueue();
    MyStack.enqueue();
    MyStack.enqueue();
    MyStack.enqueue();
    MyStack.enqueue();
    MyStack.display();
    MyStack.enqueue();
    MyStack.enqueue();
    MyStack.display();
    MyStack.dequeue();
    MyStack.dequeue();
    MyStack.dequeue();
    MyStack.dequeue();
    MyStack.dequeue();
    MyStack.display();
    MyStack.dequeue();
    MyStack.dequeue();
    MyStack.dequeue();
    MyStack.dequeue();
    MyStack.dequeue();
    MyStack.display();
    MyStack.dequeue();
    MyStack.dequeue();
    MyStack.dequeue();
    MyStack.display();

    return 0;
}