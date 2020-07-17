/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package automatas;

/**
 *
 * @author jsgl8
 */
import java.util.*;
import static jdk.nashorn.internal.runtime.regexp.joni.Syntax.Java;
public class Conjunto {
    public SortedSet a;
    public Conjunto() {
        a= new TreeSet();
    }
    public SortedSet getA() {
        return a;
    }
    public void setA(SortedSet a) {
        this.a = a;
    }
    public void inserta(Object e){
        if(a.add(e)==false){
        System.out.println("Elemento+e+" + "repetido!!..No se pudo insertar");
            
                    
        }
    }
    public void elimina(Object e){
        if(a.remove(e)){
            System.out.println("Elemento+e+" +": ha sido eliminado");
        }else{
            System.out.println("Note el elemento a eliminar");
        }
    }
    public SortedSet subconjuntosup(Object e){
        SortedSet b=new TreeSet();
        b=a.tailSet(e);
        return b;

    }
    public SortedSet subconjuntoinf(Object e){
        SortedSet b=new TreeSet();
        b=a.headSet(e);
        return b;
    }
    public SortedSet subconjuntoentre(Object ei, Object ef){
        SortedSet b=new TreeSet();
        b=a.subSet(ei, ef);
        return b;
    }
    public SortedSet union(SortedSet a, SortedSet b){
        a.addAll(b);
        return a;
    }
    public SortedSet interseccion(SortedSet a, SortedSet b){
        a.retainAll(b);
        return a;
    }
    public SortedSet diferencia(SortedSet a, SortedSet b){
        a.removeAll(b);
        return a;
    }

            
}
