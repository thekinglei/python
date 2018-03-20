#coding=utf-8
from cmd import Cmd
import os
import sys

class Cli(Cmd):

    intro = "welcome to commands line;\nif you don't know how to use it,please type 'help'"
    # prompt是命令行标志符
    prompt = ">>"
    def __init(self):
        Cmd.__init__(self)

    def do_hello(self,line):

        print "hello",line

    def do_show(self,name):
        print "func:show"
        print name    
    def do_exit(self,exit_status=None):
        if exit_status:
            exit(exit_status)
        else:
            exit(0)

if __name__ == '__main__':
    cli = Cli()
    cli.cmdloop()
