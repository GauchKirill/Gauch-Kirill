# создать ключ

ssh-keygen -t ed25519 -C "*usel.email*"

# Добавить ключ в SSH-agent

ssh-add ./my\_key

# добавить ключ в аккфунт на Github

settings -> SSH and GPG keys -> New SSH key

# клонировать репозиторий

git clone *URL*
