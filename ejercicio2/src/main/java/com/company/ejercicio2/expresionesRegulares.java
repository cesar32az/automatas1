/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.company.ejercicio2;

import java.util.regex.Matcher;
import java.util.regex.Pattern;
/**
 *
 * @author julio
 * EL EJERCICIO SE ENCUENTRA MAS ABAJO
 */ 
public class expresionesRegulares {

    /**
     * @param args the command line arguments
     */
    public static void main(final String[] args) {
        //EJEMPLO DE LA CLASE
        // TODO code application logic here
        System.out.println("hola mundo");
        // conjunto de numeros del 1 al 5
        String patronA = "[0-5]";

        // conjunto de letras de "a" a "c"
        String patronB = "[a-c]";

        // conjunto de todas las letras minusculas
        String patronC = "[a-z]";

        // conjunto de numeros
        String patronD = "[0-9]";

        // ejemplo con tipo de dato string
        String textoAlfanumerico = "0123aaaa";
        System.out.println("Texto alfanumerico:" + textoAlfanumerico);

        String replace1 = textoAlfanumerico.replaceAll(patronA, "X");
        System.out.println("Reemplazo de numeros con X: " + replace1);

        String replace2 = textoAlfanumerico.replaceAll(patronB, "X");
        System.out.println("Reemplazo de letras con X: " + replace2);


        //[0-5][a-c];
        //String patronComplejo = patronA + patronB;

        //[a-c]*[0-5]*
        //String patronComplejo = patronA + "*" + patronB + "*";

        //"[a-z]+"

        // + = una coincidencia
        // * = ninguna o muchas

        //String patronComplejo = "(" + patronA + patronC + ")+";
        String patronComplejo = "(" + patronC + ")+";

        String texto = "hola, aacc este bbcc es mi 55222aaa texto 2663aaaa   blah blah";
        System.out.println("patron complejo:" + patronComplejo);
        System.out.println(texto);

        Pattern pattern = Pattern.compile(patronComplejo);
        Matcher matcher = pattern.matcher(texto);

        // buscar ocurrencias
        while (matcher.find()) {
            System.out.println("Encontrado:" + matcher.group());
        }

        //EJERCICIO 2
        
        //PARTE 1
        
        String patronE = "[0]";
        
        
        String datos = "510350570";
        String remplaso0 = datos.replaceAll(patronE, "x");
        System.out.println("Remplaso de numeros 0 con una x: " + remplaso0);

        //PARTE 2

        //cadenas a escanear
        String cadena1;
        String cadena2;
        String cadena3;
        String cadena4;
        
        //cadenas que si cumplen
        cadena1= "palabra";
        cadena2= "hola";
        cadena3= "otras palabras";

        //cadena que no cumple
        cadena4= "he";

        Pattern pat = Pattern.compile("[a-z]{3}");  //el patron 
        Matcher mat = pat.matcher(cadena1);
        if(mat.find()){
            System.out.println("Si cumple con la expresion");
        }else{
            System.out.println("Nel mijo intentelo de nuevo");
     }

    }
    
}
