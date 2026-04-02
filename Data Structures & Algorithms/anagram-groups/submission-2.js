class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const myMap = new Map();


        for (let s of strs){
            let key = s.split('').sort().join('');

            if (!myMap.has(key)){
                myMap.set(key, []);

            }
            myMap.get(key).push(s);
            
        
        }

        return [...myMap.values()]









    }
}
