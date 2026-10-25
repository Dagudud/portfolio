#include <iostream>
#include <cmath>

using namespace std;

int polePr(int a, int b){
	return a*b;
}
int obwPr(int a, int b){
	return 2*a+2*b;
}

float poleTr(float ta, float h){
	return 0.5*ta*h;
}
float obwTr(float ta){
	return 3*ta;            // trójkąt równoboczny
}
float poleOk(float r){
	return M_PI*pow(r,2);
}
float obwOk(float r){
	return 2*M_PI*r;
}

float poleTra(float a, float b, float h){
    return (a+b)/2*h;       // trapez równoramienny
}

float obwTra(float a, float b, float h){
    // trapez równoramienny: ramiona obliczamy z twierdzenia Pitagorasa
    // c = sqrt(((a-b)/2)^2 + h^2)
    float c = sqrt(pow((a-b)/2, 2) + h*h);
    return a + b + 2*c;
}

int main(int argc, char** argv) {
	cout<<"Program do obliczania figur"<<endl;
	cout<<"Wybierz figure: "<<endl;
	cout<<"[1] - prostokat"<<endl;
	cout<<"[2] - trojkat (rownoboczny)"<<endl;
	cout<<"[3] - okrag"<<endl;
	cout<<"[4] - trapez (rownoramienny)"<<endl;
	int fig;
	cin>>fig;
	switch(fig){
		case 1: {
			int a,b;
			cout<<"Podaj a = ";
			cin>>a;
			cout<<"Podaj b = ";
			cin>>b;
			cout<<"Pole prostokata = "<<polePr(a,b)<<endl;
			cout<<"Obwod prostokata = "<<obwPr(a,b)<<endl;
			break;
		}
		case 2: {
			float ta, h;
			cout<<"Podaj a = ";
			cin>>ta;
			cout<<"Podaj h = ";
			cin>>h;
			cout<<"Pole trojkata = "<<poleTr(ta,h)<<endl;
			cout<<"Obwod trojkata = "<<obwTr(ta)<<endl;
			break;
		}
		case 3: {
			float r;
			cout<<"Podaj r = ";
			cin>>r;
			cout<<"Pole okregu = "<<poleOk(r)<<endl;
			cout<<"Obwod okregu = "<<obwOk(r)<<endl;
			break;
		}
		case 4: {
			float a, b, h;
            cout<<"Podaj a = ";
            cin>>a;
            cout<<"Podaj b = ";
            cin>>b;
            cout<<"Podaj h = ";
            cin>>h;
            cout<<"Pole trapezu = "<<poleTra(a,b,h)<<endl;
            cout<<"Obwod trapezu = "<<obwTra(a,b,h)<<endl;
			break;
		}
		default:
			cout<<"Nie rozpoznano figury"<<endl;
			break;
	}

	return 0;
}