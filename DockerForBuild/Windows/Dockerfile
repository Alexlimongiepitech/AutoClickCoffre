FROM mcr.microsoft.com/windows:2009-amd64

WORKDIR /build
COPY ../../. /build

RUN cd ~
RUN Set-ExecutionPolicy -Scope CurrentUser
RUN RemoteSigned
RUN Get-ExecutionPolicy -List

RUN $script = New-Object Net.WebClient
RUN $script | Get-Member
RUN $script.DownloadString("https://chocolatey.org/install.ps1")
RUN iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex
RUN choco upgrade chocolatey

RUN choco install -y python3
RUN python -m pip install --upgrade pip