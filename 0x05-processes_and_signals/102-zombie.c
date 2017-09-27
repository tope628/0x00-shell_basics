#include <unistd.h>
     aux | grep -e 'Z+.*<defunct>'/ in parent process
#include <stdlib.h>
#include <sys/types.h>
#include <stdio.h>

/**
 * main - creates 5 zombie processes
 * Return: voided
 */

int main(void)
{
	pid_t zombie_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		if (zombie_pid > 0)
		{
			printf("Zombie process created, PID: %i\n", zombie_pid);
			sleep(2);
		}
		else
		{
			exit(0);
		}
	}
	return (0);
}

/**
 * infinite_while - infinite loop
 * Return: voided
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
