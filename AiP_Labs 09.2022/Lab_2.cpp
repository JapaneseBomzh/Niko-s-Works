#include <iostream>
#include <cmath>
#include <algorithm>//To sort an array (15)
#include <sstream>//To convert an array to a number (13)
long  fact(int N){if(N < 0)return 0;if (N == 0)return 1;else return N * fact(N - 1);}

float volume_cylinder(float R,float H){return M_PI*pow(R,2)*H;}//1
float higher_number(float a,float b){if(a>b){return a;} else{return b;}}//2
float comparison(float a,float b){if(a>b){std::cout <<a<<'>'<<b<< std::endl;} else if(a<b){std::cout <<a<<'<'<<b<< std::endl;}else{std::cout <<a<<'='<<b<< std::endl;}}//3
float percent_of_the_number(float a,float b){return a*0.01*b;}//4
float distance(float x1,float y1,float x2,float y2){return sqrt(pow((x1-x2),2)+pow((y1-y2),2));}//5
int table_of_factorials(int n){for(int i=1;i<n+1;i++){std::cout << fact(i) << std::endl;}}//6
void equation(double a,double b,double c){

    double x1,x2,D;
    D=pow(b,2)-4*a*c;

    if (D>0){
        x1=(-b-sqrt(D))/2*a;
        x2=(-b+sqrt(D))/2*a;

        std::cout << x1 << std::endl;
        std::cout << x2 << std::endl;
    }

    else {
        if (D == 0)
        {
            x1 = -b / (2 * a);
            std::cout << x1 << std::endl;

        }

        else
        {
            std::cout << "There are no roots" << std::endl;

        }

    }

}//7
int IsPointInSquare(int x,int y){ return (abs(x) + abs(y)) <= 1;}//8
int summ_N_number(int n){int s=0;for(int i=1 ;i<n+1;i++)s+=i;return s;}//9
float power(float x,int y){float p=1; for(int i ;i<y;i++)p*=x;return p;}//10
char pyramid(int n){int x,y;for(int i=1;i<n+1;i++){for(int j=1;j<=i;j++) { std::cout << "*"; }std::cout<< std::endl;}}//11

float line(float x1,float y1,float x2,float y2){return sqrt(pow(x1-x2,2)+pow(y1-y2,2) );}//12
float square(float a,float b,float c){float p=(a+b+c)/2;return sqrt(p*(p-a)*(p-b)*(p-c));}
float IsPointInTriangle(float x1,float y1,float x2,float y2,float x3,float y3,float x4,float y4)
{float a=line(x1,y1,x2,y2),b=line(x1,y1,x4,y4),c=line(x2,y2,x4,y4);
    float s1=square(a,b,c);
    a=line(x2,y2,x3,y3);b=line(x2,y2,x4,y4);c=line(x3,y3,x4,y4);
    float s2=square(a,b,c);
    a=line(x1,y1,x3,y3);b=line(x1,y1,x4,y4);c=line(x3,y3,x4,y4);
    float s3=square(a,b,c);
    a=line(x1,y1,x2,y2);b=line(x2,y2,x3,y3);c=line(x3,y3,x1,y1);
    int st=square(a,b,c);
    int ss=s1+s2+s3;

    return ss == st;}
int reverse_number(int n){
    std::stringstream ss;
    int counter = 0;
    int *arr = new int[n];
    while (n) {
        arr[counter] = n%10;
        n /= 10;
        counter++;
    }
    for (unsigned i = 0; i < (sizeof arr / sizeof arr [0])+counter-2; ++i)
        ss << arr [i];

    int result;
    ss >> result;
    return result;
}//13
void pros(int m) {
    for (int i = 1; i < m + 1; i++) {
        if (i == 2 or i == 3 or i == 5 or i == 7) { std::cout << i << '\t'; }

        if (i != 1 && i % 2 != 0 && i % 3 != 0 && i % 5 != 0 && i % 7 != 0) { std::cout << i << '\t'; }

    }
    std::cout <<std::endl;
}//14
int max(int x1,int x2,int x3,int x4,int x5)
{
    const int length = 5;
    int array[length] = { x1, x2, x3, x4, x5 };
    for (int startIndex = 0; startIndex < length - 1; ++startIndex)
    {
        int smallestIndex = startIndex;
        for (int currentIndex = startIndex + 1; currentIndex < length; ++currentIndex)
        {
            if (array[currentIndex] < array[smallestIndex])
                smallestIndex = currentIndex;
        }
        std::swap(array[startIndex], array[smallestIndex]);
    }
    return array[4];
}//15

bool prime(int n){
    if (n != 1 && n % 2 != 0 && n % 3 != 0 && n % 5 != 0 && n % 7 != 0) { return true;}

    if (n == 2 or n == 3 or n == 5 or n == 7) {return true; }
    else return false;}//16
void summ_prime(int n){
        int i,flag = 0;

        for (i = 1; i <= n/2; i++){
            if (prime(i) && prime(n-i)){
                flag = 1;
                break;
            }
        }
        if (flag) {
            std::cout << n << " can be represented as the sum of two primes, for example: \n";
            std::cout << n << "=" << i << "+" << n-i << '\n';
        }
        else {
            std::cout << n << " cannot be represented as the sum of two primes\n ";
        }}

int main() {
    float a,b,x1,x2,y1,y2;


    std::cout << volume_cylinder(1,3) << std::endl;//1

    std::cin >> a;std::cin >> b;//2

    std::cout <<higher_number(a,b)<< std::endl;

    comparison(a,b);//3

    std::cout <<percent_of_the_number(a,b)<< std::endl;//4

    std::cin >> x1;std::cin >> y1;std::cin >> x2;std::cin >> y2;//5
    std::cout << distance(x1,y1,x2,y2) << std::endl;

    table_of_factorials(10);//6

    equation(2,4,2);//7

    if (IsPointInSquare(1, 0)){ std::cout <<"YES"<< std::endl; }//8
    else{ std::cout <<"NO"<< std::endl; }

    std::cout <<summ_N_number(10) << std::endl;//9

    std::cout <<power(0.5,7) << std::endl;//10

    pyramid(10);//11

    if (IsPointInTriangle(2, 2,2,-2,-5,0,0,0)){ std::cout <<"YES"<< std::endl; }//12
    else{ std::cout <<"NO"<< std::endl; }
    std::cout <<  reverse_number(34545324)<< std::endl;;
    pros(100);//14

    std::cout <<max(2,4,57,2,1)<< std::endl;//15
    summ_prime(254);//16
}

