#include <stdio.h>
#include <math.h>
#include <string.h>

int main() {

	int t;
	scanf("%d",&t);
	while(t--) {
		unsigned long long int i,n,c=0,s;
		char a[55]={'\0'};
		scanf("%s",a);
		n=strlen(a);
		if(n==1)
			printf("2\n");
		else {
			if(a[0]!=a[1])
				c++;
			for(i=1;i<n-1;i++) {
				if((a[i]!=a[i+1])&&(a[i]!=a[i-1]))
					c++;
			}
			if(a[n-1]!=a[n-2])
				c++;
			s=pow(2,c);
			printf("%llu\n",s);
		}
	}
	return 0;
}