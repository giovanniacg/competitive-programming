Dada uma string de caracteres, podemos permutar os caracteres individuais para formar novas strings. Se pudermos impor uma ordem nos caracteres (por exemplo, uma sequência alfabética), então as strings em si podem ser ordenadas, e qualquer permutação dada pode receber um número único que designa sua posição nessa ordem. Por exemplo, a string "acab" gera as seguintes 12 permutações distintas:

```
aabc 1   acab 5   bcaa 9
aacb 2   acba 6   caab 10
abac 3   baac 7   caba 11
abca 4   baca 8   cbaa 12
```

Assim, a string "acab" pode ser caracterizada nesta sequência como a posição 5.  

Escreva um programa que leia uma string e determine sua posição na sequência ordenada das permutações dos seus caracteres constituintes. Observe que o número de permutações pode se tornar muito grande; no entanto, garantimos que nenhuma string será fornecida cuja posição seja maior que \( 2^{31} - 1 = 2.147.483.647 \).  

### Entrada  
A entrada consistirá de uma série de linhas, cada uma contendo uma string. Cada string consistirá de até 30 letras minúsculas, não necessariamente distintas. O arquivo será encerrado por uma linha contendo apenas um único caractere ‘#’.  

### Saída  
A saída consistirá em uma série de linhas, uma para cada linha da entrada. Cada linha conterá a posição da string na sequência, justificada à direita em um campo de largura 10.  

### Exemplo de Entrada  
```
bacaa  
abc  
cba  
#  
```

### Exemplo de Saída  
```
        15  
         1  
         6  
```