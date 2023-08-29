'''
  Write program to implement a priority queue in C++ using an inorder list to store the 
items in the queue. Create a class that includes the data items (which should be 
template) and the priority (which should be int). The inorder list should contain these 
objects, with operator <= overloaded so that the items with highest priority appear at the 
beginning of the list (which will make it relatively easy to retrieve the highest item.)

  '''

#include <iostream>
#include <list>

template <typename T>
class PriorityQueue {
private:
    class Node {
    public:
        T data;
        int priority;

        Node(const T& data, int priority) : data(data), priority(priority) {}
    };

    std::list<Node> queue;

public:
    void enqueue(const T& item, int priority) {
        if (queue.empty()) {
            queue.emplace_front(item, priority);
        }
        else {
            auto it = queue.begin();
            while (it != queue.end() && priority <= it->priority) {
                ++it;
            }
            queue.insert(it, Node(item, priority));
        }
    }

    T dequeue() {
        if (queue.empty()) {
            throw std::runtime_error("Queue is empty");
        }

        T item = queue.front().data;
        queue.pop_front();

        return item;
    }

    bool isEmpty() {
        return queue.empty();
    }
};

int main() {
    PriorityQueue<int> pq;

    pq.enqueue(5, 2);
    pq.enqueue(10, 1);
    pq.enqueue(7, 3);
    pq.enqueue(3, 4);

    while (!pq.isEmpty()) {
        std::cout << pq.dequeue() << " ";
    }

    return 0;
}
