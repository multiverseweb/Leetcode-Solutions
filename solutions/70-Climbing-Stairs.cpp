#include <iostream>
class Solution {
public:
    int climbStairs(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return func(n);
        }
    }   
private:
    int func(int n) {
        int a = 1, b = 1, c;
        for (int i = 0; i < n - 1; ++i) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }
};
