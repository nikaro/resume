FROM nikaro/archlinux-dev

RUN \
    # install required tools
    sudo pacman -Syu --noconfirm \
        texlive-bibtexextra \
        texlive-bin \
        texlive-core \
        texlive-fontsextra \
        texlive-formatsextra \
        texlive-latexextra \
        && \
    # clean up
    sudo rm -r \
        /var/lib/pacman/sync \
        /var/cache/pacman/pkg \
        &&  \
    # pelican
    python3 -m pip install --user \
        pelican \
        && \
    # tlmgr
    sudo sed -i 's@"$Master/../.."@"$Master/../../.."@' /usr/share/texmf-dist/scripts/texlive/tlmgr.pl && \
    echo -e "\nalias tlmgr='/usr/share/texmf-dist/scripts/texlive/tlmgr.pl --usermode'" >> ~/.bashrc && \
    /usr/share/texmf-dist/scripts/texlive/tlmgr.pl --usermode init-usertree && \
    /usr/share/texmf-dist/scripts/texlive/tlmgr.pl --usermode option repository http://mirrors.rit.edu/CTAN/systems/texlive/tlnet && \
    :
