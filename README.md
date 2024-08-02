Analisador de Linguagens de Programação no GitHub
Este script Python recupera e analisa as linguagens de programação usadas nos repositórios de um usuário do GitHub. Ele usa a GitHub API para obter os dados dos repositórios e exibe a distribuição das linguagens de programação em uma forma gráfica e textual.

``Funcionalidades``
- Recupera Dados dos Repositórios: Obtém todos os repositórios do usuário especificado.
- Analisa Linguagens de Programação: Compila estatísticas de uso das linguagens para cada repositório.
- Exibição Gráfica: Apresenta uma barra gráfica que mostra a porcentagem de bytes de código em cada linguagem.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

``Como usar:``
1. Clone o repositorio ``git clone https://github.com/Devkneves/language-statistics.git``  
2. Certifique-se de ter o requests instalado. Você pode instalá-lo usando pip: ``pip install requests`` no terminal linux, ou no CMD caso use Windows
3. Dentro do repositorio use o comando ``Python script.py > stats.md`` para executar o script e salvar o output no arquivo ``stats.md``
4. O script exibirá a distribuição das linguagens usadas em seus repositórios do GitHub.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Exemplo de Saída:
```txt
Python    1234567 bytes ##################------------------  50.00%
JavaScript  987654 bytes ###############-----------------------  40.00%
HTML       123456 bytes #####----------------------------  10.00%
```

------------------------------------------------------------------------------------------------------------------------------------------------------------------

``Observações:``

1. O token pessoal é necessário para autenticação e para evitar limites de taxa baixos impostos para usuários não autenticados.
2. As barras gráficas são simplificadas para uma visualização rápida; ajustes podem ser feitos para personalizar a saída.
