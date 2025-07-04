import subprocess

def create_user_container(user_id, port):
    container_name = f"user_{user_id}"
    subprocess.run([
        "docker", "run", "-d",
        "--name", container_name,
        "-p", f"{port}:80",
        "dorowu/ubuntu-desktop-lxde-vnc",
    ])