// Function calling itself

// #include <iostream>
// using namespace std;
// void greet() {
//     cout<<"Hey"<<endl;
//     greet();
// }
// // infinite time print "Hey"
// int main() {
//     greet();
// }

// print n to 1
// #include <iostream>
// using namespace std;
// int value(int a){
//     if (a == 0) return 0;
//     cout<<a<<endl;
//     value(a-1);
// }
// int main() {
//     value(3);
// }

// print 1 to n by using recursion
// #include <iostream>
// using namespace std;
// int value(int a, int n){
//     if(a==n) return 0;
//     cout<<a<<endl;
//     value(a+1,n);
// }
// int main() {
//     int num;
//     cout<<"Enter the value of num: ";cin>>num;
//     value(1, num);
// }

// print sum form 1 to n (parameterised)
// #include <iostream>
// using namespace std;
// int value(int n) {
//     if(n == 0) return 0;
//     value(n-1);
//     cout<<n<<endl;
    
// }
// int main() {
//     int num;
//     cout<<"Enter the value of num: ";cin>>num;
//     value(num);
//     int add = 0;
//     add += num;
//     cout<<"Addition of the number is: "<<add;
// }

// return types

// print sum 1 to n (return type)
// #include <iostream>
// using namespace std;
// int sum(int n) {
//     if (n==1) return 1;
//     return (n + sum(n-1));
// }
// int main() {
//     int n;
//     cout<<"Enter n: ";cin>>n;
//     cout<<sum(n);
// }

// factorial of n using recursion
// #include <iostream>
// using namespace std;
// int factorial(int n) {
//     if(n==1 || n == 1) return 1;
//     return(n*factorial(n-1));
// }
// int main() {
//     int num;
//     cout<<"Enter number: ";cin>>num;
//     cout<<factorial(num);
// }

// #include <iostream>
// using namespace std;
// int power(int base, int po) {
//     if(po == 0) return 1;
//     return (base * power(base, po-1));
// }
// int main() {
//     int a,b;
//     cout<<"Enter base: ";cin>>a;
//     cout<<"Enter power: ";cin>>b;
//     cout<<power(a,b);
// }

// multiple call
// nth fibonacci series => 1 1 2 3 5 8 13 21 34 55 89 ....
// #include <iostream> 
// using namespace std;
// int fibo(int num){
//     if(num == 1 || num == 2) return 1;
//     return (fibo(num-1) + fibo(num-2));
// }
// int main() {
//     int n;
//     cout<<"Enter value of n: "; cin>>n;
//     cout<<fibo(n);
// }

