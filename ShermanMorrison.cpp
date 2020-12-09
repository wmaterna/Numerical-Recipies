#include<iostream>
#include<iomanip>
#include<math.h>
#define SIZE_OF_MATRIX 7
using namespace std;

void cholesky_decomp(double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX],double* x,double* b);
void print(double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX],double x[7], double b[7]);
void shermanMorrisson(double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX],  double* x, double*b,double uv[SIZE_OF_MATRIX][SIZE_OF_MATRIX]);
void creat_matrix(double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX]);


void print(double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX],double x[SIZE_OF_MATRIX],
double b[SIZE_OF_MATRIX]){
	cout<<"Matrix to compute:";
	for(int i=0;i<SIZE_OF_MATRIX;i++){
	cout<<endl;
		for(int j=0;j<SIZE_OF_MATRIX;j++)
			cout<<tab[i][j];

	}
cout<<endl;
}

void cholesky_decomp(double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX],double* x,double* b){
double lower[SIZE_OF_MATRIX][SIZE_OF_MATRIX]={0};
lower[0][0]=sqrt((tab[0][0]));
for(int i=1;i<SIZE_OF_MATRIX;i++){
lower[i][i-1]=tab[i][i-1]/lower[i-1][i-1];
lower[i][i]=sqrt((tab[i][i]-lower[i][i-1]*lower[i][i-1]));
}
double y[SIZE_OF_MATRIX]={0};

y[0]=b[0]/lower[0][0];
for(int i=1;i<SIZE_OF_MATRIX;i++)
y[i]=(b[i]-y[i-1]*lower[i][i-1])/lower[i][i];

x[SIZE_OF_MATRIX-1]=y[SIZE_OF_MATRIX-1]/lower[SIZE_OF_MATRIX-1][SIZE_OF_MATRIX-1];
for(int i=SIZE_OF_MATRIX-2;i>=0;i--)
x[i]=(y[i]-lower[i+1][i]*x[i+1])/lower[i][i];



}
void shermanMorrisson(double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX], double* x, double*
b, double uv[SIZE_OF_MATRIX][SIZE_OF_MATRIX]){

double z[SIZE_OF_MATRIX]={0};
cholesky_decomp(tab,z,b);

double q[SIZE_OF_MATRIX]={0};
cholesky_decomp(tab,q,uv[0]);

long double tmp=(z[0]+z[6])/(1+q[0]+q[6]);
for(int i=0;i<SIZE_OF_MATRIX;i++){
x[i]=z[i]-tmp*q[i];
}
tab[0][0]=4;
tab[6][6]=4;
tab[0][6]=1;
tab[6][0]=1;
print(tab,x,b);
}

void creat_matrix(double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX]){
	for(int i=0;i<SIZE_OF_MATRIX;i++){
	tab[i][i]=4;
	if(i==0){
	tab[i][i+1]=1;
	tab[i][i]=3;
	}
	if(i==6){
	tab[i][i-1]=1;
	tab[i][i]=3;
	}
	else{
	tab[i][i-1]=1;
	tab[i][i+1]=1;
	}
	}}

		
int main(int argc, char const *argv[])
{
double tab[SIZE_OF_MATRIX][SIZE_OF_MATRIX]={0};
double x[SIZE_OF_MATRIX]={0};
double b[SIZE_OF_MATRIX]={0};
double uv[SIZE_OF_MATRIX][SIZE_OF_MATRIX]={0};
	creat_matrix(tab);
for(int i=0;i<SIZE_OF_MATRIX;i++){
	if(i==0)
	{
		uv[0][0]=1;
		uv[0][6]=1;
	}
else if(i==6)
uv[6][0]=1;
uv[6][6]=1;
b[i]=i+1;
}

shermanMorrisson(tab,x,b,uv);

cout<<"Solution vector"<<endl;

for(int i=0;i<SIZE_OF_MATRIX;i++)
	cout<<x[i]<<" ";

return 0;
	
}
