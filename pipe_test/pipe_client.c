
#include "pipe_client.h"
#include "stdio.h"


DWORD WINAPI slave_thread(LPVOID param);
HANDLE hSlave_thread;
HANDLE slave_hPipe = INVALID_HANDLE_VALUE;

uint8_t slave_pipi_buf[PIPE_BUFFER_SIZE] = {0};


DWORD WINAPI slave_thread(LPVOID param)
{
    DWORD readNum;
    uint8_t exitflag = 1;
    
    printf("run slave thread\r\n");

    if(WaitNamedPipe(PIPE_NAME, NMPWAIT_WAIT_FOREVER))
    {
        slave_hPipe = CreateFile(PIPE_NAME, GENERIC_READ|GENERIC_WRITE, \
                0, NULL, \
                OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
        if(INVALID_HANDLE_VALUE == slave_hPipe)
        {
            printf("connect pipe failed\r\n");
            goto out;
        }
    }
    else
    {
        goto out;
    }
    printf("connected\r\n");

    while(exitflag)
    {
        if(FALSE == ReadFile(slave_hPipe, slave_pipi_buf, sizeof(slave_pipi_buf), \
                        &readNum, NULL))
        {
            printf("read failed\r\n");
            exitflag = 0;
        }
        slave_pipi_buf[readNum] = 0;
        printf("get buffer data :\r\n");
        printf("%s\r\n", slave_pipi_buf);
    }
    return 0;
out :
    printf("close pipe\r\n");
    CloseHandle(slave_hPipe);
    return -1;
}



HANDLE hSlave_thread;

void _thread_init(void)
{
    hSlave_thread = CreateThread(NULL, 0, slave_thread, NULL, 0, NULL);

    WaitForSingleObject(hSlave_thread, INFINITE);

    printf("thread exit\r\n");

    CloseHandle(hSlave_thread);
}

int main(void)
{
    printf("init thread...\r\n");
    _thread_init();
    return 0;
}

