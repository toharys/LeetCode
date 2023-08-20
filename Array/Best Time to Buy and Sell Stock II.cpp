class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size()==1){ // edge case
            return 0;
        }
        int max_profit=0;
        int i=0;
        while(i<prices.size()){
        int j=i;
        for(;i<(prices.size()-1) && prices[i]<prices[i+1];i++);
        max_profit+=(prices[i]-prices[j]);
        i++;
        }
        return max_profit;
        }
};
