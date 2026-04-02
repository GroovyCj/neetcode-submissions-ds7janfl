class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */

    // nums = [1,4,8,9] target = 12
    twoSum(nums, target) {
    const resultMap = new Map();

    for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const desiredNum = target - num;

    if (resultMap.has(desiredNum)) {
      return [resultMap.get(desiredNum), i];
    }

    resultMap.set(num, i);
  }


}


        









};

