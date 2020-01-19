## voice
say -v Whisper "Now I am whispering"
say -v Anna 'Guten Tag!'

## Find and rename
## Duplicate lines

## Replace lines
Get bundle id osascript -e 'id of app "praat"'
cd -  # go back to the previous folder
echo $0  / echo $SHELL # echo the shell
open -a "QuickTime Player" ~/Desktop/filename.mp4
open x (with default app)

## R

R -e 'rmarkdown::render("rToVim.Rmd","word_document")' && open rToVim.docx
http://blog.fellstat.com/?cat=11
https://github.com/chuyuanli/Text-Mining-Project/blob/master/projet_li.Rm

## zsh
https://stackoverflow.com/questions/37398532/how-do-i-yank-into-the-system-register-from-v-imode
http://stchaz.free.fr/mouse.zsh   mouse and copy paste in zsh
exec bash  / bash/ zsh
ctrl n and p to scroll among suggestions
ctrl l to clear

## Tmux

Start new named session: tmux new -s [session name]
Detach from session: ctrl+b d
List sessions: tmux ls
Attach to named session: tmux a -t [name of session]
Kill named session: tmux kill-session -t [name of session]
Split panes horizontally: ctrl+b "
Split panes vertically: ctrl+b %
Kill current pane: ctrl+b x
Move to another pane: ctrl+b [arrow key]
Cycle through panes: ctrl+b o
Cycle just between previous and current pane: ctrl+b ;
Kill tmux server, along with all sessions: tmux kill-server

# iterm
https://www.iterm2.com/documentation-one-page.html
