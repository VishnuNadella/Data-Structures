#include <iostream>
#include <vector>

using namespace std;

class Stack
{
    int top = -1;
    int stack_size;
    int stack[];

public:
    void create(int size)
    {
        stack_size = size;
        for (int i = 0; i < stack_size; i++)
        {
            stack[i] = 0; // initialize each element to 0
        }
    }

    int isFull()
    {
        if (top == stack_size - 1)
        {
            return 1;
        }
        return 0;
    }

    int isEmpty()
    {
        if (top == -1)
        {
            return 1;
        }
        return 0;
    }

    void push()
    {
        if (isFull())
        {
            cout << "-------------Stack is full-------------" << endl;
        }
        else
        {
            int push_val;
            cout << "Enter value: ";
            cin >> push_val;
            top += 1;
            stack[top] = push_val;
        }
    }

    void pop()
    {
        if (isEmpty())
        {
            cout << "-------------Stack is empty-------------" << endl;
        }
        else if (top != -1)
        {
            stack[top] = 0;
            top -= 1;
        }
    }

    void display()
    {
        if (top == -1)
        {
            cout << "-------------Cannot print from an empty stack-------------" << endl;
        }
        else
        {
            cout << "-------------Stack as follows-------------" << endl;

            for (int i = 0; i < top + 1; i++)
            {
                cout << stack[i] << " ";
            }
            cout << endl;
        }
    }
};

int main()
{
    Stack MyStack;
    MyStack.create(10);
    MyStack.push();
    MyStack.push();
    MyStack.push();
    MyStack.push();
    MyStack.display();
    MyStack.push();
    MyStack.push();
    MyStack.push();
    MyStack.push();
    MyStack.push();
    MyStack.display();
    MyStack.push();
    MyStack.push();
    MyStack.display();
    MyStack.pop();
    MyStack.pop();
    MyStack.pop();
    MyStack.pop();
    MyStack.pop();
    MyStack.display();
    MyStack.pop();
    MyStack.pop();
    MyStack.pop();
    MyStack.pop();
    MyStack.pop();
    MyStack.pop();
    MyStack.pop();
    MyStack.pop();

    return 0;
}