# Servidor HTTP Simples

Servidor HTTP básico implementado em Python puro usando sockets TCP. O objetivo é entender como funciona o protocolo HTTP sem usar frameworks.

## Sobre

Este é um projeto educacional que mostra como funciona a comunicação HTTP sobre TCP. O servidor aceita conexões, processa requisições manualmente e retorna respostas HTTP/1.1.

## Tecnologias

- Python 3
- Biblioteca `socket`
- Biblioteca `urllib.parse`

Sem dependências externas.

## Como funciona

1. Cria socket TCP
2. Bind em localhost:8080
3. Aguarda conexão (accept é bloqueante)
4. Recebe requisição HTTP
5. Processa método e caminho
6. Retorna resposta HTTP formatada
7. Fecha conexão

## Rotas

| Rota | Descrição | Exemplo |
|------|-----------|---------|
| `/` | Página inicial | `http://localhost:8080/` |
| `/uppercase?text=hello` | Converte texto para maiúsculas | `http://localhost:8080/uppercase?text=hello` |
| Qualquer outra | Retorna 404 | `http://localhost:8080/qualquercoisa` |

## Como usar

Tenha Python 3 instalado, depois:

```bash
python server.py
```

Acesse no navegador:
```
http://localhost:8080/
```

Ou teste com curl:
```bash
curl http://localhost:8080/
curl "http://localhost:8080/uppercase?text=hello"
```

## Detalhes técnicos

O servidor usa `socket.socket(AF_INET, SOCK_STREAM)` para criar um socket TCP.

Depois faz bind na porta 8080 e fica esperando conexões com `accept()`, que é bloqueante.

Quando chega uma requisição, o servidor lê com `recv(1024)`, faz parse da primeira linha (`GET /path HTTP/1.1`) e monta a resposta no formato:

```
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 13

Hello, World!
```

## Limitações

- Só processa uma conexão por vez
- Só aceita GET (sem POST, PUT, DELETE)
- Sem suporte a arquivos estáticos
- Sem segurança (HTTP, sem autenticação)
- Não trata keep-alive

É um projeto didático, não para produção.

## Testes

```bash
# Página inicial
curl http://localhost:8080/

# Converter para maiúsculas
curl "http://localhost:8080/uppercase?text=python"
# Retorna: PYTHON

# Página inexistente
curl http://localhost:8080/naoexiste
# Retorna: Página não encontrada
```

## Referências

- [RFC 2616 - HTTP/1.1](https://www.rfc-editor.org/rfc/rfc2616)
- [Python socket docs](https://docs.python.org/3/library/socket.html)
