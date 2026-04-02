class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const dups = new Set();

        for(let n of nums){
            if(dups.has(n)){
                return true
            }
            else{
                dups.add(n)
            }
        }
        return false;





    }
}
