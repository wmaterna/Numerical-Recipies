
#include<iostream>
#include<math.h>
#include<vector>
#include<iomanip>
#define Euler 2.71828182845904523536
#define PI 3.141592653589
#define Precision -7
#define Iterations 100

using namespace std;

double area(double,double,int);
double f(double);

double f(double x){
	double temp;
	temp=sin(PI*(1+sqrt(x))/(1+pow(x,2)))*pow(Euler,-x);
	return temp;
}

double area(double low,double high, int k){
	double N=pow(2,k);
	double area=0;
	double h=(high-low)/N;
	for(double i=low; i<=high; i=i+h){
		if(i==low){
			if(i==high){
			area+=f(i)/2;
			}}
		else area=area+f(i);
	}
	double tmp=area*h;
return tmp;
}



int main(int argc, char const *argv[])
{
double tolerance=pow(10,Precision);
int i=-1;
while(1){
		if(pow(Euler,i) < tolerance){
			break;}
		i--;
	}
i=-i;
cout<<"Integrate upper limit: "<<i<<endl;
double upper=i;
double lower=0;
vector<double> rombergs;
vector<double> old_romberg;
cout<<std::fixed<<setprecision(-Precision);
rombergs.push_back(area(lower, upper, 0));
int tempK;
double temp;
int k;
for(k=1; k<Iterations-1; k++){
	old_romberg=rombergs;
	rombergs.clear();
	cout<<"Number of iteration:"<<k<<endl;
	tempK=k;
		for(int n=0; n<=k; n++){
			if(n==0){
				rombergs.push_back(area(lower,upper,k));
				cout<<rombergs[0]<<" ";
				tempK--;
			}
else{
temp=(pow(4,n)*rombergs[n-1]-old_romberg[n-1])/(pow(4,n)-1);
cout<<temp<<" ";
rombergs.push_back(temp);
tempK--;
}
}
cout<<endl;
if(abs(rombergs[k]-old_romberg[k-1]) < tolerance){
	int ltmp=round(lower);
	int utmp=round(upper);
	cout<<endl<<endl;
	cout<<"Solution on ["<<ltmp<<","<<utmp<<"]:"<<rombergs[k];
	break;
}
}
double result=rombergs[k];
cout<<endl;
cout<<"Solution of given integer: "<<result<<endl;
return 0;
}


