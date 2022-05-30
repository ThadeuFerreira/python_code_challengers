#Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.



class Solution {
public:
    string removeKdigits(string num, int k) {
        std::stack<char> numStack;

        //Construct a monotone increasing sequence of digits
        for (int i = 0; i < num.length(); i++) {
            while (k > 0 && !numStack.empty() && numStack.top() > num[i]) {
                numStack.pop();
                k--;
            }
            numStack.push(num[i]);
        }

        // - Trunk the remaining K digits at the end
        //- in the case k==0: return the entire list
        std::stack<char> finalStack;
        while (k > 0) {
            finalStack.push(numStack.top());
            numStack.pop();
            k--;
        }

        //strip the leading zeros
        while (!finalStack.empty() && finalStack.top() == '0') {
            finalStack.pop();
        }

        //convert the stack to string
        std::string result;
        while (!finalStack.empty()) {
            result.push_back(finalStack.top());
            finalStack.pop();
        }
        return result;
        
    }
};