## 选择排序算法
### 实例一
1. 将一组数从小到大进行排列
2. 外层循环从第一个数开始，内层循环从第二个数开始，将第二个数，第三个数……直到最后一个数与第一个数比较大小，如果这个数比第一个数小
就将其交换位置，当内层循环遍历结束后，已经选出最小的一个数
3. 接下来外层循环从第二个数开始，内层循环从第三个数开始，外层循环的数与内层循环的数依次比较，选出最小的
4. 循环往复，直到排列完毕
```c++
#include<iostream>
#include<algorithm>
using namespace std;
void SelectionSort(int arr[],int n)//1.数组 2，数组中元素个数
{
    for(int i=0;i<n;i++)
    {
        //寻找[i,n）区间里的最小值
        //将数组从小到大进行排序
        int minIndex=i;//存储当前最小元素的索引值
        for(int j=i+1;j<n;j++)
        {
            if(arr[j]<arr[minIndex])
            {
                minIndex=j;
            }
        }
        swap(arr[i],arr[minIndex]);//将arr[i]的值与当前遍历一次后找到的最小值进行交换
        //swap是c++标准库中内置的函数，最新标准就在std中，也可以引出来:#include<algorithm>
    }
}


//测试类
int main()
{
    int arr[10]={1,4,5,6,2,3,7,5,8,10};
    SelectionSort(arr,10);
    //将排序后的结果打印
    for(int i=0;i<10;i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}
```
上面的排序是基于整数，但是也要比较其他类型的，所以要使用模版,在每个函数的前面都添加语句：template<typename T>，并且函数参数的数组型都改为T。
 下面是测试类:
  ```c++
  int main()
{
    //整数数组
    int arr[10]={1,4,5,6,2,3,7,5,8,10};
    SelectionSort(arr,10);
    //将排序后的结果打印
    print(arr,10);
    
    //浮点数数组
    double a[10]={1.2,3.4,5.6,2,5.3,1.2,6,6,8.4,6};
    SelectionSort(a, 10);
    print(a,10);
    
    //string类
    string s[4]={"A","C","D","B"};
    SelectionSort(s, 4);
    print(s, 4);
    
    return 0;
}
```
结果：
```c++
1 2 3 4 5 5 6 7 8 10 
1.2 1.2 2 3.4 5.3 5.6 6 6 6 8.4 
A B C D 
```
### 实例二
打印输出学生成绩和学生姓名，将学生成绩按从大到小或从小到大，但是要注意的是，大于和小于都不是绝对的，而是根据用户自定义而来的。在c++中有运算符重载，用户可以自定义<,>的意义
```c++
//宏定义
#ifndef Student_hpp
#define Student_hpp

//.h文件是对外界开放的，而.cpp文件是对外界隐藏的
#include<iostream>
#include<string>
using namespace std;

struct Student{
    string name;
    int score;
    
    //运算符重载，便于比较大小
    bool operator<(const Student &otherStudent){
        //return  score<otherStudent.score;//成绩从小到大排列，如果>则是从大到小
        //如果分数相同，将姓名从小到大排列
        return score!=otherStudent.score?score<otherStudent.score:name<otherStudent.name;
    }
    
    //对<<运算符输出的重载
    //传入ostream &os即输出outputStream的引用
    friend ostream& operator<<(ostream &os,Student &student)
    {
        // <<运算符的意思就是输出下面内容
        os<<"Student:"<<student.name<<" "<<student.score<<endl;
        return os;
    }
};

#endif /* Student_hpp */
```
测试类：
```c++
//Student
    Student d[4]={{"A",98},{"C",100},{"B",97},{"D",94}};
    SelectionSort(d, 4);
    print(d, 4);
```
结果：
```c++
Student:D 94
 Student:B 97
 Student:A 98
 Student:C 100
```
### 实例三：随机生成算法测试用例
随机生成数组，来测试比较函数
```c++
//生成辅助的函数
#ifndef SortTextHelper_h
#define SortTextHelper_h

#include<iostream>
#include<ctime>
#include<cassert>
using namespace std;

//新命名的空间
namespace SortTextHelper
{
    //返回数组，所以用指针，返回数组中的第一个元素
    //生成有n个元素的随机数组，每一元素的随机范围为[rangeL,rangeR]
    int* generateRandomArray(int n,int rangeL,int rangeR){
        assert(rangeL<=rangeR);//设置rangeL<rangeR
        //创建新的数组
        int *arr=new int[n];
        //arr里面的数是随机数
        //1.设置随机种子,当前时间作为随机数的种子
        srand(time(NULL));
        for(int i=0;i<n;i++)
        {
            //生成从0到rangeR-rangeL之间的整数，+rangeL为偏移（加一个rangeL），就可以生成rangeR-rangeL之间的整数，并赋值给arr[i]
            arr[i]=rand()%(rangeR-rangeL+1)+rangeL;
        }
        return arr;
    }
}

#endif /* SortTextHelper_h */
```
测试类
```c++
    int n=10000;
    int *arr= SortTextHelper::generateRandomArray(n,0,n);
    SelectionSort(arr, n);
    print(arr, n);
    delete[] arr;//开放数组空间，所以释放数组，避免内存泄漏
    
    return 0;
```
### 实例四：测试算法性能
通过得到运行函数的时间来测试该函数的运行效率
1. 写出判断最终得到的数组是否从小到大排序，如果是则为真，否则为假
```c++
//判断数组是否排序成功,从小到大
    template<typename T>
    bool isSorted(T arr[],int n)
    {
        for(int i=0;i<n-1;i++)
        {
            if(arr[i]>arr[i+1])
            {
                return false;
            }
        }
        return true;
    }
```
2. 在SortTextHelper中写出测试算法的函数
```c++
//测试算法性能的函数，通过比较时间大小来判定函数性能
    /*
     1. sortname:排序算法的名字
     2. 传入函数本身，这里使用指针
     3. 测试用的数组
     4. 测试数组的大小
     */
    template<typename T>
    void testSort(string sortName,void(*sort)(T[],int n),T arr[],int n)
    {
        //用clock函数来测定时间
        //开始的时间
        clock_t startTime=clock();
        //通过sort对数组进行排序
        sort(arr,n);
        //结束的时间
        clock_t endTime=clock();
        //打印时间
        //endTime-startTime：时钟周期的个数
        //CLOCKS_PER_SEC:库中的宏定义，表示每一秒钟运行的时钟周期的个数
        //double(endTime-startTime)/CLOCKS_PER_SEC：该程序运行了多少秒
        assert(isSorted(arr, n));//判断有序否，不能在计算endTime之前，否则包含验证数组是否有序的时间，如果数组不是有序的，那么程序会自动中断，不会计算下面的时间
        cout<<sortName<<":"<<double(endTime-startTime)/CLOCKS_PER_SEC<<"s"<<endl;
    }
```
测试：
```c++
    int n=100000;//时间和数据增长是成平方关系
    int *arr= SortTextHelper::generateRandomArray(n,0,n);
    SortTextHelper::testSort("SelectionSort", SelectionSort, arr, n);
```
结果：
```c++
n=100000,得到结果：SelectionSort:9.10164s
n=10000,得到结果：SelectionSort:0.092s
```
所以，在时间复杂度为o(n^2)中，时间长度和数据增长长度的平方成正比，100000/10000=10，而时间增大的倍数为100倍
