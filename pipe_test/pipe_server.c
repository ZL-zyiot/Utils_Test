
#include "pipe_server.h"
#include "stdio.h"


DWORD WINAPI master_thread(LPVOID param);
HANDLE hMaster_thread;
HANDLE master_hPipe = INVALID_HANDLE_VALUE;

uint8_t master_pipi_buf[PIPE_BUFFER_SIZE] = {0};

DWORD WINAPI master_thread(LPVOID param)
{
    DWORD writeNum;
    uint8_t exitflag = 1;

    printf("run master thread\r\n");
    master_hPipe = CreateNamedPipe(PIPE_NAME, PIPE_ACCESS_DUPLEX, \
                PIPE_TYPE_BYTE|PIPE_READMODE_BYTE, 2, \
                PIPE_BUFFER_SIZE, PIPE_BUFFER_SIZE, \
                1000, NULL);
    if(INVALID_HANDLE_VALUE == master_hPipe)
    {
        printf("create name pipe failed\r\n");
        goto out;
    }
    printf("wait for connect...\r\n");
    if(FALSE == ConnectNamedPipe(master_hPipe, NULL))
    {
        printf("connect failed\r\n");
        goto out;
    }
    printf("connected\r\n");

    while(exitflag)
    {
        scanf("%s", master_pipi_buf);
        if(FALSE == WriteFile(master_hPipe, master_pipi_buf, \
                    (DWORD)strlen(master_pipi_buf), &writeNum, NULL))
        {
            printf("write failed\r\n");
            exitflag = 0;
        }
    }
    return 0;
out :
    printf("close pipe\r\n");
    CloseHandle(master_hPipe);
    return -1;
}



HANDLE hMaster_thread;

void _thread_init(void)
{
    hMaster_thread = CreateThread(NULL, 0, master_thread, NULL, 0, NULL);

    WaitForSingleObject(hMaster_thread, INFINITE);

    printf("thread exit\r\n");

    CloseHandle(hMaster_thread);
}

int main(void)
{
    printf("先执行 server ，再执行 client \r\n");
    printf("init thread...\r\n");
    _thread_init();
    return 0;
}

