class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
         s = s.trim().toLowerCase().replace(/[^a-zA-Z0-9]/g, '')
        let left = 0, right = (s.length - 1);
        while(left < right){
            if(s[left] !== s[right]){
                return false;
            }
            else {
                left +=1;
                right -=1;
            }
            

           

            
        }
        return true;
    }
}
