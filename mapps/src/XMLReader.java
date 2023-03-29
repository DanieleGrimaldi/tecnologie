import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.URL;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.xml.sax.SAXException;

public class XMLReader {
    private static final String BASE_PATH = "";

    public static String fetchFromWeb(URL url) throws IOException{
        String file = "";
        BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream()));
        String line = "";
        while((line = in.readLine()) != null) file += line + "\n";
        in.close();
        return file;
    }
    
    public static String fetchFromWeb(String path) throws IOException {
        URL url = new URL(path);
        return fetchFromWeb(url);
    }

    public static void printToFile(String file, String path) throws FileNotFoundException{
        PrintWriter pw = new PrintWriter(BASE_PATH + path);
        pw.write(file);
        pw.close();
    }

    public static Element getRootElementFromXML(String file) throws ParserConfigurationException, SAXException, IOException{
        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = dbf.newDocumentBuilder();
        Document document = builder.parse(file);

        return document.getDocumentElement();
    }
}