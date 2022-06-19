FROM debian:stable-slim

RUN \
    # install required tools
    apt-get update --yes && \
    apt-get install --yes \
        bash-completion \
        bsdmainutils \
        entr \
        git \
        jq \
        python3-pip \
        ripgrep \
        wkhtmltopdf \
        && \
    git clone https://github.com/ryanoasis/nerd-fonts.git /usr/local/share/nerd-fonts && \
    /usr/local/share/nerd-fonts/install.sh --install-to-system-path && \
    python3 -m pip install resume-pycli && \
    :
