'''
  Implement C++ program for expression conversion as infix to postfix and its evaluation 
using stack based on given conditions: 
1. Operands and operator, both must be single character.
2. Input Postfix expression must be in a desired format.
3. Only '+', '-', '*' and '/ ' operators are expected.

  '''
for(int i = 0; i < expression.length(); i++) {

    if(expression[i] == ' ' || expression[i] == ',') continue;

    else if(isOperator(expression[i])) {

        int operand2 = S.top(); S.pop();
        int operand1 = S.top(); S.pop();

        int result = performOperation(expression[i], operand1, operand2);

        S.push(result);
    }
    else if(isdigit(expression[i])){

        int operand = 0;
        while(i<expression.length() && isdigit(expression[i])) {

            operand = (operand*10) + (expression[i]-'0');
            i++;
        }

        i--;
        S.push(operand);
    }
}

return S.top();

 // If operand, add to postfix
    if(isdigit(expression[i])) {
        postfix += expression[i];
    }

    else if(expression[i] == ' ' || expression[i] == ',') {
        continue;
    }

    else if(isOperator(expression[i])) {
        while(!S.empty() && S.top()!= '(' && hasHigherPrecedence(S.top(),expression[i])) {
            postfix+= S.top();
            S.pop();
        }

        S.push(expression[i]);
    }

    else if(expression[i] == '(') {
        S.push(expression[i]);
    }

    else if(expression[i] == ')') {
        while(!S.empty() && S.top() !=  '(') {
            postfix+= S.top();
            S.pop();
        }
        S.pop();
    }
}

while(!S.empty()) {
    postfix += S.top();
    S.pop();
}

return postfix;
