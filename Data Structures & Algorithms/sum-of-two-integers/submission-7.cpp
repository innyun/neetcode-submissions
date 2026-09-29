class Solution {
public:
    int getSum(int a, int b) {
        int carry = 0;
        int c = 0;
        int bit, bitA, bitB;
        for (int i = 0; i < 32; i++) {
            bitA = (a >> i) & 1;
            bitB = (b >> i) & 1;
            bit = bitA ^ bitB ^ carry;
            c = (bit << i) | c;
            carry = bitA & bitB | ((bitA | bitB) & carry);
        }
        return c;
    }
};
