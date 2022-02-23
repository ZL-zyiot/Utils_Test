#ifndef __COMMON_H__
#define __COMMON_H__
#ifdef __cplusplus
extern "C"
{
#endif


typedef unsigned char   uint8_t;
typedef unsigned short  uint16_t;
typedef unsigned int    uint32_t;


#define PIPE_NAME   "\\\\.\\pipe\\packet_pipe"
#define PIPE_BUFFER_SIZE    (1024)

#ifdef __cplusplus
}
#endif
#endif
