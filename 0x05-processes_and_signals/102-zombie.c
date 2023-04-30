#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <signal.h>

/**
 * main - Creates 5 zombie processes
 *
 * Return: 0 (success)
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == -1)
		{
			perror("fork error");
			exit(EXIT_FAILURE);
		}
		else if (pid == 0)
		{
			/* Child Process */
			exit(EXIT_SUCCESS);
		}
		else
		{
			/* Parent Process */
			printf("Zombie process created, PID: %d\n", pid);
		}
	}

	/* Infinite loop */
	while (1)
	{
		sleep(1);
	}
	return (0);
}
