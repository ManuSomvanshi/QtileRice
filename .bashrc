#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

#Alias
alias ls='exa -a --color=always --group-directories-first --icons' # preferred listing
alias ranger='RANGER_LOAD_DEFAULT_RC=FALSE ranger'
alias svim='sudo -E vim'
alias rdata='ranger /mnt/Data'
alias room201='nmcli device wifi connect "201_5Ghz " password "ms20room201"'
alias wifi='nmcli device wifi'

#PS1 stuff
export PS1="\[$(tput bold)\]\[\033[38;5;04m\] \[$(tput sgr0)\]\[\033[38;5;14m\] \W ⟫\[$(tput sgr0)\] \[$(tput sgr0)\]"

#Run fetch
#PF_INFO="ascii title os host kernel de pkgs memory" XDG_CURRENT_DESKTOP="Qtile" PF_SEP=":" PF_COLOR=1 PF_COL1=4 PF_COL2=6 PF_COL3=5 pfetch

export PATH=$PATH:~/.local/bin:~/.config/rofi/scripts
export http_proxy="http://172.16.2.251:3128/"
export ftp_proxy="ftp://172.16.2.251:3128/"
export rsync_proxy="rsync://172.16.2.251:3128/"
export no_proxy="localhost,127.0.0.1,192.168.1.1,::1,*.local"
export HTTP_PROXY="http://172.16.2.251:3128/"
export FTP_PROXY="ftp://172.16.2.251:3128/"
export RSYNC_PROXY="rsync://172.16.2.251:3128/"
export NO_PROXY="localhost,127.0.0.1,192.168.1.1,::1,*.local"
export https_proxy="http://172.16.2.251:3128/"
export HTTPS_PROXY="http://172.16.2.251:3128/"
