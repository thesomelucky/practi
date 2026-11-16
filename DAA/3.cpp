#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Item {
    int id;
    double profit;
    double weight;
};

bool cmp(const Item& a, const Item& b) {
    return a.profit / a.weight > b.profit / b.weight;
}

int main() {
    int n;
    cout << "Enter the number of items: ";
    cin >> n;

    if (!cin || n <= 0) {
        cout << "Number of items must be positive.\n";
        return 1;
    }

    vector<Item> items(n);

    cout << "Enter profit and weights for items: " << endl;
    for (int i = 0; i < n; i++) {
        items[i].id = i + 1;
        double p, w;
        cin >> p >> w;

        if (!cin || p < 0 || w <= 0) {
            cout << "Profit must be non-negative and weight must be positive.\n";
            return 1;
        }

        items[i].profit = p;
        items[i].weight = w;
    }

    double capacity;
    cout << "Enter the weight of knapsack: ";
    cin >> capacity;

    if (!cin || capacity < 0) {
        cout << "Knapsack capacity cannot be negative.\n";
        return 1;
    }

    sort(items.begin(), items.end(), cmp);

   double total = 0;
   for (const Item& item : items) {
       if (capacity >= item.weight) {
           capacity -= item.weight;
           total += item.profit;
           cout << "Item " << item.id << " taken fully.\n";
       } else {
           double fraction = capacity / item.weight;
           total += item.profit * fraction;
           cout << "Item " << item.id << " taken fractionally ("
                << fraction << ").\n";
           break;
       }
   }

   cout << "Maximum profit = " << total << endl;

   return 0;
}
