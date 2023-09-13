class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        std::sort(nums1.begin(), nums1.end());
        std::sort(nums2.begin(), nums2.end());
        
        int ind1=0, ind2=0, write_ind=0;
        while(ind1<nums1.size()&&ind2<nums2.size()){
            if(nums1[ind1]==nums2[ind2]){
                    nums1[write_ind]=nums1[ind1];
                ind1++ , ind2++, write_ind++;
                }
            else{
                if(nums1[ind1]>nums2[ind2]){
                    ind2++;
                }
                else{
                    ind1++;
                }
            }
        }
        nums1.resize(write_ind);
        return nums1;
    }
};
