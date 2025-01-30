# just-chat
Simple one-click deployment of huggingface-chat to interact with LLM

## Install Docker and Docker Compose
If you never installed Docker and Docker Compose, you can use the following instructions to install them. Otherwise you can skip this step.
To check if you have Docker and Docker Compose installed, you can use the following commands:

```bash
docker --version
docker-compose --version
```
The commands apply to both Linux (bash) and Windows (PowerShell). After this point instaltion split into Linux and Windows.


## On Linux
### Install Docker and Docker-compose Standalone

Refer to the official guides: 
 - [Docker Installation Guide](https://docs.docker.com/engine/install/ubuntu/).
 - [Docker-compose Standalone Installation Guide](https://docs.docker.com/compose/install/standalone/).
 
 For Ubuntu users, you can review and use the provided convenience.sh script, executing the code below. Running the script will install Docker and Docker Compose.Otherwise you can follow the steps presented after this command.

  ```bash
  ./scripts/install_docker_ubuntu.sh
  ```


### Setup Docker’s apt repository

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
#Updates the package lists (apt-get update).
#Installs required packages (ca-certificates and curl) for handling HTTPS-based repositories.

sudo install -m 0755 -d /etc/apt/keyrings
#Creates the /etc/apt/keyrings directory with 0755 permissions (readable and executable by everyone, writable only by the owner).
#This directory is used to store GPG keys securely.

sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
#Downloads Docker’s official GPG key (used to verify package authenticity) and saves it to /etc/apt/keyrings/docker.asc.
#Changes file permissions so that all users can read it (a+r).


# Add the repository to Apt sources:
#Adds Docker’s official repository to the system's package sources.
#dpkg --print-architecture ensures the right package architecture (amd64, arm64, etc.).
#. /etc/os-release && echo "VERSION_CODENAME" dynamically fetches your Ubuntu version codename (e.g., jammy for Ubuntu 22.04).
#Writes the repository URL into /etc/apt/sources.list.d/docker.list.
#> /dev/null discards unnecessary output.

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "ЁVERSION_CODENAMEЁ") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  sudo apt-get update

```


### Install latest Docker and docker-compose standalone packages

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
#Installs:
#docker-ce (Docker Community Edition engine)
#docker-ce-cli (Docker CLI tools)
#containerd.io (Container runtime for managing containers)
#docker-buildx-plugin (Next-gen build system for Docker)
#docker-compose-plugin (Plugin for Docker Compose v2)

curl -SL https://github.com/docker/compose/releases/download/v2.32.4/docker-compose-linux-$(uname -m) -o /usr/local/bin/docker-compose
#Downloads the latest Docker Compose binary (v2.32.4) from GitHub.
#$(uname -m) ensures that the correct architecture (e.g., x86_64, aarch64) is downloaded.
#Saves it to /usr/local/bin/docker-compose.

chmod +x /usr/local/bin/docker-compose
#Changes file permissions to make it executable.

sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
#Creates a symbolic link from /usr/local/bin/docker-compose to /usr/bin/docker-compose.
#This allows you to run Docker Compose commands without specifying the full path.
```


## On Windows

### Prerequisites
Before installing Docker on Windows, ensure your system meets the following requirements:

Windows 10 (Pro, Enterprise, Education) Version 1909 or later
Windows 11 (any edition)
WSL 2 (Windows Subsystem for Linux) enabled (recommended) link here [https://learn.microsoft.com/en-us/windows/wsl/install]
Hyper-V enabled (if using Windows 10 Pro/Enterprise)
At least 4GB of RAM (recommended)

Though WSL is not strictly required for installation, it is highly recommended for running Linux-based containers efficiently.
If you don’t want to use WSL during Docker Desktop installation, uncheck the option "Use WSL 2 instead of Hyper-V".
Docker will automatically switch to Windows Containers instead of Linux Containers.

Limitations Without WSL:
-You cannot run Linux-based containers (unless using a full virtual machine).
-Performance is slower because it uses Hyper-V (Windows 10 Pro/Enterprise) or Windows-native virtualization.
-Some Docker features (e.g., Kubernetes support) won’t work.


### Install Docker Desktop
1. Download Docker Desktop [https://docs.docker.com/desktop/setup/install/windows-install/]

2. Install Docker Desktop:
-Locate the Docker Desktop Installer.exe file in your Downloads folder.
-Double-click to start the installation.
-Check the required options:
--Enable WSL 2 (recommended)
--Enable Windows Containers (optional, needed for Windows-based containers).
-Click Install and wait for it to complete.

3. Restart Your PC
After installation, restart your computer to apply the changes.

4. Run Docker Desktop
Open Start Menu and search for Docker Desktop.
Click to launch Docker.
Wait for it to start (it may take a few seconds).
You should see the Docker whale 🐳 icon in the taskbar.

5. Install Docker Compose on Windows
Docker Compose v2 is already built into Docker Desktop. 
If you need standalone Docker Compose v1, install it manually:

Download the latest Docker Compose binary:
In powershell
```
curl -SL "https://github.com/docker/compose/releases/download/v2.32.4/docker-compose-windows-x86_64.exe" -o "C:\Program Files\Docker\Docker\resources\bin\docker-compose.exe"
```

Add Docker Compose to System Path (if not already).
Restart your system.

Docker works best with Windows Subsystem for Linux (WSL 2). 
Open Docker Desktop, go to Settings → General, and check:
Use WSL 2 for Linux containers.

6. Ensure Docker Starts on Boot (Optional)
To make Docker automatically start:
Open Docker Desktop.
Go to Settings → General.
Enable “Start Docker Desktop when you log in”.



## For both operating systems

### Verify installation

```bash
sudo docker run hello-world
docker-compose --version
```

## Clone Just-Chat repository
```bash
git clone https://github.com/winternewt/just-chat.git
```

## Start the application
```bash
docker compose up
```


## Some notes
1. After the application is started, you can access the chat interface at 0.0.0.0:3000.

2. If you want to change some settings, the docker-compose.yml has the controls.However changing them IS NOT necessary. In the file you can find 
  the port(found under huggingchat-ui service)
  the model name (found under chat-env-generator service)
  the database name (found under chat-mongo service)
  the UI name (found under huggingchat-ui service)
  the API key (found under chat-env-generator service).

3. If you have errors from having previously run docker compose, check in terminal with command "docker ps" if there are other containers running that might cause conflicts.

4. If you want to stop those containers go to the folder where they originated (in terminal using 'cd' command) and run "docker compose down". To avoid such problems for future make sure after each run of 'docker compose up' you run 'docker compose down' or CTRL+C to stop all containers.
