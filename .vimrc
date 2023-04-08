syntax on
syntax enable

set rnu 
set nu 
set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set wrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
set laststatus=2
set noshowmode
set sw=2
set conceallevel=2
set background=dark
set updatetime=300
set shortmess+=c

"plugin install
call plug#begin('~/.vim/plugged')
    Plug 'itchyny/lightline.vim'
    Plug 'preservim/nerdtree'
    Plug 'frazrepo/vim-rainbow'
    Plug 'lervag/vimtex'
    Plug 'KeitaNakamura/tex-conceal.vim', {'for': 'tex'}
    Plug 'morhetz/gruvbox'
    Plug 'shinchu/lightline-gruvbox.vim'
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    Plug 'SirVer/ultisnips'
call plug#end()

"latex settings
filetype indent on
let g:tex_conceal_frac=1 
let g:tex_conceal="abdgm"
let g:vimtex_view_method = 'zathura'
let g:tex_flavor = 'latex'
let g:vimtex_complete_enabled=1
let g:vimtex_quickfix_mode=0
let g:vimtex_syntax_custom_cmds = [
          \ {'name': 'vb', 'mathmode': 1, 'argstyle': 'bold'},
          \ {'name': 'R', 'mathmode': 1, 'concealchar': 'ℝ'},
          \ {'name': 'C', 'mathmode': 1, 'concealchar': 'ℂ'},
          \ {'name': 'N', 'mathmode': 1, 'concealchar': 'ℕ'},
          \ {'name': 'Z', 'mathmode': 1, 'concealchar': 'ℤ'},
          \ {'name': 'Q', 'mathmode': 1, 'concealchar': 'ℚ'},
          \ {'name': 'a', 'mathmode': 1, 'concealchar': 'α'},
          \ {'name': 'b', 'mathmode': 1, 'concealchar': 'β'},
          \ {'name': 'g', 'mathmode': 1, 'concealchar': 'γ'},
          \ {'name': 'e', 'mathmode': 1, 'concealchar': 'ϵ'},
          \ {'name': 'p', 'mathmode': 1, 'concealchar': 'ϕ'},
          \ {'name': 'd', 'mathmode': 1, 'concealchar': 'δ'},
          \ {'name': 's', 'mathmode': 1, 'concealchar': 'σ'},
          \]
inoremap <C-f> <Esc>: silent exec '.!inkscape-figures create "'.getline('.').'" "'.b:vimtex.root.'/Figures/"'<CR><CR>:w<CR>
nnoremap <C-f> : silent exec '!inkscape-figures edit "'.b:vimtex.root.'/Figures/" > /dev/null 2>&1 &'<CR><CR>:redraw!<CR>
"Use 24-bit (true-color) mode in Vim/Neovim when outside tmux.
"If you're using tmux version 2.2 or later, you can remove the outermost $TMUX check and use tmux's 24-bit color support
"(see < http://sunaku.github.io/tmux-24bit-color.html#usage > for more information.)
if (empty($TMUX))
  "For Neovim > 0.1.5 and Vim > patch 7.4.1799 < https://github.com/vim/vim/commit/61be73bb0f965a895bfb064ea3e55476ac175162 >
  "Based on Vim patch 7.4.1770 (`guicolors` option) < https://github.com/vim/vim/commit/8a633e3427b47286869aa4b96f2bfc1fe65b25cd >
  " < https://github.com/neovim/neovim/wiki/Following-HEAD#20160511 >
  if (has("termguicolors"))
    set termguicolors
  endif
endif

"theme-ing vim
let g:gruvbox_italic=1
let g:gruvbox_transparent_bg=1
let g:gruvbox_termcolors=256
let g:gruvbox_italicize_comments=1
autocmd VimEnter * hi Normal guibg=NONE ctermbg=NONE

"plugin options
let g:lightline = {}
let g:lightline.colorscheme = 'gruvbox'
colorscheme gruvbox
let mapleader = " "

"snippet options
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<c-b>"
let g:UltiSnipsJumpBackwardTrigger="<c-z>"
let g:UltiSnipsEditSplit="vertical"
let g:UltiSnipsSnippetsDir="~/.vim/plugged/ultisnips"
let g:UltiSnipsSnippetDirectories="~/.vim/plugged/ultisnips"
let g:UltiSnipsSnippetStorageDirectoryForUltiSnipsEdit="~/.vim/plugged/ultisnips"

"insert mappings
imap jh <ESC>
"normal mappings
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <leader>t :vert :term<CR>
