#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, W;
    cout << "Enter number of items: ";
    cin >> n;
    if (!cin || n < 0) { cout << "Invalid number of items.\n"; return 1; }
    vector<int> p(n + 1), w(n + 1);
    cout << "Enter profit and weight of each item:\n";
    for (int i = 1; i <= n; i++) {
        cin >> p[i] >> w[i];
        if (!cin || p[i] < 0 || w[i] < 0) {
            cout << "Profit and weight must be non-negative.\n";
            return 1;
        }
    }
    cout << "Enter knapsack capacity: ";
    cin >> W;
    if (!cin || W < 0) { cout << "Invalid capacity.\n"; return 1; }

    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));
    for (int i = 1; i <= n; i++)
        for (int j = 0; j <= W; j++) {
            dp[i][j] = dp[i - 1][j];
            if (w[i] <= j) dp[i][j] = max(dp[i][j], p[i] + dp[i - 1][j - w[i]]);
        }

    cout << "DP Table:\n";
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= W; j++) cout << dp[i][j] << "\t";
        cout << "\n";
    }
    cout << "Maximum profit = " << dp[n][W] << "\n";

    cout << "Items selected: ";
    for (int i = n, j = W; i > 0; i--)
        if (dp[i][j] != dp[i - 1][j]) {
            cout << i << " ";
            j -= w[i];
        }
    cout << "\n";
    return 0;
}
