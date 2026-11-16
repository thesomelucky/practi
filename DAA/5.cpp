#include <iostream>
#include <cstdlib>
using namespace std;

int n, col[20];     // col[r] = column of the queen in row r

bool isSafe(int r, int c) {
    for (int i = 0; i < r; i++)
        if (col[i] == c || abs(col[i] - c) == abs(i - r)) return false;
    return true;
}

bool solve(int r) {
    if (r == n) return true;
    for (int c = 0; c < n; c++)
        if (isSafe(r, c)) {
            col[r] = c;
            if (solve(r + 1)) return true;     // else backtrack and try next column
        }
    return false;
}

int main() {
    int first;
    cout << "Enter number of queens: ";
    cin >> n;
    if (!cin || n < 1 || n > 20) { cout << "Enter n from 1 to 20.\n"; return 1; }
    cout << "Enter column (1 to " << n << ") of the first queen in row 1: ";
    cin >> first;
    if (!cin || first < 1 || first > n) { cout << "Invalid column.\n"; return 1; }
    col[0] = first - 1;   // first queen is already placed

    if (solve(1)) {
        cout << "Final " << n << "-Queens matrix:\n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) cout << (col[i] == j ? "1 " : "0 ");
            cout << "\n";
        }
    } else
        cout << "No solution exists with the first queen at column " << first << "\n";
    return 0;
}
