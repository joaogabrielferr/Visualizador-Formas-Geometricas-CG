from Classes import *
import math

#########Algoritmo de Dan Cohen e Ivan Sutherland para clipar retas

#funcao para calcular o codigo de um ponto
def codigo(x,y,xmin,xmax,ymin,ymax):
    c = 0
    if y > ymax : c = 8
    elif y < ymin: c = 4

    if x > xmax : c+=2
    elif x < xmin : c+=1

    return c


def cohen_sutherland(x0,y0,x1,y1,xmin,xmax,ymin,ymax):
    accept = False
    done = False
    codA = codigo(x0,y0,xmin,xmax,ymin,ymax)
    codB = codigo(x1,y1,xmin,xmax,ymin,ymax)
    codOut = 0

    while done == False:
        if codA | codB == 0:
            accept = True
            done = True
            return [x0,y0],[x1,y1]
        elif codA & codB != 0:
            return [float('inf')],[float('inf')]
        else:
            if codA != 0: codOut = codA
            else: codOut = codB
            if codOut & 0x08:
                x=x0+(x1-x0)*(ymax-y0)/(y1-y0)
                y=ymax
            elif codOut & 0x04:
                x=x0+(x1-x0)*(ymin-y0)/(y1-y0)
                y=ymin
            elif codOut & 0x02:
                y=y0+(y1-y0)*(xmax-x0)/(x1-x0)
                x=xmax
            elif codOut & 0x01:
                y=y0+(y1-y0)*(xmin-x0)/(x1-x0)
                x=xmin
            if codOut == codA:
                x0=x; y0=y; codA = codigo(x0,y0, xmin, xmax, ymin, ymax)
            else:x1=x; y1=y; codB = codigo(x1,y1, xmin, xmax, ymin, ymax)



########Algoritmo de ivan Sutherland e Gary Hodgman para clipar poligonos
#Modificado de: https://www.geeksforgeeks.org/polygon-clipping-sutherland-hodgman-algorithm-please-change-bmp-images-jpeg-png/


#retorna o valor x de um ponto de interccao de duas retas
def x_interceccao( x1,  y1,  x2,  y2, x3,  y3,  x4,  y4):

    num = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    num = float(num)
    den = float(den)
    return float(num/den)
  

#retorna o valor y de um ponto de interccao de duas retas
def y_interceccao( x1,  y1,  x2,  y2,x3,  y3,  x4,  y4):

    num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    num = float(num)
    den = float(den)
    return float(num/den)

  
def clipa( poligono, tam_poligono,x1,  y1,  x2,  y2):
    pontos_novos = []
    novo_tamanho = 0
    
    # for i in range(100):
    #     p = Ponto(0.0,0.0,0.0)
    #     pontos_novos.append(p)
  
    #(ix,iy),(kx,ky) sao as coordenadas dos pontos
    for i in range(tam_poligono):
        #i e k formam uma linha no poligono
        if i == tam_poligono - 1:
            k = 0
        else: k = i + 1
        ix = poligono[i].x
        iy = poligono[i].y
        kx = poligono[k].x
        ky = poligono[k].y
  
        #calculando posicao do primeiro ponto
        i_pos = (x2-x1) * (iy-y1) - (y2-y1) * (ix-x1)
  
        #calculando posicao do segundo ponto
        k_pos = (x2-x1) * (ky-y1) - (y2-y1) * (kx-x1)
  
        #caso 1: ambos os pontos estao dentro da window
        if i_pos < 0  and k_pos < 0 :
            #somente o segundo ponto eh adicionado
            p = Ponto(float(kx),float(ky),0.0)
            #pontos_novos[novo_tamanho] = p
            pontos_novos.append(p)
            novo_tamanho+=1
        #caso 2: somente o primeiro ponto esta fora da window
        elif i_pos >= 0  and k_pos < 0:
            #ponto de intersecao com a window e segundo ponto sao adicionados
            x = x_interceccao(x1,y1, x2, y2, ix, iy, kx, ky)
            y = y_interceccao(x1,y1, x2, y2, ix, iy, kx, ky)
            p = Ponto(float(x),float(y),0.0)
            #pontos_novos[novo_tamanho] = p
            pontos_novos.append(p)
            novo_tamanho+=1
            p = Ponto(float(kx),float(ky),0.0)
            #pontos_novos[novo_tamanho] = p
            novo_tamanho+=1
            pontos_novos.append(p)
        #case 3: somente o segundo ponto esta fora da window
        elif i_pos < 0  and k_pos >= 0:
            #somente o ponto de interseccao com a window eh adicionado
            x = x_interceccao(x1,y1, x2, y2, ix, iy, kx, ky)
            y = y_interceccao(x1,y1, x2, y2, ix, iy, kx, ky)
            p = Ponto(float(x),float(y),0.0)
            #pontos_novos[novo_tamanho] = p
            pontos_novos.append(p)
            novo_tamanho+=1
  
        #Caso 4: Ambos os pontos estao fora, nao adiciona nenhum        


    tam_poligono = novo_tamanho

    # for i in range(0,tam_poligono):
    #     poligono[i] = pontos_novos[i]

    poligono = pontos_novos
 
    return poligono,tam_poligono


  
#Algoritmo de Sutherland-Hodgman para clipar poligonos
def sutherland_hodgman(poligono, tam_poligono,window,tam_window):
    #i e k sao dois pontos consecutivos
    for i in range(tam_window):
        if i == tam_window - 1:
            k = 0
        else: k = i + 1
        poligono,tam_poligono = clipa(poligono, tam_poligono, window[i].x,window[i].y, window[k].x,window[k].y)

    # print("apos clipagem:",end = "")
    # for i in range(len(poligono)):
    #     print("(",poligono[i].x,',',poligono[i].y,')',end = "")
    # print("\n")
    return poligono,tam_poligono



#########Algoritmo para ordenar os pontos em sentido horario
#Fonte:https://stackoverflow.com/questions/41855695/sorting-list-of-two-dimensional-coordinates-by-clockwise-angle-using-python

origin = [0,0]
refvec = [0,1]

def clockwiseangle_and_distance(point):
    # Vector between point and the origin: v = p - o
    vector = [point.x-origin[0], point.y-origin[1]]
    # Length of vector: ||v||
    lenvector = math.hypot(vector[0], vector[1])
    # If length is zero there is no angle
    if lenvector == 0:
        return -math.pi, 0
    # Normalize vector: v/||v||
    normalized = [vector[0]/lenvector, vector[1]/lenvector]
    dotprod  = normalized[0]*refvec[0] + normalized[1]*refvec[1]     # x1*x2 + y1*y2
    diffprod = refvec[1]*normalized[0] - refvec[0]*normalized[1]     # x1*y2 - y1*x2
    angle = math.atan2(diffprod, dotprod)
    if angle < 0:
        return 2*math.pi+angle, lenvector
    return angle, lenvector



#encontra centro do poligono
def centroid(vertices):
    x = [vertice.x for vertice in vertices]
    y = [vertice.y for vertice in vertices]
    tam = len(vertices)
    xr = sum(x)/tam
    yr = sum(y)/tam

    return xr,yr


def ordenaSentidoHorario(pol):
    x,y = centroid(pol)
    origin[0] = x
    origin[1] = y
    pol = sorted(pol,key = clockwiseangle_and_distance)

    return pol



#Implementacao de um algoritmo de clipagem de poligonos utilizando o algoritmo de Cohen e Sutherland
#para clipagem de retas
def clipaPoligonos(poligono,xmin,xmax,ymin,ymax):

    novo_pol = []

    for i in range(len(poligono)-1):
        a,b = cohen_sutherland(poligono[i].x,poligono[i].y,poligono[i+1].x,poligono[i+1].y,xmin,xmax,ymin,ymax)
        if a[0] != float('inf'):
            p1 = Ponto(float(a[0]),float(a[1]),0.0)
            p2 = Ponto(float(b[0]),float(b[1]),0.0)
            novo_pol.append(p1)
            novo_pol.append(p2)
    
    a,b = cohen_sutherland(poligono[len(poligono)-1].x,poligono[len(poligono)-1].y,poligono[0].x,poligono[0].y,xmin,xmax,ymin,ymax)
    if a[0] != float('inf'):
        p1 = Ponto(float(a[0]),float(a[1]),0.0)
        p2 = Ponto(float(b[0]),float(b[1]),0.0)
        novo_pol.append(p1)
        novo_pol.append(p2)
    #novo_pol = ordenaSentidoHorario(novo_pol)

    return novo_pol

