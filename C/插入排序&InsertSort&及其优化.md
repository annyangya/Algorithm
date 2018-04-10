## 插入排序
对一组数进行插入排序，从第二个数开始，每个数与这个数的前一个数进行比较，如果这个数比前一个数小，则二者交换位置。

### 案例一
```c++
#ifndef InsertSort_h
#define InsertSort_h
#include<iostream>
using namespace std;

template<typename T>
void InsertSort(T arr,int n)
{
//    for(i=1;i<n;i++)//对于插入排序，第0个元素可以不用考虑，在插入排序开始，第0个元素已经有序，不需要 把它插入前面的位置，所以从第二个即索引值为1的元素开始考察
//    {
//        //寻找元素arr[i]的合适的位置
//        for(j=i;j>0;j--)//不>=0，每次把这个元素和前一个元素比较，当j=1的时候，判断能不能和0交换位置，所以最多到j=1;j=i,即从当前位置考察
//        {
//            if(arr[j]<arr[j-1])//如果当前位置的值大小小于前一位置的值的大小
//            {
//                swap(arr[j],arr[j-1]);//则把二者交换位置，j--，继续向前查看
//            }else//如果当前元素值大于前一个元素值，说明元素已经放在合适的位置，就终止该循环，考察下一个i的元素
//            {
//                break;
//            }
//        }
        //更简洁的写法
        for(int i=1;i<n;i++)
        {
            for(int j=i;j>0&&arr[j]<arr[j-1];j--)//直接在循环中比较大小，不符合则进行下一次循环，所以插入排序比选择排序快一点,但是根据测试结果来看选择排序速率更快，所以要进行插入排序的优化
            {
                swap(arr[j],arr[j-1]);
            }
        }
}

#endif /* InsertSort_h */
```
因为要将插入排序和选择排序进行比较，而两者比较的数组元素应该相同，所以要在SortTextHelper中添加数组copy的方法
```c++
//copy生成随机数组的元素，用于比较各排序方法的速率快慢
    //可以改为模版函数，该方法仅用于测试
    int* copyArray(int a[],int n)//1. 要拷贝的数组 2. 数组长度
    {
        int* arr=new int[n];//拷贝的目的数组
        copy(a,a+n,arr);//1. 数组头指针 2. 数组尾指针 3. 目的数组的头指针  copy是std中的内置函数
        return arr;
    }
```
测试：
```c++
    int n=10000;
    int* arr=SortTextHelper::generateRandomArray(n, 0, n);
    int *arr2=SortTextHelper::copyArray(arr, n);
    SortTextHelper::testSort("SelectSort", SelectionSort, arr, n);
    SortTextHelper::testSort("InsertSort", InsertSort, arr2, n);
    
    delete[] arr;
    delete[] arr2;
    return 0;
```
结果
```c++
SelectSort:0.094339s
InsertSort:0.132974s
```
1. 按理说插入排序应该比选择排序速度快一点，因为中间有终止循环的位置，但是因为选择排序中还有交换的操作，这也比较耗费时间，所以插入排序慢一点。所以接下来进行插入排序的优化
2. 可以让插入排序在内层循环中最终只交换一次

### 优化
将当前位置的元素（A）赋值一份给副本，然后让其与前一个元素（B）比较，如果当前位置比前一个元素位置小，
则前一个元素位置占据当前位置（A的位置），但是此时副本的元素先不占据前一个位置（B的位置），
而是接着与前一个位置的前一个元素（C）比较，如果A小于C，则C到B的位置，如果此时C前面没有值，
或者A与C前面的值比较A比较大，则A占据C的位置，否则A还要继续比较，知道找到合适的位置
```c++
for(int i=1;i<n;i++)
    {
        T e=arr[i];//将要考察的arr[i]的元素存在一个新的变量中
        int j;//保存元素e应该插入的位置
        for(j=i;j>0&&arr[j-1]>e;j--)//arr[j-1]>e,当前位置的元素的前一个元素仍然大于e，说明j不是e的位置
        {
            arr[j]=arr[j-1];//把前一个位置的元素放在当前位置，因为前一个位置的元素大于当前位置，
        }
        arr[j]=e;//内层循环结束后得到了e的最终位置
    }
```
结果
```c++
SelectSort:0.09393s
InsertSort:0.060231s
```
随机数组范围缩小差距更明显，现在rangeL,rangeR,为0，1
结果
```c++
SelectSort:0.089641s
InsertSort:0.050425s
```
当数组元素近乎有序时，可以看到更明显的效果。先创建生成近乎有序数组的函数
```c++
 //生成近乎于有序的数组
    int* generateNearlyOrderedArray(int n,int swaptimes)//n:数组长度，swaptimes：交换次数
    {
        //先生成完全有序的数组
        int* arr=new int[n];
        for(int i=0;i<n;i++)
        {
            arr[i]=i;
        }
        //再随机挑选几对进行交换，但是结果仍然近乎有序
        srand(time(NULL));
        for(int i=0;i<swaptimes;i++)
        {
            //随机x和y的位置（0，n）
            int pox=rand()%n;
            int poy=rand()%n;
            swap(arr[pox],arr[poy]);//交换两者的位置
        }
        return arr;
    }
```
测试
```c++
    int n=10000;
    int* arr=SortTextHelper::generateNearlyOrderedArray(n, 100);//只有200个元素没在应该的位置
    int* arr2=SortTextHelper::copyArray(arr, n);
    SortTextHelper::testSort("SelectSort", SelectionSort, arr, n);
    SortTextHelper::testSort("InsertSort", InsertSort, arr2, n);
    delete[] arr;
    delete[] arr2;
    return 0;
```
结果
```c++
SelectSort:0.10348s
InsertSort:0.001831s
```
可以看到插入排序用的时间明显比选择排序短。优化后的插入排序对于近乎有序的数组排序比很多复杂度为nlogn的排序算法还要快

