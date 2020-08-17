# Calculadora de Média Personalizada (FM_IEP)

Projeto feito para fins estudantis,mas utilizado por profissionais. Meu primeiro projeto executável,criado para otimizar o tempo que os professores levariam para contabilizar a média final de cada aluno na instituição de ensino Instituto Ieda Picon,localizada em Embu das Artes - SP - Brasil.

## 🚀 Objetivo da Aplicação

O objetivo deste projeto foi de otimizar o tempo que o professor levava para fechar as médias finais de cada aluno dentro da instituição. Além disso, há a diminuição de erros devido o uso de números flutuantes em grande quantidade,pois apenas com o uso da calculadora normal,ocorria uma certa dificuldade para manipular os números,levando a erros e por consequência reinicio da contagem das notas. Com o uso da Calculadora Personalizada, de acordo com as notas requeridas pela institutição, o professor em menos tempo consegue concluir o "fechamento" de todas as médias finais. Outrossim, o programa cria um arquivo txt que facilita a passagem de notas para o sistema oficial da instituição.

## 📋 Pré-Requisitos

Sistema Operacional Windows

## 🔧 Instalação

Necessário apenas o dowload do arquivo **FECHAMENTO_MÉDIA.EXE** localizado neste repositório.

## ⚙️ Execução

A forma de uso é extremamente simples e intuitiva. O professor inicialmente digita a série e a quantidade de alunos referente a série digitada, após isso o programa recebe as notas de cada atividade feita por aluno da série,simultanêamente o programa registra a turma, número de chamada, média e situação em forma de tabela em um arquivo txt. Ao fim da adição de notas pela serie o professor tem opções de fechar mais médias, ver as médias que ja foram fechadas ou apagar os dados do arquivo.

## :newspaper: Screens
![tela1](https://user-images.githubusercontent.com/64699971/90288822-11c40e00-de51-11ea-9c5d-ee0aea2c7a5f.png)
![tela2](https://user-images.githubusercontent.com/64699971/90288824-12f53b00-de51-11ea-89d3-b88d14e9abed.png)
![tela4](https://user-images.githubusercontent.com/64699971/90288825-12f53b00-de51-11ea-95b4-192bdac41976.png)
![tela5](https://user-images.githubusercontent.com/64699971/90288827-138dd180-de51-11ea-9af1-e4e3c649879b.png)


### 🔩 Análise dos dados inseridos

As diretrizes de notas da intituição segue a seguinte relação:
* Para o aluno ser aprovado sua média final deve ser equivalente ou maior a 7 pontos finais.
* Caso o aluno tenha a somatória das notas equivalente ou maior a 6.75 pontos,sua média final será arredondada para 7 pontos finais,sendo aprovado.
* Caso o aluno tenha a somatória das notas equivalente ou menor a 6.74 pontos,sua média final será arredondada para 6.5 pontos finais,sendo reprovado.

O arredondamento das notas é baseada em:
* Para a parte decimal da nota ser arredondada para cima,deve ser equivalente ou maior a 0.25 décimos.
* Para a parte decimal da nota ser arredondada para baixo,deve ser equivalente ou menor a 0.24 décimos.
```
NOTA FINAL: 5.26
ALUNO REPROVADO! - NOTA: 5.5
_____________________________
NOTA FINAL: 5.23
ALUNO REPROVADO! - NOTA: 5.0
```

## 📦 Utilização

O arquivo executável foi enviado para os professores da instituição que utilizam ao final do bimestre. O feedback recebido pelos professores é de que o programa foi extremamente útil pois otimizou o tempo que levariam para concluir a atividade e houve a diminuição da taxa de erros com números flutuantes.

## 🛠️ Ferramentas

* [Python 3](https://www.python.org/downloads/) - O compilador/IDE utilizado.
* [PyInstaller](https://www.pyinstaller.org/) - Biblioteca utilizada para gerar o arquivo executável.

## 📌 Versão

Este projeto possui um intuito estudantil, logo as versões são publicadas conforme o aprendizado evolui, atualmente está na segunda versão.

## ✒️ Autor

* **Victor Alves de Oliveira** - Bacharel de Sistemas de Informação - Universidade Federal de Viçosa (UFV-CRP). - victoralvees17@gmail.com

## 🎁 Expressões de gratidão

* Agradecimento ao [Instituto Ieda Picon](https://www.institutoiedapicon.com.br/)
* Agradeço,pelo auxílio na lógica do programa, Gabriel Costa Silva - Bacharel em Engenharia Química - Universidade de São Paulo (USP) - gcosta.gcs@usp.br
