# Chankro

Your favourite tool to bypass __disable_functions__ and __open_basedir__ in your pentests. 

## How it works

PHP in Linux calls a binary (sendmail) when the mail() function is executed. If we have putenv() allowed, we can set the environment variable "LD_PRELOAD", so we can preload an arbitrary shared object. Our shared object will execute our custom payload (a binary or a bash script) without the PHP restrictions, so we can have a reverse shell, for example.

## Example:

The syntax is pretty straightforward:

```
$ python2 chankro.py --arch 64 --input rev.sh --output chan.php --path /var/www/html
```

Note: path is the absolute path where our .so will be dropped.

## Install

### Git

```
$ git clone https://github.com/TarlogicSecurity/Chankro.git
$ cd Chankro
$ python2 chankro.py --help
```

### [BlackArch](https://blackarch.org/)

```
# pacman -S chankro
$ chankro --help
```
