#include <stdio.h>
#include <stdlib.h>

#define MOD 1000000007

int cmp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int numFactoredBinaryTrees(int* arr, int arrSize) {
    qsort(arr, arrSize, sizeof(int), cmp);

    long long dp[arrSize];
    for (int i = 0; i < arrSize; i++) {
        dp[i] = 1;  // each number alone is one tree
    }

    for (int i = 0; i < arrSize; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[i] % arr[j] == 0) {
                int right = arr[i] / arr[j];

                // binary search for right factor
                int left = 0, r = arrSize - 1;
                while (left <= r) {
                    int mid = (left + r) / 2;
                    if (arr[mid] == right) {
                        dp[i] = (dp[i] + dp[j] * dp[mid]) % MOD;
                        break;
                    } else if (arr[mid] < right) {
                        left = mid + 1;
                    } else {
                        r = mid - 1;
                    }
                }
            }
        }
    }

    long long result = 0;
    for (int i = 0; i < arrSize; i++) {
        result = (result + dp[i]) % MOD;
    }

    return (int)result;
}
