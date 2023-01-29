FROM debian:latest

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
        # playwright dependencies
        gstreamer1.0-libav \
        libasound2 \
        libatk-bridge2.0-0 \
        libatspi2.0-0 \
        libdbus-glib-1-2 \
        libenchant-2-2 \
        libevent-2.1-7 \
        libgles2 \
        libgstreamer-gl1.0-0 \
        libgtk-3-0 \
        libharfbuzz-icu0 \
        libmanette-0.2-0 \
        libnspr4 \
        libnss3 \
        libopengl0 \
        libopenjp2-7 \
        libopus0 \
        libsecret-1-0 \
        libwebpdemux2 \
        libxtst6 \
        && \
    git clone --depth 1 https://github.com/ryanoasis/nerd-fonts.git /usr/local/share/nerd-fonts && \
    /usr/local/share/nerd-fonts/install.sh --install-to-system-path && \
    python3 -m pip install resume-pycli && \
    :
