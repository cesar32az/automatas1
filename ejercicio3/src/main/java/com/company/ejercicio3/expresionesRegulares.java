/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.company.ejercicio3;

import java.util.regex.Matcher;
import java.util.regex.Pattern;
/**
 *
 * @author julio
 */
public class expresionesRegulares {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        /**EJERCICIO 3
         * Generar las expresiones regulares para 
         * que cumplan con los requerimientos 
         */
        String Patron1;
        String Patron2;
        String Patron3;
        String Patron4;
        String Patron5;


         //1
        Patron1 = "";

         //2
        Patron2 = "([abc]*[^bc][abc]*)*";

         //3
        
        Patron3 = "^2[012]*[1]$";

         //4
        Patron4 = "(([aa][ab][ba][bb]){2})*";

         //5
        /**
         * el lenguaje L puede ser visto como una concatenacion de
         * el lenguaje {a} y cadenas a, b, estas pertenecen al lenguaje {a,b}
         * ambos son lenguajes regulares, por lo que su concatenacion tambien es un lenguaje regular
         */
        //el patron quedaria asi
        Patron5 = "^[a][ab]*";


         //Cadenas
        String cadena1;
        String cadena2;
        String cadena3;
        String cadena4;

        cadena1 = "ksdabclas";
        cadena2 = "";
        cadena3 = "20110201";
        cadena4 = "abbaccbcbaba";

        //Tester

        Pattern pat = Pattern.compile(Patron2);  //el patron 
        Matcher mat = pat.matcher(cadena2);
        if(mat.find()){
            System.out.println("Si cumple con la expresion");
        }else{
            System.out.println("No cumple con la expresion");
        }

        

    }
    
}
