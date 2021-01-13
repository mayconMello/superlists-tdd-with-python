Provisionamento de um novo site
==============================

## Pacotes ncessários:

* nginx
* Python 3.8
* virtualenv + pip
* Git

## Configuração do Nginx Virtual Host

* veja nginx.template.conf
* subsitua SITENAME, por exemplo, por staging.my-domain.com

## Serviço Systemd

* veja gunicorn-systemd.template.service
* substitua SITENAME, por exemplo, por staging.my-domain.com

## Estrutura de pastas:
Suponha que temos uma conta de usuário em /home/username

/home/username 

└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv
