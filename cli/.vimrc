" windows uses _vimrc in ~\_vimrc
" linux uses .vimrc in ~/.vimrc

syntax enable

" :color Ctrl + D to see options
colorscheme koehler 

set tabstop=4     " number of visual spaces per TAB
set softtabstop=4 " number of spaces in tab
set expandtab     " tabs are spaces
set smartindent

set number
set ruler

"currently only works on linux 
set mouse=a

set ignorecase
set smartcase

set wildmenu
set wildmode=full

" windows seems to need this command to use backspace properly
" set backspace=indent,eol,start 
set spell
