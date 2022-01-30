
-- SPDX-FileCopyrightText: Copyright 2022 Alex Murphy <supernova@alexmurphy.uk>
--
-- SPDX-Licence-Identifier: EPL-2.0


--[[ notes and resources

https://vonheikemen.github.io/devlog/tools/configuring-neovim-using-lua/
:h 

]]--


-- options

vim.opt.number = true
vim.opt.ignorecase = true

vim.opt.expandtab = true
vim.opt.tabstop = 2
vim.opt.shiftwidth = 2 vim.opt.softtabstop = 2 vim.wo.colorcolumn = "110"

vim.cmd("colorscheme murphy")


-- keybindings 

vim.api.nvim_set_keymap("n", "<C-h>", "<C-w><C-h>", {noremap = true})
vim.api.nvim_set_keymap("n", "<C-j>", "<C-w><C-j>", {noremap = true})
vim.api.nvim_set_keymap("n", "<C-k>", "<C-w><C-k>", {noremap = true})
vim.api.nvim_set_keymap("n", "<C-l>", "<C-w><C-l>", {noremap = true})

vim.api.nvim_set_keymap("n", ";", ":", {noremap = true})
vim.api.nvim_set_keymap("n", "<C-s>", "<Esc>:w<Enter>", {noremap = true})
vim.api.nvim_set_keymap("n", "<C-j>", "<Esc>:w<Enter>:source %<Enter>", {noremap = true})
vim.api.nvim_set_keymap("n", "TT", ":terminal<Enter>:set nonumber<Enter>a", {noremap = true})
vim.api.nvim_set_keymap("n", "BB", ":terminal<Enter>:set nonumber<Enter>arlwrap bb<Enter>", {noremap = true})

vim.api.nvim_set_keymap("i", "jj", "<Esc>", {noremap = true})
vim.api.nvim_set_keymap("i", "<C-f>", "<Esc>A", {noremap = true})

vim.api.nvim_set_keymap("t", "<Esc>", "<C-\\><C-n>", {noremap = true})
vim.api.nvim_set_keymap("t", "jj", "<C-\\><C-n>", {noremap = true})
vim.api.nvim_set_keymap("t", "<C-f>", "<Right><Right><Right><Right><Right><Right>", {noremap = true})


-- plugin manager

vim.cmd([[

call plug#begin(stdpath('data') . '/plugged')

Plug 'Olical/conjure'
Plug 'jiangmiao/auto-pairs'

call plug#end()

]])


-- leader keys

vim.g.mapleader = " "
vim.g.maplocalleader = " "


-- clerk

vim.cmd([[
function! ClerkShow()
  exe "w"
  exe "ConjureEval (nextjournal.clerk/show! \"" . expand("%:p") . "\")"
endfunction

nmap <silent> <localleader>cs :execute ClerkShow()<CR>
]])

-- currently unused

-- doesn't seem necessary any more!
--vim.cmd(setnocompatible)

-- replaced by auto-pairs
--vim.api.nvim_set_keymap("i", "(", "()<Left>", {noremap = true})
--vim.api.nvim_set_keymap("i", "[", "[]<Left>", {noremap = true})
--vim.api.nvim_set_keymap("i", "{", "{}<Left>", {noremap = true})
--vim.api.nvim_set_keymap("i", "\"", "\"\"<Left>", {noremap = true})
--vim.api.nvim_set_keymap("t", "(", "()<Left>", {noremap = true})
--vim.api.nvim_set_keymap("t", "{", "{}<Left>", {noremap = true})
--vim.api.nvim_set_keymap("t", "[", "[]<Left>", {noremap = true})
--vim.api.nvim_set_keymap("t", "{", "{}<Left>", {noremap = true})
--vim.api.nvim_set_keymap("t", "\"", "\"\"<Left>", {noremap = true})


-- motivation

print("Get cracking!")


