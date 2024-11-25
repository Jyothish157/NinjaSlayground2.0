public class calculateGCD {
    public static int calcGCD(int n, int m){
        // Write your code here.
       if(n < 0 || m < 0){
           throw new IllegalArgumentException("Input values must be non-negative");
       }
       while(m!=0){
           int temp = m;
           m = n % m;
           n = temp;
       }
       return n;
    }
}
