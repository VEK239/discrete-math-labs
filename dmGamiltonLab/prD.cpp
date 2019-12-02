#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

vector<int> hamWay(vector<vector<bool>>& matrix, int n) {
    vector<int> result;
    for (int i = 0; i < n; ++i) {
        int placeToInsert = result.size();
        for (int j = 0; j < result.size(); ++j) {
            if (matrix[i][result[j]]) {
                placeToInsert = j;
                break;
            }
        }
        result.insert(result.begin() + placeToInsert, i);
    }
    return result;
}

vector<int> hamCycle(vector<vector<bool>>& matrix, int n, vector<int>& way) {
    vector<int> result;
    int wayStart = 0;
    int indexToEraseUntil = n;
    for (int k = 2; k < n; ++k) {
        if (matrix[way[k]][way[0]]) {
            indexToEraseUntil = k + 1;
        }
    }
    result.insert(result.begin(), way.begin(), way.begin() + indexToEraseUntil);
    wayStart = indexToEraseUntil;

    while (wayStart < n) {
        int deletingCount = 0;
        int placeToInsert = -1;
        for (int i = wayStart; i < way.size(); ++i) {
            bool check = false;
            for (int j = 0; j < result.size(); ++j) {
                if (matrix[way[i]][result[j]]) {
                    placeToInsert = j;
                    deletingCount = i + 1;
                    check = true;
                    break;
                }
            }
            if (check) break;
        }
        result.insert(result.begin() + placeToInsert, way.begin() + wayStart, way.begin() + deletingCount);
        wayStart += deletingCount - wayStart;
    }
    return result;
}

int main() {
    ifstream fin("guyaury.in");
    ofstream fout("guyaury.out");
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
            matrix[k][j] = c != '1';
        }
    }
    vector<int> result = hamWay(matrix, n);
    result = hamCycle(matrix, n, result);
    for (int i : result) {
        fout << i + 1 << ' ';
    }
}