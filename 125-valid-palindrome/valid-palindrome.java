class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder str = new StringBuilder();

        for(char ch : s.toCharArray())
        {
            if(Character.isLetterOrDigit(ch))
            {
                str.append(ch);
            }
        }
        String original = str.toString();
        String reversed = str.reverse().toString();

        return original.equalsIgnoreCase(reversed);
    }
}