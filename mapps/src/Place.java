import java.util.HashMap;
import java.util.Map;

import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class Place {
    private final HashMap<String, String> attributes = new HashMap<>();
    private final HashMap<String, String> childs = new HashMap<>();

    public Place(Node place){

        NamedNodeMap attributi = place.getAttributes();
        for(int i = 0; i < attributi.getLength(); i++){
            Node n = attributi.item(i);
            attributes.put(n.getNodeName(), n.getNodeValue());
        }


        NodeList figli = place.getChildNodes();
        for(int i = 0; i < figli.getLength(); i++){
            Node n = figli.item(i);
            if(!n.getNodeName().equals("text#")){
                childs.put(n.getNodeName(), n.getTextContent());
            }
            
        }
        
    }

    @Override
    public String toString() {
        String s = "";
        for (Map.Entry<String, String> entry : childs.entrySet()) {
            s+=("Key : " + entry.getKey() + " Value : " + entry.getValue())+"\n";
        }
        return s;
    }
}
