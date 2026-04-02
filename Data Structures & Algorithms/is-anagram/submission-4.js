class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const myMap  = new Map();
        const myMap2 = new Map();
        for (let char of s){
            if (myMap.has(char)){
                myMap.set(char, myMap.get(char) + 1);

            }
            else{
                myMap.set(char, 1)
            };
          

        };
        for (let char of t){
            if (myMap2.has(char)){
                  myMap2.set(char, myMap2.get(char) + 1);

            }
            else{
                myMap2.set(char, 1)
            };



        };

        if (myMap.size !== myMap2.size) return false;

        for (const [char, count] of myMap) {
            if (myMap2.get(char) !== count) return false;

    }
    return true
}   
}
