package Sorting;
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class mergeSort {

// Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    //So arr[k](start from left) add by comparison of arr1[i] &arr2[j]
public static void merge(int arr[], int left, int mid, int right)
    {
        // Find sizes of two subarrays to be merged
        int len1 = mid - left + 1;
        int len2 = right - mid;
        int[] arr1 = new int[len1];
        int[] arr2= new int[len2];
        for(int i=0;i<len1;i++) arr1[i]=arr[left+i];
        for(int i=0;i<len2;i++) arr2[i]=arr[mid+1+i];
        int i=0,j=0;//index for both sub array
        int k = left;
        while(i<len1&&j<len2){
            if(arr1[i] < arr2[j]){
                arr[k] = arr1[i];
                i++;
            }else{
                arr[k] = arr2[j];
                j++;
            }
            k++;
        }
        while(i<len1) arr[k++] = arr1[i++];
        while(j<len2) arr[k++] = arr1[j++];
    }
 
    // Main function that sorts arr[l..r] using
    // merge()
public static void sort(int[] arr, int left, int right)
    {
       if (left < right){
           int mid = left + (right-left)/2;
           sort(arr,left,mid);
           sort(arr,mid+1,right);
           merge(arr,left,mid,right);
       }
    }
 
    /* A utility function to print array of size n */
    static void printArray(int[] arr)
    {
        int n = arr.length;
        System.out.print("[");
        for (int i=0; i<n-1; ++i)
            System.out.print(arr[i] + ",");
        System.out.print(arr[n-1]+"]");
    }
 
    // Driver method
    public static void main(String args[])
    {
       Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr= new int[n];    
        for(int i=0;i<n;i++) arr[i]=sc.nextInt();

        sort(arr, 0, arr.length-1);      
        printArray(arr);
        
    }
    

}