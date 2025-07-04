#!/bin/bash
USER_NAME=${USER_NAME:-user$(date +%s)}

useradd -m $USER_NAME
echo "$USER_NAME:$USER_NAME" | chpasswd
mkdir -p /home/$USER_NAME/.vnc
echo "$USER_NAME" | vncpasswd -f > /home/$USER_NAME/.vnc/passwd
chmod 600 /home/$USER_NAME/.vnc/passwd
chown -R $USER_NAME:$USER_NAME /home/$USER_NAME

echo "Starting VNC for $USER_NAME..."
su - $USER_NAME -c "/usr/bin/vncserver :1 -geometry 1280x800 -depth 24 && tail -F /home/$USER_NAME/.vnc/*.log"
