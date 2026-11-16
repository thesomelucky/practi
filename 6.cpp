#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <string>
#include <algorithm>
using namespace std;

long long comparisons = 0;

int partition(vector<int>& a, int low, int high) {
    int pivot = a[high], i = low - 1;
    for (int j = low; j < high; j++) {
        comparisons++;
        if (a[j] <= pivot) swap(a[++i], a[j]);
    }
    swap(a[i + 1], a[high]);
    return i + 1;
}

void quickSort(vector<int>& a, int low, int high, bool randomized) {
    if (low < high) {
        if (randomized) swap(a[low + rand() % (high - low + 1)], a[high]);
        int p = partition(a, low, high);
        quickSort(a, low, p - 1, randomized);
        quickSort(a, p + 1, high, randomized);
    }
}

void run(string name, vector<int> a, bool randomized) {
    comparisons = 0;
    quickSort(a, 0, static_cast<int>(a.size()) - 1, randomized);
    cout << name;
    for (int x : a) cout << x << " ";
    cout << " | Comparisons = " << comparisons << "\n";
}

int main() {
    srand(time(0));
    int n;
    cout << "Enter number of elements: ";
    cin >> n;
    if (!cin || n < 0) { cout << "Invalid number of elements.\n"; return 1; }
    vector<int> a(n);
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) {
        if (!(cin >> a[i])) { cout << "Invalid element.\n"; return 1; }
    }
    run("Deterministic: ", a, false);
    run("Randomized   : ", a, true);
    return 0;
}
