#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    ifstream fin("chvatal.in");
    ofstream fout("chvatal.out");
    int n;
    fin >> n;
    vector<vector<bool>> matrix(n);
    for (int i = 0; i < n; ++i) {
        matrix[i].resize(n, false);
    }
    for (int j = 1; j < n; ++j) {
        for (int k = 0; k < j; ++k) {
            char c;
            fin >> c;
            matrix[j][k] = c == '1';
            matrix[k][j] = matrix[j][k];
        }
    }
    vector<int> queueList(n * n + 1);
    for (int i = 0; i < n; ++i) {
        queueList[i] = i;
    }
    int start = 0;
    for (int i = 0; i < n * (n - 1); ++i) {
        int ver0 = queueList[start];
        int ver1 = queueList[start + 1];
        if (!matrix[ver0][ver1]) {
            int index = 2;
            while (index < n - 1 && (!matrix[ver0][queueList[start + index]] || !matrix[ver1][queueList[start + index + 1]])) {
                ++index;
            }
            if (index == n - 1) {
                index = 2;
                while (!matrix[ver0][queueList[start + index]]) {
                    ++index;
                }
            }
            for (int j = 0; j < index / 2; ++j) {
                swap(queueList[start + j + 1], queueList[start + index - j]);
            }
        }
        queueList[start + n] = queueList[start];
        ++start;
    }

    for (int i = start; i < n + start; ++i) {
        fout << queueList[i] + 1 << ' ';
    }
}