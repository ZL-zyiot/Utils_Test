#include <stdio.h>
#include <stdarg.h>
#include <string.h>
#include <stdlib.h>

int my_init_para(int para_num, char *p, ...)
{
	char string[1024] = "string: ";
	char *temp;
	va_list args;
	va_start(args, p);
	temp = p;
	strcat(string, temp);
	while(--para_num)
	{
		temp = va_arg(args, char*);
		if(temp)
		{
			strcat(string, temp);			
		}
		else
		{
			break;
		}
	}
	va_end(args);
	printf("%s\r\n", string);

	return 0;
}

int my_parse_para(int para_num, char *p, ...)
{
	char *temp;
	va_list args;
	va_start(args, p);
	temp = p;
	while (para_num--)
	{
		switch(*temp)
		{
			case 'p':
				temp++;
				int port = atoi(temp);
				temp = va_arg(args, char*);
				printf("port = %d\r\n", port);
			break;
			
			case 'b':
				temp++;
				int baud = atoi(temp);
				temp = va_arg(args, char*);
				printf("baud = %d\r\n", baud);
			break;

			case 'v':
				temp++;
				int verify = atoi(temp);
				temp = va_arg(args, char*);
				printf("verify = %d\r\n", verify);
			break;

			default:
				temp++;
			break;
		}
	}
	
}


int main(int argc, char *argv[])
{
	my_init_para(2, "para1", "para2");
	my_parse_para(3, "p1", "b115200", "v0");

	return 0;
}
