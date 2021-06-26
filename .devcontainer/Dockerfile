FROM nikaro/alpine-dev

RUN \
    # install required tools
    sudo apk add \
        entr \
        jq \
        py3-pip \
        ripgrep \
        wkhtmltopdf \
        xorg-server \
        && \
    python3 -m pip install resume-pycli && \
    :
