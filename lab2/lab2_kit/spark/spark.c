// shell cmd: c++ spark.c -o spark; ./spark

#include <stdio.h>
#include <stdlib.h>   // exit()
#include <time.h>

#define N (1 << 20)
#define ARRAY_MIN (1 << 13)
#define ARRAY_MAX N

#define LOGFILE "spark.out"

typedef char data_cell;




double diff(timespec start, timespec end)
{
	double sec;
        double nsec;
	if ((end.tv_nsec-start.tv_nsec)<0) {
		sec = (double) end.tv_sec-start.tv_sec-1;
		nsec =(double)  1000000000+end.tv_nsec-start.tv_nsec;
	} else {
		sec =(double)  end.tv_sec-start.tv_sec;
		nsec =(double)  end.tv_nsec-start.tv_nsec;
	}
	return sec * 1000000000 + nsec;
}





int main(){

  /************************************/

  data_cell A[N];

  register int array_size;
  register int stride;
  register int limit;
  register int repeat;
  register int index;
  register int line;
  int counter;
  float avgMISSES;
  float avgTIME;
  FILE* logfile;

  /************************************/

  int retval;
  long long values[2];
  long long start_cycles, end_cycles;
  timespec start_usec, end_usec;

  logfile = fopen(LOGFILE,"w");

  for (long long i = 0; i < N; i++)
    A[i] = 0;

  for(array_size = ARRAY_MIN; array_size <= ARRAY_MAX; array_size=array_size*2)
    for(stride=1; stride <= array_size / 2; stride = 2 * stride){ 
      limit=array_size-stride+1;
 
 
      /* Gets the starting time in clock cycles */
      start_cycles = clock();
 
      /* Gets the starting time in microseconds */
      clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &start_usec);

      /************************************/

      for(repeat = 0; repeat <= 200 * stride; repeat++)
        for(index = 0; index < limit; index += stride)
          A[index] = A[index] + 1;
 
      /************************************/

      /* Gets the ending time in clock cycles */
      end_cycles = clock();
 
      /* Gets the ending time in microseconds */
      clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &end_usec);
      counter = 0;
      for(repeat = 0; repeat <= 200 * stride; repeat++)
        for(index = 0; index < limit; index += stride)
          counter++;
/*
     for(repeat=0,counter=0; repeat<=200*stride; repeat++)
        for(index=0; index<limit; index+=stride)
          counter++;
*/
      //avgMISSES=(float)(values[0])/counter;
     // avgTIME=(float)(end_usec - start_usec);
      //printf("array_size=%d \tSTRIDE=%d \tavgMISSES=%f \tavgTIME=%f\n", array_size,stride,avgMISSES,avgTIME); 
      //fprintf(logfile,"array_size=%d \tSTRIDE=%d \tavgMISSES=%f \tavgTIME=%f\n", array_size,stride,avgMISSES,avgTIME); 
	  
      printf("array_size= %d \tSTRIDE= %d \tnano= %lf \t numberOfAccesses= %5d \tAMAT= %lf\n", array_size,stride, diff(start_usec,end_usec), counter, (double)diff(start_usec,end_usec) / counter);
	
	  
    }
  fclose(logfile);
}


