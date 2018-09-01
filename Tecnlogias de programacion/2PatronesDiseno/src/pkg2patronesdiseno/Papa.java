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
public class Papa implements InterfacePapa {
    @Override
   public void dormir(){
   System.out.println("Zzz...");
   }

    @Override
    public void cocina() {
        System.out.println("Huevo con que?");
    }
}
