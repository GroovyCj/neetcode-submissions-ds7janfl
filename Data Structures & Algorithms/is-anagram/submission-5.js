class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {

        const sortedS = new Map();
        const sortedT = new Map();

        for(let char of s){
            if(sortedS.has(char)){
             sortedS.set(char, sortedS.get(char) + 1 )
            }
            else{
                sortedS.set(char, 1)
            }
       
        }
        for(let char of t){
                   if(sortedT.has(char)){
                sortedT.set(char, sortedT.get(char) + 1 )
            }
            else{sortedT.set(char, 1)}
        }

        if (sortedS.size !== sortedT.size){
            return false
        }
        for (const [char, count] of sortedS){
            if(sortedT.get(char) !== count) return false;
        }
        return true









    }
}
