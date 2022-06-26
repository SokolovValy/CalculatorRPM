#include <iostream>
#include <cstdlib>
using namespace std;
int main(){

  int q,w;
  
  q=0;
  w=0;
  
  char s;

while(true){
cout<<"Enter the data in the format: a+b"<<endl;
  cin>>q>>s>>w;

  switch(s){
 
    case '*':
	cout<<q*w<<endl;
    break;
    
    case '+':
	cout<<q+w<<endl;
    break;
    
    case '-':
	cout<<q-w<<endl;
    break;

    case '/':
	cout<<q/w<<endl;
    break;
    
    case '1':
    exit(1);
    
    default:
    exit(1);
	   }
	   }
	}
