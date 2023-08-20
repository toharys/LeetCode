class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        std::vector<int> res(nums);
        int new_indx;
        for(int i=0;i<nums.size();i++){
        new_indx = (i+k)%nums.size();
        res[new_indx]=nums[i];
        }
        nums=res;
    }
};
