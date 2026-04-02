class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const arrset = new Set();

         for (const item of nums) {
            if (arrset.has(item)){
                return true;
            }
            else {
                 arrset.add(item);

            };

    };
      return false;
    }
}
