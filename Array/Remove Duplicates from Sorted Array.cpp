class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        int indx = 0;
        int curr = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != curr) {
                curr = nums[i];
                nums[indx + 1] = nums[i];
                indx++;
            }
        }
        
        return indx + 1; // Return the count of unique elements
    }
};
