# Visualizador-Formas-Geometricas-CG
Obs:O repositório contém um manual detalhado com imagens sobre a execução e utilização do programa.<br/>
Foi utilizadas o PyQT5 (módulo em python para criar GUI apss) para o desenvolvimento e a ferramenta QTDesigner para criar a interface, portanto é necessário ter a o PyQT5 instalada.<br/>

#Sobre

Este programa foi desenvolvido como trabalho para a disciplina de Computação Gráfica. Contém uma interface onde é possível adicionar e visualizar formas geométricas, e realizar transformações como rotação, translação e escala, além de visualizar algoritmos de clipping em tempo real.<br/>
O programa faz a conversão das coordenadas do mundo real(Window) para a viewport no programa, assim os pontos incluidos devem ser referentes aos pontos do window. É possível especificar tanto o tamanho da window e da viewport quantos os pontos a serem desenhados passando um arquivo XML como entrada para o programa. Caso nenhum arquivo seja usado como entrada, a window é criada com os seguintes valores padrão: <br/>
Window: (0,0) a (10,10)<br/>
(Ou seja, os pontos adicionados devem estar incluidos entre (0,0), (0,10), (10,0) e (10,10) para que apareçam na tela. Caso contrário serão desenhados fora da viewport.<br/>
Viewport: Janela de visualização de 640x480 pixels.<br/>
O repositório contém um manual detalhando exatamente como o projeto foi feito e como ele deve ser executado.
