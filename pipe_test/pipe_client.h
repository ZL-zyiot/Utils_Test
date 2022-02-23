
#ifndef __PIPE_CLIENT_H__
#define __PIPE_CLIENT_H__
#ifdef __cplusplus
extern "C"
{
#endif

#include <windows.h>
#include "common.h"

DWORD WINAPI slave_thread(LPVOID param);

#ifdef __cplusplus
}
#endif
#endif
