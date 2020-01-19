## Make the change repeatable
test<F2>

If I’m in Insert mode with my cursor at the end of a line, the quickest way to open a new line is to press <CR> . And yet I sometimes prefer to press <Esc>o just because I anticipate that I might want that extra granularity from the undo command.
etes estes

I like to make each “undoable chunk” correspond to a thought. As I write this text (in Vim, of course!), I often pause at the end of a sentence to consider what I’ll write next. No matter how brief its duration, each pause forms a natural break point, giving me a cue to leave Insert mode. When I’m ready to continue writing, I press A and carry on where I left off.

If I decide that I’ve taken a wrong turn, I’ll switch to Normal mode and press u . Each time I undo, my text decomposes in coherent chunks that correspond to my thought process as I was writing the original text.

Just as painters spend a fraction of their time applying paint, programmers spend a fraction of their time composing code. More time is spent thinking, reading, and navigating from one part of a codebase to another. And when we do want to make a change, who says we have to switch to Insert mode? We can reformat existing code, duplicate it, move it around, or delete it. From Normal mode, we have many tools at our disposal.

https://github.com/kana/vim-textobj-entire
https://github.com/tpope/vim-commentary

Expert typists recommend drastic measures: delete the entire word; then type it out again. If you can type at a rate above sixty words per minute, retyping a word from scratch will only take a second. If you can’t type that fast, consider this to be good practice! There are particular words that I consistently mistype. Since I started following this advice, I’ve become more aware of which words trip me up. As a result, I now make fewer mistakes.
don't first visual then operate, operate + selection

cw... instead of c3w
the p for paragraph is useful too
gUaw
gUU
gcap gcG gcc
gh gw gu
K(man the word under cursor)
reselect the previous selected region gv
ctrl + r in insert mode to paste

for paste ,slow That’s because Vim inserts the text from the register as if it were being typed one character at a time. If the ‘textwidth’ or ‘autoindent’ options are enabled, you might end up with unwanted line breaks or extra indentation.
ctrl r ctrl p for smart paste (fast and without reformatting)

u in visual mode lowcase
gd
<leader><leader> s <char>	Search character
<leader><leader> f <char>	Find character forwards
<leader><leader> F <char>	Find character backwards
nice fonts https://wesbos.com/programming-fonts/  I use Consolas:h15
![](http://justfrenchy.fr/img/2019-03-11-18-04-02.png)
![](http://justfrenchy.fr/img/2019-03-11-18-09-33.png)
https://github.com/terryma/vim-expand-region    # nice extension for va}
vim -u NONE -N # don't read vimrc and non compatible
vim -u code/essential.vim
>G
normal.
:%normal A;
:%normal i//
cl=s
S = cc
& repeat substitute
:pwd
set autochdir   # wd always the same as the filed edited
:cd %:p:h     # current file directory for all windows
:lcd %:p:h # different for each window
:cd  # on home directory

db delete backward
daw vs diw(bdw)   daw also deletes the space, try on the following
sss ssss  daw = sss(cursor)
-3 + 051  set nrformats=
gc - toggles line comment. For example gcc to toggle line comment for current line and gc2j to toggle line comments for the current line and the next two lines.
gC - toggles block comment. For example gCi) to comment out everything within parenthesis.
https://coderoncode.com/tools/2017/04/16/vim-the-perfect-ide.html
