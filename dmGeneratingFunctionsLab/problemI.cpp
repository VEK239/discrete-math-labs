#include <iostream>
#include <vector>

using namespace std;

long long MOD = 104857601;

int main() {
    int k;
    long long n;
    cin >> k >> n;
    --n;
    vector<long long> elements(2 * k);
    for (int i = 0; i < k; ++i) {
        cin >> elements[i];
    }
    vector<long long> coefs(k + 1, 1);
    for (int i = 1; i <= k; ++i) {
        long long c;
        cin >> c;
        coefs[i] = (MOD - c) % MOD;
    }
    while (n >= k) {
        for (int i = k; i < 2 * k; ++i) {
            elements[i] = 0;
            for (int j = 0; j < k; ++j) {
                elements[i] = (elements[i] - coefs[j + 1] * elements[i - j - 1] % MOD + MOD) % MOD;
            }
        }
        for (int i = int(n % 2); i < 2 * k; i += 2) {
            elements[i / 2] = elements[i];
        }

        vector<long long> new_coefs(k + 1);
        for (int i = 0; i <= 2 * k; i += 2) {
            for (int j = 0; j <= i; ++j) {
                long long q_left = (j <= k ? coefs[j] : 0);
                long long q_right = (i - j <= k ? (coefs[i - j] * ((i - j) % 2 ? -1 : 1)) : 0);
                new_coefs[i / 2] = (new_coefs[i / 2] + q_left * q_right % MOD) % MOD;
            }
        }
        coefs = new_coefs;
        n /= 2;
    }
    cout << elements[n] % MOD;
}