# Check-Diff-File
A little python script help me to figure out what difference between two 
similar project.

## Motivation
I tried to compile linux kernel with compiler flag -O0. This is tough for
me because I'm a newbie of linux kernel and I can't solve most of error 
complain by compiler.

As a GOP(google oriented programming) believer, I googled this question to
find some useful suggestion. Most of them said that I can't compile kernel with
O0 flag cause it should be compiled with O2 flags!

Fortunately, I found a book called runninglinuxkernel, the author modified linux
kernel and compiled it with O0! He also shared this [project](https://github.com/figozhang/runninglinuxkernel_5.0) in github. Since
I want to know how to solved the error complained by compiler not just take 
other project and run it. After I emailed to author, the author replied me but 
he told me all I need to do is solved every error I met when compile kernel.
And it is hard to be explained in a few words.

So I came an idea, why not just compare two project: the original 5.0 kernel and
the modifed one? So I make this project to compare the files of two projects 
intersectin and calulate files hash then compare it.

(poor english, feel free to correct it :D)


## Usage
```
./compare_project.py [absolute project path 1] [absolute project path 2]
```


