# Vim Basics

*from [Yann Esposito](http://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/)*

Vim is lauded as one of the most powerful text editors, and as one of the most popular among high-profile software developers. One of its benefits is its text-driven interface, which is available on almost any terminal or server. Read more at [Wikipedia](https://en.wikipedia.org/wiki/Vim_%28text_editor%29). To install Vim on Ubuntu, use the command `sudo apt-get install vim`.

To move around in Vim, you can always fall back to the trusty arrow keys, but the proper way to navigate character-by-character is with the `h`, `j`, `k`, and `l` keys. The `w` (start of next word), `b` (beginning of word behind), and `e` (end of next word) commands are also helpful for quick navigation.

In Vim, there are two primary modes, 'NORMAL' and 'INSERT'. 'NORMAL' is the mode you start in and use for navigation, and 'INSERT' is the mode you need to enter if you want to actually modify or add new text. To enter 'NORMAL' mode, just hit the `Esc` key. To enter 'INSERT' mode, just hit the `i` key.

To save and close a document, you need to type `:wq` then hit enter. `:` is the Vim syntax to start entering a command, `w` is the command to save/write a file, and `q` is the command to quit.

To access help about any feature in Vim, type `:help <command>` and hit enter.
