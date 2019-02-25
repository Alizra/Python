#-------------------------------------------------------------------------------
Entry_1 = float(input((1*"\n") + " Prendas A Comprar" + " : "))
while (Entry_1 > 0 and Entry_1 < 1000):
    if(Entry_1 > 0):
        Entry_2 = float(input(" Costo Por Prenda " + " : "))    
        #-------------------------------------------------------------------------------
        Result = (Entry_1 * Entry_2)                                       
        Result_1 = (Result / Entry_1)                                     
        Iva = (0.16)                                                      
        Result_2 = (Result_1 * Iva)    
        Result_2_1 = (Result * Iva)                                      
        Result_3 = (Result_2  + Result_1) 
        Result_3_1 = (Result_2_1  + Result)                                                                   
        #--------------------------------------------------------------------------------
        print ((2*"\n") + " Costo Por Una prenda" + (3*"\t"), end = '')
        print (" Costo Por Varias Prendas")
        print ((1*"\n") + (3*" ") + "IVA" + " :" + (8*" "), Result_2, (3*"\t"), end = '')
        print ((3*" ") + "IVA" + " :" + (8*" "), Result_2_1)
        print ((3*" ") + "Sub Total" + " :" + (1*" "), Result_1, (3*"\t"), end = '')
        print ((3*" ") + "Sub Total" + " :" + (1*" "), Result)
        print ((3*" ") + "Total" + " :" + (5*" "), Result_3, (3*"\t"), end = '')
        print ((3*" ") +"Total" + " :" + (5*" "), Result_3_1)
        Entry_1 = int(input((1*"\n") + " Prendas A Comprar" + " : ")) 
    else:
        print ("Saliendo")
        break;
   