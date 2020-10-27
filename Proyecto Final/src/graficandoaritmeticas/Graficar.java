/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package graficandoaritmeticas;

import java.io.StringReader;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author julio
 */
public class Graficar {
    
    public static void interpretar(String archivo) {
        analizadores.Sintactico pars;
        
        try {
            pars=new analizadores.Sintactico(new analizadores.Lexico(new StringReader(archivo)));   
            pars.parse();
        } catch (Exception ex) {
            Logger.getLogger(Graficar.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
}
