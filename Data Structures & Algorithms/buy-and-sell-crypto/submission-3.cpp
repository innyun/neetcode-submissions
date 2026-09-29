class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int a = 0;
        int b = 0;

        int maxProfit = 0;

        while (b < prices.size()) {
            int profit = prices[b] - prices[a];
            if (profit > maxProfit) {
                maxProfit = profit;
            } else if (profit < 0) {
                a = b;
            }
            b++;
        }

        return maxProfit;
    }
};
