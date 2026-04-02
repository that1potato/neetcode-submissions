class MinStack {

    private Stack<Integer> minVal;
    private Stack<Integer> stack;

    public MinStack() {
        this.minVal = new Stack<>();
        this.stack = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
        if (minVal.isEmpty()) {
            minVal.push(val);
        } else {
            int min = minVal.pop();
            if (min < val) {
                minVal.push(min);
                minVal.push(min);
            } else {
                minVal.push(min);
                minVal.push(val);
            }
        }
    }
    
    public void pop() {
        if (stack.size() > 0) {
            minVal.pop();
            stack.pop();
        }
    }
    
    public int top() {
        int topVal = stack.pop();
        stack.push(topVal);
        return topVal;
    }
    
    public int getMin() {
        int min = minVal.pop();
        minVal.push(min);
        return min;
    }
}
