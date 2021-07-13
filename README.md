# Calculadora de Média Personalizada (FM_IEP)

Projeto feito para fins estudantis,mas utilizado por profissionais. Meu primeiro projeto executável,criado para otimizar o tempo que os professores levariam para contabilizar a média final de cada aluno na instituição de ensino Instituto Ieda Picon,localizada em Embu das Artes - SP - Brasil.

## 🚀 Objetivo da Aplicação

O objetivo deste projeto foi de otimizar o tempo que o professor levava para fechar as médias finais de cada aluno dentro da instituição. Além disso, há a diminuição de erros devido o uso de números flutuantes em grande quantidade,pois apenas com o uso da calculadora normal,ocorria uma certa dificuldade para manipular os números,levando a erros e por consequência reinicio da contagem das notas. Com o uso da Calculadora Personalizada, de acordo com as notas requeridas pela institutição, o professor em menos tempo consegue concluir o "fechamento" de todas as médias finais. Outrossim, o programa cria um arquivo txt que facilita a passagem de notas para o sistema oficial da instituição.

## 📋 Pré-Requisitos

Sistema Operacional Windows

## 🔧 Instalação

Necessário apenas o dowload do arquivo [**FECHAMENTO_MÉDIA_IEP**](https://drive.google.com/drive/folders/1NR1sQgU7Euo3dxfdbW52yuv0BYYfbTh6?usp=sharing). 

## ⚙️ Execução

A forma de uso é extremamente simples e intuitiva. O professor inicialmente digita a série e a quantidade de alunos referente a série digitada, após isso o programa recebe as notas de cada atividade feita por aluno da série,simultanêamente o programa registra a turma, número de chamada, média e situação em forma de tabela em um arquivo txt. Ao fim da adição de notas pela serie o professor tem opções de fechar mais médias, ver as médias que ja foram fechadas ou apagar os dados do arquivo.

## :newspaper: Screens
<p align="center">
  <img width="500" height="350" src="https://user-images.githubusercontent.com/64699971/98950103-58201c00-24d7-11eb-9749-18fb82e51000.png">
  <img width="500" height="650" src="https://user-images.githubusercontent.com/64699971/98950104-58b8b280-24d7-11eb-961e-f76e8e9c56ca.png">
  <img width="500" height="350" src="https://user-images.githubusercontent.com/64699971/98950107-58b8b280-24d7-11eb-82e0-c2a85535e424.png">
  <img width="500" height="650" src="https://user-images.githubusercontent.com/64699971/98950109-58b8b280-24d7-11eb-8025-6805bb9258ac.png">
  <img width="500" height="350" src="https://user-images.githubusercontent.com/64699971/98949888-0f686300-24d7-11eb-99a0-6eb002f3f53d.png">
  <img width="500" height="350" src="https://user-images.githubusercontent.com/64699971/98950111-59514900-24d7-11eb-95e5-6fe9a339a15b.png">
  <img width="500" height="100" src="https://user-images.githubusercontent.com/64699971/98950101-57878580-24d7-11eb-8b7f-62825537ffc4.png">
</p>


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

* [VS Code](https://code.visualstudio.com/)
* [Python 3](https://www.python.org/downloads/)
* [PyInstaller](https://www.pyinstaller.org/) - Biblioteca utilizada para gerar o arquivo executável.

## ✒️ Autor

* **Victor Alves de Oliveira** - Bacharel de Sistemas de Informação - Universidade Federal de Viçosa (UFV-CRP). - victoralvees17@gmail.com

## 🎁 Expressões de gratidão

* Agradecimento ao [Instituto Ieda Picon](https://www.institutoiedapicon.com.br/)
* Agradeço,pelo auxílio na lógica do programa, Gabriel Costa Silva - Bacharel em Engenharia Química - Universidade de São Paulo (USP) - gcosta.gcs@usp.br
