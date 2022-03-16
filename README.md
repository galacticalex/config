# [neovim](https://neovim.io/) config

## Remember a few things:

Plugin manager installed with 

`curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim` (from [here](https://www.linode.com/docs/guides/how-to-install-neovim-and-plugins-with-vim-plug/)

Navigate to `~/.config/nvim` and run:

`git clone https://github.com/galacticalex/config.git .`

Opening first time will error out because the colour scheme is not installed. This is not a problem. Proceed, then run:

`:PlugInstall`

Exit and re-open neovim. 
