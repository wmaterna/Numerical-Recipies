//
//  main.cpp
//  Cholasky
//
//  Created by Weronika Materna on 24/11/2019.
//  Copyright © 2019 Weronika Materna. All rights reserved.
//


#include <iostream>
#include <limits>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_blas.h>
#include <gsl/gsl_linalg.h>
#include <math.h>
#define SIZE_OF_MATRIX 7

using namespace std;

void create_matrix(double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX]);
void prntl(double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX]);
void cholesky_decomp(double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX],double lower[SIZE_OF_MATRIX][SIZE_OF_MATRIX]);
void transposition(double lower[SIZE_OF_MATRIX][SIZE_OF_MATRIX], double upper [SIZE_OF_MATRIX][SIZE_OF_MATRIX]);
void solve(double lower[SIZE_OF_MATRIX][SIZE_OF_MATRIX], double b[SIZE_OF_MATRIX], double x[SIZE_OF_MATRIX],double z[SIZE_OF_MATRIX]);

int main()
{
	double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX]={0};
	double lower[SIZE_OF_MATRIX][SIZE_OF_MATRIX]={0};
	double b[SIZE_OF_MATRIX]={1,2,3,4,5,6,7};
	double x[SIZE_OF_MATRIX];
	double z[SIZE_OF_MATRIX]={0};
	create_matrix(tab);
	prntl(tab);
	cout<<endl;
	cholesky_decomp(tab, lower);
	prntl(lower);
	cout<<endl;
	solve(lower, b, x, z);

	return 0;
}
void solve(double lower[SIZE_OF_MATRIX][SIZE_OF_MATRIX], double b[SIZE_OF_MATRIX], double x[SIZE_OF_MATRIX],double z[SIZE_OF_MATRIX]){
  int i;
  double s=0;
 
 z[0]=b[0]/lower[0][0];
  for(i = 1; i < SIZE_OF_MATRIX; i++) {
        s=lower[i][i-1]*z[i-1];
	z[i]=(b[i]-s) / lower[i][i];
 }
  

	s=0;
	x[SIZE_OF_MATRIX-1] = z[SIZE_OF_MATRIX-1]/lower[SIZE_OF_MATRIX-1][SIZE_OF_MATRIX-1];
	for(i = SIZE_OF_MATRIX-2; i >=0; i--) {
		   s = lower[i+1][i]*x[i+1];
			x[i]=(z[i]-s)/lower[i][i];
 }
	cout<<endl<<"Solution vector: "<<endl;
	for (i=0; i<SIZE_OF_MATRIX; i++)
	{
		cout<<x[i]<<endl;
	}
}
void transposition(double lower[SIZE_OF_MATRIX][SIZE_OF_MATRIX], double upper [SIZE_OF_MATRIX][SIZE_OF_MATRIX])
{
	for (int i=0; i<SIZE_OF_MATRIX; i++)
	{
		for (int j=0; j<SIZE_OF_MATRIX; j++)
		{
			upper[j][i]=lower[i][j];
		}
	}
}
void create_matrix(double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX])
{
	int i=0;
while(i<7)
{
	tab[i][i-1]=1;
	tab[i][i]=4;
	tab[i][i+1]=1;
	i++;
}
}
void prntl(double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX])
{
	for (int i=0; i<SIZE_OF_MATRIX; i++)
	{
		for(int j=0; j<SIZE_OF_MATRIX; j++)
		{
			cout<<tab[i][j]<<" ";
		}
		cout<<endl;
	}
}

void cholesky_decomp(double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX],double lower[SIZE_OF_MATRIX][SIZE_OF_MATRIX])
{
	
	for (int i = 0; i < SIZE_OF_MATRIX; i++) {
		  for (int j = 0; j <= i; j++) {
			  double sum = 0;
	
			  if (j == i)
			  {
				  for (int k = 0; k < j; k++)
					  sum += pow(lower[j][k], 2);
				  lower[j][j] = sqrt(tab[j][j] -
										  sum);
			  } else {
	
				  for (int k = 0; k < j; k++)
					  sum += (lower[i][k] * lower[j][k]);
				  lower[i][j] = (tab[i][j] - sum) /
										lower[j][j];
			  }
		  }
	  }
}
 
void cholesky_decomp(double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX],double lower[SIZE_OF_MATRIX][SIZE_OF_MATRIX])
{
	lower[0][0]=sqrt((tab[0][0]));
	for (int i=1; i<SIZE_OF_MATRIX;i++)
	{
		lower[i][i-1]=tab[i][i-1]/lower[i-1][i-1];
		lower[i][i]=sqrt((tab[i][i]-lower[i][i-1]*lower[i][i-1]));
		
	}
}
