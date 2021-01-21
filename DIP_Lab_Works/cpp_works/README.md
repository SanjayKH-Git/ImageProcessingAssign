**3. Write a c++ program to perform operator Overloading.**
```cpp
#include <iostream>
using namespace std;
class Complex
{
    private:
        int real,img;       
    public:
        Complex(int r=0, int i=0)
        {
            real=r;
            img=i;
        }
    Complex operator + (Complex const &obj)
    {
        Complex res;
        res.real=real+obj.real;
        res.img=img+obj.img;
        return res;
    }
    
    Complex operator - (Complex const &obj)
    {
        Complex res;
        res.real=real - obj.real;
        res.img=img - obj.img;
        return res;
    }
    
    Complex operator * (Complex const &obj)
    {
        Complex res;
        res.real=real *obj.real;
        res.img=img * obj.img;
        return res;
    }
    void print()
    {
        cout<<real<<" + i"<<img<<endl;
    }
};

int main()
{
    Complex c1(10,5), c2(2,4);
    Complex add = c1 + c2;
    cout<<"Addition = ";
    add.print();
    Complex sub = c1 - c2;
    cout<<"Subtraction = ";
    sub.print();
    Complex mul = c1 * c2;
    cout<<"Multiplication = ";
    mul.print();
}
```
*output:*
```
Addition = 12 + i9
Subtraction = 8 + i1
Multiplication = 20 + i20
```
