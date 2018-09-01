/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pkg2patronesdiseno;

/**
 *
 * @author davca
 */
public class Hijo implements InterfaceMama{
   @Override
   public void chancla(){
   System.out.println("Recibe la chancla");
   }

    @Override
    public void cocina() {
        System.out.println("Aprende Cocina");
    }
    
    InterfacePapa uso = new Papa();
    
    public void dormir(){
       uso.dormir();
    }
}
