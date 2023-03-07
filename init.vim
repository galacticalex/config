set number
imap jj <Esc>
map <C-s> :w<Enter>
set ignorecase

call plug#begin()
Plug 'romainl/Apprentice'
Plug 'vim-airline/vim-airline'
Plug 'axelf4/vim-strip-trailing-whitespace'
Plug 'luochen1990/rainbow'

Plug 'guns/vim-sexp'
Plug 'tpope/vim-repeat'
Plug 'jiangmiao/auto-pairs'

Plug 'Olical/conjure'

Plug 'mileszs/ack.vim'
call plug#end()

let g:rainbow_active = 1
colorscheme desert

nnoremap <Space> <Nop>
let g:mapleader = " "
let g:maplocalleader = " "
