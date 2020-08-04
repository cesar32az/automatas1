/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Paquete;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *
 * @author luis_
 */
public class Class {
        public static void main(String[] args) throws Exception{
            Scanner leer = new Scanner(System.in);
            String cadena;
            String cadena2;
            
    String patronA = "a*ab*(a+b)(ba*(a+b))*";
            System.out.println("Ingrese el patron a: ");
            cadena = leer.nextLine();
            
            Pattern pattern = Pattern.compile(patronA);
            Matcher match = pattern.matcher(cadena);
            
            if(match.find()){
                System.out.println("SI coincide la cadena ");
            } else {
                    System.out.println("NO coincide la cadena ");
                    }
    
    String patronB = "(aa+abc*b)(ab*c)*";
            System.out.println("Ingrese el patron b: ");
            cadena2 = leer.nextLine();
            
             Pattern pat = Pattern.compile(patronB);
             Matcher mat = pat.matcher(cadena2);
             
             if(mat.find()){
                 System.out.println("SI coincide la cadena ");
             } else {
                 System.out.println("NO cincide la cadena ");
             }
             
        }    
}

    
