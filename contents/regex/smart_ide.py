import re
# import sys

code = ""
"""
for line in sys.stdin:
    code += "\n" + line"""

codes = ["""
class Node:
	
	def __init__(self,data=None,next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return "Node[Data=" + `self.data` + "]"
""",
"""
import java.io.*;

public class SquareNum {

   public static void main(String args[]) throws IOException
   {
      System.out.println("This is a small Java Program!");
   }
}
""",
"""
#include<stdio.h>
#include<assert.h>
/* maxVertices represents maximum number of vertices that can be present in the graph. */
#define maxVertices   100
void Dfs(int graph[][maxVertices], int *size, int presentVertex,int *visited)
{
        printf("Now visiting vertex %d\n",presentVertex);
        visited[presentVertex] = 1;
        /* Iterate through all the vertices connected to the presentVertex and perform dfs on those
           vertices if they are not visited before */
        int iter;
        for(iter=0;iter<size[presentVertex];iter++)
        {
                if(!visited[graph[presentVertex][iter]])
                {
                        Dfs(graph,size,graph[presentVertex][iter],visited);
                }
        }
        return;
        

}
""",
"""
print f"Hello world{}"
""",
"""
import java.io.*;
class ShellSort
{
void ShellSort(int array[], int number_of_elements)
{
        int iter, jter, increment, temp,i,j;
        for(increment = number_of_elements/2;increment > 0; increment /= 2)
        {
                for(i = increment; i<number_of_elements; i++)
                {
                        temp = array[i];
                        for(j = i; j >= increment ;j-=increment)
                        {
                                if(temp < array[j-increment])
                                {
                                        array[j] = array[j-increment];
                                }
                                else
                                {
                                        break;
                                }
                        }
                        array[j] = temp;
                }
        }
}
int main()throws IOException
{
    BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
        int number_of_elements;
        System.out.println("Enter the number of elements");
        number_of_elements=Integer.parseInt(in.readLine());
        int array[]=new int[number_of_elements];
        int iter;
         System.out.println("Enter the elements one by one");
        for(iter = 0;iter < number_of_elements;iter++)
        {
                array[iter]=Integer.parseInt(in.readLine());;
        }
        /* Calling this functions sorts the array */
        ShellSort(array,number_of_elements);
        for(iter = 0;iter < number_of_elements;iter++)
        {
               System.out.print(array[iter]+"\t");
        }
        System.out.print("\n");
        return 0;
}
}
""",
"""
#include<stdio.h>
#include<limits.h>
#include<assert.h>
#define maxVertices 100
#define  infinity 1000010000
/*Declaring heap globally so that we do not need to pass it as an argument every time*/
/* Heap used here is Min Heap */
typedef struct Node
{
        int vertex,distance;
}Node;
Node heap[1000000];
int seen[maxVertices];
int heapSize;
/*Initialize Heap*/
void Init()
{
        heapSize = 0;
        heap[0].distance = -INT_MAX;
        heap[0].vertex  = -1;
}
/*Insert an element into the heap */
void Insert(Node element)
{
        heapSize++;
        heap[heapSize] = element; /*Insert in the last place*/
        /*Adjust its position*/
        int now = heapSize;
        while(heap[now/2].distance > element.distance)
        {
                heap[now] = heap[now/2];
                now /= 2;
        }
        heap[now] = element;
}
Node DeleteMin()
{
        /* heap[1] is the minimum element. So we remove heap[1]. Size of the heap is decreased.
           Now heap[1] has to be filled. We put the last element in its place and see if it fits.
           If it does not fit, take minimum element among both its children and replaces parent with it.
           Again See if the last element fits in that place.*/
        Node minElement,lastElement;
        int child,now;
        minElement = heap[1];
        lastElement = heap[heapSize--];
        /* now refers to the index at which we are now */
        for(now = 1; now*2 <= heapSize ;now = child)
        {
                /* child is the index of the element which is minimum among both the children */
                /* Indexes of children are i*2 and i*2 + 1*/
                child = now*2;
                /*child!=heapSize beacuse heap[heapSize+1] does not exist, which means it has only one
                  child */
                if(child != heapSize && heap[child+1].distance < heap[child].distance )
                {
                        child++;
                }
                /* To check if the last element fits ot not it suffices to check if the last element
                   is less than the minimum element among both the children*/
                if(lastElement.distance > heap[child].distance)
                {
                        heap[now] = heap[child];
                }
                else /* It fits there */
                {
                        break;
                }
        }
        heap[now] = lastElement;
        return minElement;
}
int main()
{
        int graph[maxVertices][maxVertices],size[maxVertices]={0},distance[maxVertices]={0},cost[maxVertices][maxVertices];
        int vertices,edges,weight;
        int iter;
        /* vertices represent number of vertices and edges represent number of edges in the graph. */
        scanf("%d%d",&vertices,&edges);
        int from,to;
        for(iter=0;iter<edges;iter++)
        {
                scanf("%d%d%d",&from,&to,&weight);
                assert(from>=0 && from<vertices);
                assert(to>=0 && to<vertices);
                graph[from][size[from]] = to;
                cost[from][size[from]] = weight;
                size[from]++;
        }
        int source;
        scanf("%d",&source);
        Node temp;
        for(iter=0;iter<vertices;iter++)
        {
                if(iter==source)
                {
                        temp.distance = 0;
                        distance[0]=0;
                }
                else
                {
                        temp.distance = infinity;
                        distance[iter]= infinity;
                }
                temp.vertex = iter;
                Insert(temp);
        }
        while(heapSize)
        {
                Node min = DeleteMin();
                int presentVertex = min.vertex;
                if(seen[presentVertex])
                {
                        /* This has already been processed */
                        continue;
                }
                seen[presentVertex] = 1;
                for(iter=0;iter<size[presentVertex];iter++)
                {
                        int to = graph[presentVertex][iter];
                        if(distance[to] > distance[presentVertex] + cost[presentVertex][iter])
                        {
                                distance[to] = distance[presentVertex] + cost[presentVertex][iter];
                                /* Instead of updating it in the queue, insert it again. This works because the updated
                                   distance is less than previous distance which makes it to pop out of the queue early */
                                temp.vertex = to;
                                temp.distance = distance[to];
                                Insert(temp);
                        }
                }
        }
        for(iter=0;iter<vertices;iter++)
        {
                printf("vertex is %d, its distance is %d\n",iter,distance[iter]);
        }


        return 0;



}
""",
"""
import java.io.*;
/* Logic: This is divide and conquer algorithm. This works as follows.
         (1) Divide the input which we have to sort into two parts in the middle. Call it the left part
              and right part.
             Example: Say the input is  -10 32 45 -78 91 1 0 -16 then the left part will be
             -10 32 45 -78 and the right part will be  91 1 0 6.
         (2) Sort Each of them seperately. Note that here sort does not mean to sort it using some other
              method. We already wrote fucntion to sort it. Use the same.
         (3) Then merge the two sorted parts.
*/
/*This function Sorts the array in the range [left,right].That is from index left to index right inclusive
 */
class MeregeSort
{
void MergeSort(int array[], int left, int right)
{
        int mid = (left+right)/2;
        /* We have to sort only when left<right because when left=right it is anyhow sorted*/
        if(left<right)
        {
                /* Sort the left part */
                MergeSort(array,left,mid);
                /* Sort the right part */
                MergeSort(array,mid+1,right);
                /* Merge the two sorted parts */
                Merge(array,left,mid,right);
        }
}
/* Merge functions merges the two sorted parts. Sorted parts will be from [left, mid] and [mid+1, right].
 */
void Merge(int array[], int left, int mid, int right)
{
        /*We need a Temporary array to store the new sorted part*/
        int tempArray[]=new int[right-left+1];
        int pos=0,lpos = left,rpos = mid + 1;
        while(lpos <= mid && rpos <= right)
        {
                if(array[lpos] < array[rpos])
                {
                        tempArray[pos++] = array[lpos++];
                }
                else
                {
                        tempArray[pos++] = array[rpos++];
                }
        }
        while(lpos <= mid)  tempArray[pos++] = array[lpos++];
        while(rpos <= right)tempArray[pos++] = array[rpos++];
        int iter;
        /* Copy back the sorted array to the original array */
        for(iter = 0;iter < pos; iter++)
        {
                array[iter+left] = tempArray[iter];
        }
        return;
}
int main()throws IOException
{
    BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
        int number_of_elements;
        System.out.println("Enter the number of elements");
        number_of_elements=Integer.parseInt(in.readLine());
        int array[]=new int[number_of_elements];
        int iter;
        System.out.println("Enter the elements one by one");
        for(iter = 0;iter < number_of_elements;iter++)
        {
                array[iter]=Integer.parseInt(in.readLine());
        }
        /* Calling this functions sorts the array */
        MergeSort(array,0,number_of_elements-1);
        for(iter = 0;iter < number_of_elements;iter++)
        {
                System.out.print(array[iter]+"\t");
        }
        System.out.print("\n");
        return 0;
}
}
"""]

patterns = {
        "Python": r'(\bclass\ [A-Z]\w*:)|(\b\t*def\ [_a-zA-Z][_a-zA-Z]+\(.*\):)|([\t\ ]*\#\ +[\w\d:\.,\ ]*?[\r\n])|(print[\( ][\w\d\ "\':.,(){}]*[\) ]*[\r\n]*)',
        "C": r'(#include<[a-z]+\.h>)|(\b[a-z]*\ [a-zA-Z]*\([a-zA-Z0-9\ \*,_]*\)[\r\n\ ]*{)|(scanf\(.*\);)|(\/\*.*\*\/\b)', #|(\b\ *\w* [\w,\ +=<>\/*\[\]]*;)',
        "Java": r'(import[\ \w\.]*\**;)|(\b[ivpc][\ a-zA-Z]*\(*[\ a-zA-Z\[\]\,_]*\)*\ *[\w\ ]*[\r\n\ ]*{)|([a-zA-Z0-9]*\.[a-zA-Z0-9\.]*\([\w\.\:\ \"\'!?+,]*\);)'
    }

for code in codes:
    likelihood = [0, ""]
    for lang, pattern in patterns.items():
        score = 0
        for matches in re.findall(pattern, code):
            score += len([x for x in matches if x.strip() != ""])
        if likelihood[0] < score:
            likelihood = [score, lang]
    print(likelihood[1])
