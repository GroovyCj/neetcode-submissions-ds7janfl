class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const ana = {};
        for (let s of strs){
            const sortedS = s.split('').sort().join('');
            if(!ana[sortedS]){
                ana[sortedS] = [];
            }
            ana[sortedS].push(s);




        }
        return Object.values(ana);





    }
}
