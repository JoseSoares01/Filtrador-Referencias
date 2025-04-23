Claro! Aqui está um modelo de `README.md` bem estruturado para o seu projeto. Você pode copiar e colar no repositório do GitHub:

```markdown
# 📁 Filtrador de Referências - Versão Final

Este é um aplicativo em Python com interface gráfica (GUI) que permite filtrar dados de um arquivo principal (WZPRE) com base nas referências encontradas em um segundo arquivo (arquivo de referência). Ideal para uso em ambientes administrativos ou operacionais que lidam com grandes volumes de dados e precisam cruzar listas de referências.

---

## 🚀 Funcionalidades

- Leitura de arquivos `.csv` ou `.xlsx` como entrada.
- Filtragem de linhas com base na correspondência de referências entre dois arquivos.
- Geração de arquivo final com as linhas correspondentes.
- Escolha entre saída em CSV ou Excel.
- Interface gráfica intuitiva com PySimpleGUI.
- Barra de progresso visual e percentual durante o processamento.
- Botão de ajuda com explicação clara do processo.

---

## 🖼 Interface

A interface gráfica permite que o usuário:

1. Selecione o **Ficheiro WZPRE (Ficheiro 1)**.
2. Selecione o **Ficheiro de Referência (Ficheiro 2)**.
3. Escolha o **formato de saída** desejado (Excel ou CSV).
4. Visualize o **progresso do processamento** em tempo real.
5. Veja uma **prévia do resultado filtrado**.
6. Use o botão **Limpar** para reiniciar o processo.
7. Acesse a seção **Ajuda** com instruções detalhadas.

---

## 💾 Requisitos

- Python 3.7+
- pandas
- openpyxl (para arquivos .xlsx)
- PySimpleGUI

---

## 🔧 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script:
   ```bash
   python app_pos_bo.py
   ```

---

## 📚 Exemplo de Uso

- O programa abrirá uma janela onde você poderá selecionar dois arquivos.
- Ele procurará automaticamente pela coluna com o nome **referencia** (não sensível a maiúsculas/minúsculas).
- Apenas as linhas do Ficheiro 1 que tiverem referências encontradas no Ficheiro 2 serão mantidas.
- O resultado será salvo como `resultado_filtrado.csv` ou `resultado_filtrado.xlsx` na mesma pasta do Ficheiro 1.

---

## 🧑‍💻 Autor

**Janyel Luiza**  
Desenvolvido com foco em eficiência, praticidade e experiência do usuário.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## ✨ Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir issues ou pull requests.
```
