class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        int idx = 0;
        while (idx < tokens.length) {
            String token = tokens[idx];
            idx += 1;
            switch (token) {
                case "+" -> {
                    Integer operand1 = stack.pop();
                    Integer operand2 = stack.pop();
                    stack.push(operand2 + operand1);
                }
                case "-" -> {
                    Integer operand1 = stack.pop();
                    Integer operand2 = stack.pop();
                    stack.push(operand2 - operand1);
                }
                case "*" -> {
                    Integer operand1 = stack.pop();
                    Integer operand2 = stack.pop();
                    stack.push(operand2 * operand1);
                }
                case "/" -> {
                    Integer operand1 = stack.pop();
                    Integer operand2 = stack.pop();
                    stack.push(operand2 / operand1);
                }
                default -> {
                    stack.push(Integer.parseInt(token));
                }
            }
        }
        return stack.pop();
    }
}
