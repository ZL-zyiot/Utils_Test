
#ifndef __PIPE_SERVER_H__
#define __PIPE_SERVER_H__
#ifdef __cplusplus
extern "C"
{
#endif

#include <windows.h>
#include "common.h"

DWORD WINAPI master_thread(LPVOID param);

#ifdef __cplusplus
}
#endif
#endif
