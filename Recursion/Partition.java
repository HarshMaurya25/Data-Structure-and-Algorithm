import java.util.ArrayList;
import java.util.List;

public class Partition {
    public static void main(String[] args) {

        String s = "abaca";
        List<List<String>> Answer = new ArrayList<>();
        System.out.println(partitions2(s, new ArrayList<>()).toString());

        // System.out.println(Answer.toString());

    }

    public static void Partitions(String s, List<String> Partition, List<List<String>> Answer) {

        if (s.length() == 0) {
            Answer.add(new ArrayList<>(Partition));
            return;
        }

        for (int i = 0; i < s.length(); i++) {
            String part = s.substring(0, i + 1);

            Partition.add(part);
            Partitions(s.substring(i + 1), Partition, Answer);
            Partition.remove(part);
        }

    }

    public static List<List<String>> partitions2(String s, List<String> partition) {

        List<List<String>> answer = new ArrayList<>();

        // Base case
        if (s.length() == 0) {

            answer.add(new ArrayList<>(partition));

            System.out.println(partition.toString() + " " + answer.toString());
            return answer;
        }

        for (int i = 0; i < s.length(); i++) {

            String part = s.substring(0, i + 1);

            partition.add(part);

            answer.addAll(partitions2(s.substring(i + 1), partition));

            partition.remove(partition.size() - 1);
        }

        return answer;
    }
}