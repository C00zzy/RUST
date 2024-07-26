#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/ip_icmp.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <time.h>

#define PING_PKG_S 64
#define PING_SLEEP_RATE 100000

unsigned short checksum(void *b, int len) {
	unsigned short *buf = b;
	unsigned int sum = 0;
	unsigned short result;

	while (len > 1) {
		sum += *buf++;
		len -= 2;
	}

	if (len == 1) {
		sum += *(unsigned char *)buf;
	}

	sum = (sum >> 16) + (sum & 0xFFFFF);
	sum += (sum >> 16);
	result = ~sum;
	return result;
}

void send_ping (int sockfd, struct sockaddr_in *addr, const char *ip_addr) {
	struct icmphdr icmp_hdr;
	struct sockaddr_in raddr;
	char packet[PING_PKG_S];
	memset(&icmp_hdr, 0, sizeof(icmp_hdr));
	memset(packet, 0, sizeof(packet));

	icmp_hdr.type = ICMP_ECHO;
	icmp_hdr.un.echo.id = getpid();
	icmp_hdr.un.echo.sequence = 1;
	icmp_hdr.checksum = checksum(&icmp_hdr, sizeof(icmp_hdr));

	memcpy(packet, &icmp_hdr, sizeof(icmp_hdr));

	if (sendto(sockfd, packet, sizeof(icmp_hdr), 0, (struct sockaddr *) addr, sizeof(*addr)) <= 0) {
		perror("sendto");
	} else {
		printf("Ping sent to %s\n", ip_addr);
	}
}

void receive_ping(int sockfd) {
	char buffer[1024];
	struct sockaddr_in addr;
	socklen_t len = sizeof(addr);

	if (recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr *)&addr, &len) > 0) {
		printf("Ping recieved from address\n");
	} else {
		perror("recvfrom");
	}
}

int main(int argc, char *argv[]) {
	if (argc != 2) {
		fprintf(stderr, "Usage: %s <IP Address>\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	const char *ip_addr = argv[1];
	int sockfd;
	struct sockaddr_in addr;

	if ((sockfd=socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)) < 0) {
		perror("socket");
		exit(EXIT_FAILURE);
	}

	memset(&addr, 0, sizeof(addr));
	addr.sin_family = AF_INET;
	addr.sin_addr.s_addr = inet_addr(ip_addr);

	while (1) {
		send_ping(sockfd, &addr, ip_addr);
		receive_ping(sockfd);
		usleep(PING_SLEEP_RATE);
	}

	close(sockfd);
	return 0;
}
