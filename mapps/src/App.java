import java.io.IOException;
import java.util.ArrayList;

import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class App {

    private final static String inizio = "https://nominatim.openstreetmap.org/search?q=";
    private final static String fine ="&format=xml&polygon_geojson=1&addressdetails=1";

    public static void main(String[] args) throws Exception {


        String ricerca="mariano+comense,+monnet";

        String source=inizio+ricerca+fine;

        String file = "";
                try {
                    file = XMLReader.fetchFromWeb(source);
                    XMLReader.printToFile(file, "data.xml");
                } catch (IOException e1) {
                    // TODO Auto-generated catch block
                    e1.printStackTrace();
                }
                
        Element root= XMLReader.getRootElementFromXML("data.xml");

        NodeList Childs = root.getElementsByTagName("place");
        
        ArrayList<Place> lista = new ArrayList<Place>();

        for (int i = 0; i < Childs.getLength(); i++) {
            lista.add(new Place(Childs.item(i)));
        }

        System.out.println(lista.get(0));
        

    }
}

