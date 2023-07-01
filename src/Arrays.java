public class Arrays {
    public static void main(String[] args) throws Exception {
        //Array initiation
        int[] intArray = new int[7]; //Not a dynamic array, static one
        
        intArray[0]=20; // starts from 0 index
        intArray[1]=35;
        intArray[2]=-15;
        intArray[3]=7;
        intArray[4]=-55;
        intArray[5]=1;
        intArray[6]=-22;

        //print the array

        for(int i=0; i<intArray.length;i++){
            System.out.println(intArray[i]);

        }



    }
}
