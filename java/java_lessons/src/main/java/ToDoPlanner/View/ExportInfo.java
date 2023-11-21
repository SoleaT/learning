package ToDoPlanner.View;

import ToDoPlanner.Model.Planner;
import ToDoPlanner.Model.Queue;
import org.jdom2.Document;
import org.jdom2.Element;
import org.jdom2.output.Format;
import org.jdom2.output.XMLOutputter;

import java.io.FileOutputStream;
import java.io.IOException;

public interface ExportInfo {

    String path = "src/main/java/ToDoPlanner/View/fil1.xml";

    static void writeToFile(Queue data) {
        Document doc = new Document();
        doc.setRootElement(new Element("Tasks", "path"));
        Planner t1=null;
        while (Queue.tasksNumber > 0) {
            if (data.getHighQ().size() > 0) {
                t1 = data.leaveQueue(data.getHighQ());
            } else if (data.getMidQ().size() > 0) {
                t1 = data.leaveQueue(data.getMidQ());
            } else if (data.getLowQ().size() > 0) {
                t1 = data.leaveQueue(data.getLowQ());
            }
            if (t1 != null) {
                System.out.println(t1);
                Element elem1 = new Element("Task", "path");
                elem1.setAttribute("id", String.valueOf(t1.getId()));
                elem1.addContent(new Element("taskname", "path").setText("" + t1.getTaskName()));
                elem1.addContent(new Element("username", "path").setText(t1.getUserName()));
                elem1.addContent(new Element("deadline", "path").setText(t1.getDeadline().toString()));
                elem1.addContent(new Element("priority", "path").setText(t1.getPriority().toString()));
                elem1.addContent(new Element("startdate", "path").setText(t1.getStart().toString()));
                doc.getRootElement().addContent(elem1);
            }
        }
        XMLOutputter xmlWriter = new XMLOutputter(Format.getPrettyFormat());
        try {
            xmlWriter.output(doc, new FileOutputStream(path));
            System.out.println("Данные записаны в файл");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}

