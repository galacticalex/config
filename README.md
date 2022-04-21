
<!-- SPDX-FileCopyrightText: Copyright 2022 Alex Murphy <supernova@alexmurphy.uk> -->
<!-- -->
<!-- SPDX-Licence-Identifier: CC0-1.0 -->

# [neovim](https://neovim.io/) config

_First time install notes to self._

[plug.vim](https://github.com/junegunn/vim-plug) is installed with:

> `curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim`.

Then, navigate into _~/.config/nvim/_ and run the following:

`git clone https://github.com/galacticalex/config.git ./`.

The first time neovim is opened it might error out because the colour scheme is not installed. This is not a problem. Proceed, then run:

`:PlugInstall`

Exit and re-open neovim. 

