#include <iostream>
using namespace std;

int recursiveSteps = 0;

int fib(int n) {
    recursiveSteps++;

    if (n <= 1) {
        return n;
    }

    return fib(n - 1) + fib(n - 2);
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;

    if (!cin || n < 0) {
        cout << "Please enter a non-negative integer.\n";
        return 1;
    }

    int a = 0;
    int b = 1;
    int iterativeSteps = 0;

    for (int i = 0; i < n; i++) {
        cout << a << " ";
        int next = a + b;
        a = b;
        b = next;
        iterativeSteps++;
    }

    fib(n);
    cout << "\nIterative steps: " << iterativeSteps;
    cout << "\nRecursive steps: " << recursiveSteps;

    return 0;
}
