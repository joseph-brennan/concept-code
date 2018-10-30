" windows uses _vimrc in ~\_vimrc
" linux uses .vimrc in ~/.vimrc

syntax enable

" :color Ctrl + D to see options
colorscheme koehler 

set tabstop=4     " number of visual spaces per TAB
set softtabstop=4 " number of spaces in tab
set expandtab     " tabs are spaces
set autoindent    " indent when moving to the next line while writing code
set smartindent   " similar but might be unneeded


set showmatch     "shows matching part of bracket pairs

set number
set ruler
set scrolloff=10  " let 10 lines before/after cursor during scroll

"currently only works on linux 
set mouse=a

set ignorecase
set smartcase
set hlsearch

set wildmenu
set wildmode=full

" windows seems to need this command to use backspace properly
set backspace=indent,eol,start 

set spell

" use F2 key to toggle paste mode to properly intent on and off depending which is needed
set pastetoggle=<F2>

" shows you the extra mode in use ie. --insert--(paste) when toggled on
set showmode

let g:auto_save = 1                   " enable AutoSave on Vim startup
let g:auto_save_no_updatetime = 0     " do not change the updatetime option
